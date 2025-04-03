from androguard.core.apk import APK
from androguard.core.axml import ARSCParser, ARSCResType
from androguard.core.dex import DEX
from androidemu.emulator import Emulator
from androidemu.utils.memory_helpers import read_utf8
from unicorn.unicorn_const import UC_HOOK_MEM_READ_UNMAPPED, UC_HOOK_MEM_UNMAPPED

from unicorn import UC_HOOK_CODE
import unicorn
from unicorn.arm_const import *
import lief
from arc4 import ARC4
from kavanoz.unpack_plugin import Unpacker
import os


class LoaderCoper(Unpacker):
    def __init__(self, apk_obj, dvms, output_dir):
        super().__init__(
            "loader.coper", "Unpacker for coper", apk_obj, dvms, output_dir
        )

    def lazy_check(self, apk_object: APK, dvms: list[DEX]) -> bool:
        arm32_native_libs = [
            filename
            for filename in self.apk_object.get_files()
            if filename.startswith("lib/armeabi-v7a")
        ]
        if len(arm32_native_libs) >= 5:
            self.logger.info(
                "Found more than 5 native libs, this is probably NOT a coper"
            )
            return False
        else:
            self.logger.info("Found less than 5 native libs, this is probably a coper")
            return True

    def start_decrypt(self, native_lib: str = ""):
        arm32_native_libs = [
            filename
            for filename in self.apk_object.get_files()
            if filename.startswith("lib/armeabi-v7a")
        ]
        if len(arm32_native_libs) == 0:
            self.logger.info("No native lib 😔")
            return
        if len(arm32_native_libs) != 1:
            self.logger.info("Not sure this is copper but continue anyway")

        for arm32_lib in arm32_native_libs:
            self.logger.info(f"Trying to decrypt with {arm32_lib}")
            if self.decrypt_library(arm32_lib):
                return

    def decrypt_library(self, native_lib: str) -> bool:
        fname = native_lib.split("/")[-1]
        with open(fname, "wb") as fp:
            fp.write(self.apk_object.get_file(native_lib))
        self.target_lib = fname
        # Show loaded modules.
        self.resolved_strings = []
        if not self.init_lib():
            return
        self.logger.info("Loaded modules:")
        if not self.setup_hook():
            self.logger.info("Failed to setup hooks maybe no srtcat symbol ?")
            self.logger.info("Trying to find strings in stack")
        # self.emulator.mu.hook_add(UC_HOOK_CODE, self.hook_debug_print)
        self.emulator.uc.hook_add(UC_HOOK_MEM_READ_UNMAPPED, self.hook_unmapped_read)

        try:
            self.emulator.call_symbol(self.target_module, self.target_function.name)
        except Exception as e:
            self.logger.info(f"Exception while calling symbol: {e}")
            if len(self.resolved_strings) == 0:
                self.logger.info("No strings found")
                return
        self.logger.info(f"Androidemu extracted rc4 key: {self.resolved_strings[0]}")
        if self.decrypt_files(self.resolved_strings[0]):
            self.logger.info("Decryption successful")
            os.remove(self.target_lib)
            return True
        else:
            # Now this can be because dex\n035 is added after decryption of thhe file. We can also get file name from resolved strings.
            if len(self.resolved_strings) == 2 and self.apk_object.get_package() in self.resolved_strings[1]:
                # This is tricky part. Sometimes :raw points to different point from resources.arsc/raw..
                # But instead we can search .../raw/filename in all files
                enc_filename = self.resolved_strings[1].split(":")[1]
                self.logger.debug(f"Looking for file : {enc_filename}")
                for f in self.apk_object.get_files():
                    if enc_filename in f:
                        if self.decrypt_file(self.resolved_strings[0],f):
                            os.remove(self.target_lib)
                            return True
                    else:
                        # Here we go...
                        # I dont know this is obfuscation or something else with androguard library
                        # We need to manually find mapping of res/somefile with raw/targetfile by parsing resources.arsc
                        arsc_file = self.apk_object.get_file("resources.arsc")
                        arsc_parser = ARSCParser(arsc_file)
                        # Find item <ARSCResType(start=0x3e0, id=0x2, flags=0x0, entryCount=2, entriesStart=0x5c, mResId=0x7f020000, table:raw)>
                        # then next item will be rids of raw files [(0, 2130837504), (16, 2130837505)]
                        items = arsc_parser.get_items(package_name=self.apk_object.get_package())
                        for i in range(len(items)):
                            if type(items[i]) ==  ARSCResType:
                                # Found res type
                                if items[i].get_type() == "raw":
                                    # Found raw type
                                    # items[i+1] hold list of resource ids of raw type files
                                    rids = [x[1] for x in items[i+1]]
                                    self.logger.debug(f"Found rids : {rids}")
                                    for rid in rids:
                                        curr_res_config = arsc_parser.get_resolved_res_configs(rid=rid)
                                        xml_name = arsc_parser.get_resource_xml_name(r_id=rid)
                                        if enc_filename in xml_name and len(curr_res_config) > 0:
                                            curr_res_file_name = curr_res_config[0][1]
                                            if self.decrypt_file(self.resolved_strings[0],curr_res_file_name):
                                                os.remove(self.target_lib)
                                                return True

                        return False
        os.remove(self.target_lib)
        return False

    def decrypt_files(self, rc4key: str):
        for filepath in self.apk_object.get_files():
            fd = self.apk_object.get_file(filepath)
            dede = ARC4(rc4key.encode("utf-8"))
            dec = dede.decrypt(fd)
            if self.check_and_write_file(dec):
                return True
        return False

    def decrypt_file(self,rc4key:str, filename:str):
        fd = self.apk_object.get_file(filename)
        arc4 = ARC4(rc4key.encode("utf-8"))
        dec = arc4.decrypt(fd)
        dec = b"dex\n035" + dec
        if self.check_and_write_file(dec):
            return True
        return False


    def init_lib(self):
        target_ELF = lief.ELF.parse(self.target_lib)
        java_exports = [
            jf for jf in target_ELF.exported_functions if jf.name.startswith("Java_")
        ]
        if len(java_exports) == 0:
            return False
        if len(java_exports) > 1:
            self.logger.info("Not sure this is copper but continue anyway")

        self.target_function = java_exports[0]
        # Configure logging

        # Initialize emulator
        self.emulator = Emulator(vfp_inst_set=True)
        libc_path = os.path.join(os.path.dirname(__file__), "androidnativeemu/libc.so")
        self.emulator.load_library(libc_path, do_init=False)
        self.target_module = self.emulator.load_library(self.target_lib, do_init=False)
        return True

    def hook_debug_print(self, uc, address, size, user_data):
        instruction = uc.mem_read(address, size)
        instruction_str = "".join("{:02x} ".format(x) for x in instruction)

        print(
            "# Tracing instruction at 0x%x, instruction size = 0x%x, instruction = %s"
            % (address, size, instruction_str)
        )

    def hook_unmapped_read(self, uc, access, address, size, value, user_data):
        # Read stack and print it byte per byte
        self.logger.debug("Trying to read from address : %x" % address)
        sp = uc.reg_read(UC_ARM_REG_SP)
        bp = uc.reg_read(UC_ARM_REG_R11)
        self.logger.debug(f"Stack pointer: {hex(sp)}, Base pointer: {hex(bp)}")

        # Problem here is we don't know the size of the stack data
        # If we read too much we will get unmapped memory error
        # But we can extract stack size from function prologue

        stack_size = self.extract_stack_size_from_function_prologue(
            self.emulator.uc, self.target_function, self.target_lib_base
        )
        if stack_size == 0:
            return
        stack_data = uc.mem_read(sp, stack_size)
        # Stack data contains list of strings ends with \x00 but there are also
        # filler \x00 bytes in between them. We need to split them.
        stack_data = stack_data.split(b"\x00")
        # Filter out empty strings
        stack_data = [x for x in stack_data if x != b""]
        # Decode strings
        stack_data = [x for x in stack_data]
        self.logger.debug(f"Stack data: {stack_data}")
        self.resolved_strings.append(stack_data[-1].decode("utf-8"))
        # Print stack

    def setup_hook(self):
        for module in self.emulator.modules:
            if module.filename == self.target_lib:
                self.logger.info("[0x%x] %s" % (module.base, module.filename))
                self.target_lib_base = module.base
                # emulator.mu.hook_add(
                # UC_HOOK_CODE,
                # hook_code,
                # begin=module.base + java_func_obj.address,
                # end=module.base + java_func_obj.address + (0x2198 - 0x1FC1),
                # )
                strncat = module.find_symbol("__strncat_chk")
                if strncat == None:
                    self.logger.info("No strncat symbol 😔")

                    self.logger.info("maybe octo2 ?")
                    unpack_dynlib = module.find_symbol("_ZN8WrpClass13unpack_dynlibEv")
                    if unpack_dynlib == None:
                        self.logger.info("No unpack_dynlib symbol 😔")
                        return False
                    self.logger.debug(f"{hex(unpack_dynlib.address)} unpack_dynlib addr")
                    replace_loader = module.find_symbol("_ZN8WrpClass14replace_loaderEb")

                    self.emulator.uc.hook_add(
                        UC_HOOK_CODE,
                        self.hook_unpack_dynlib,
                        begin=unpack_dynlib.address,
                        end=unpack_dynlib.address + 1,
                        user_data=replace_loader.address,
                    )
                    return False
                self.logger.debug(f"{hex(strncat.address)} strcat_chk addr")
                self.emulator.uc.hook_add(
                    UC_HOOK_CODE,
                    self.hook_strncat,
                    begin=strncat.address,
                    end=strncat.address + 1,
                )
                self.emulator.uc.hook_add(UC_HOOK_MEM_UNMAPPED, self.hook_mem_read)
                self.emulator.uc.hook_add(UC_HOOK_MEM_READ_UNMAPPED, self.hook_mem_read)
                return True
        return False

    def hook_mem_read(self, uc, access, address, size, value, user_data):
        pc = uc.reg_read(UC_ARM_REG_PC)
        data = uc.mem_read(address, size)
        self.logger.debug(
            ">>> Memory READ at 0x%x, data size = %u, pc: %x, data value = 0x%s"
            % (address, size, pc, data.hex())
        )

    def hook_strncat(self, uc: unicorn.unicorn.Uc, address, size, user_data):
        # print(f"current strncat hook addr : {hex(address)}")
        r0 = uc.reg_read(UC_ARM_REG_R0)
        # print(f"current strncat hook r0 : {hex(r0)}")
        r1 = uc.reg_read(UC_ARM_REG_R1)
        max_size = uc.reg_read(UC_ARM_REG_R2)
        # print(f"current strncat hook r1 : {hex(r1)}")
        cur_key = read_utf8(uc, r0)
        added = read_utf8(uc, r1)
        final_str = cur_key + added
        if len(final_str) == max_size - 1:
            self.logger.debug(f"current strncat hook final_str : {final_str}")
            self.resolved_strings.append(final_str)
            if len(self.resolved_strings) > 10:
                self.emulator.uc.emu_stop()

    def hook_unpack_dynlib(self, uc: unicorn.unicorn.Uc, address, size, user_data):

        self.logger.debug("unpack_dynlib triggered : %x" % address)
        sp = uc.reg_read(UC_ARM_REG_SP)
        self.logger.debug(f"Stack pointer: {hex(sp)}")
        # Problem here is we don't know the size of the stack data, we can go back calle function
        # and read prologue to extract stack size

        # Get stack size from replace_loader

        should_be_subw = uc.mem_read(
            user_data - 1 + 8, 0x4
        )
        if should_be_subw[1] != 0xb0:
            self.logger.debug("Bad instruction to find stack size")
            return 0
        # a6b0 -> read 0xa6 &= 0x7f
        stack_size = (should_be_subw[0] & 0x7f ) << 2

        self.logger.debug(f"Found stack size at replace_loader : {stack_size}")
        stack_data = uc.mem_read(sp, stack_size+12)
        # Stack data contains list of strings ends with \x00 but there are also
        # filler \x00 bytes in between them. We need to split them.
        stack_data = stack_data.split(b"\x00")
        # Filter out empty strings
        stack_data = [x for x in stack_data if x != b""]
        # Decode strings
        stack_data = [x for x in stack_data]
        self.logger.debug(f"Stack data: {stack_data}")
        # Some sanity checks
        if len(stack_data) > 5:
            # example stack strings:
            # - Q3DCe5ZIFftphISZwNpNYy4vA1Qvyyjt
            # - replace_loader
            # - 7a1bc825b313fd55
            # - b313fd551c1f219b
            # - com.handedfastee5
            # - com.handedfastee5:raw/kyndwjzbyg0
            # get rc4 key
            self.resolved_strings.append(stack_data[-1].decode("utf-8"))
            # walk backward and find raw file
            stack_data.reverse()
            for i in range(0,len(stack_data),2):
                if stack_data[i] in stack_data[i+1]:
                    # we found the file
                    self.logger.debug(f'RC4 encrypted file name : {stack_data[i+1].decode("utf-8")}')
                    self.resolved_strings.append(stack_data[i+1].decode("utf-8"))
                    break


            self.emulator.uc.emu_stop()

    def extract_stack_size_from_function_prologue(
        self, uc, target_function, target_lib_base
    ) -> int:
        # 00001ee8  f0b5       push    {r4, r5, r6, r7, lr} {var_4} {__saved_r7} {__saved_r6} {__saved_r5} {__saved_r4}
        # 00001eea  03af       add     r7, sp, #0xc {__saved_r7}
        # 00001eec  2de9000f   push    {r8, r9, r10, r11} {__saved_r11} {__saved_r10} {__saved_r9} {__saved_r8}
        # 00001ef0  adf2144d   subw    sp, sp, #0x414

        # We need 4th instruction, if its sub/subw with parameters sp,sp then get the value
        # of the last parameter
        # F it just read bytes
        # -1 is for thumb mode
        should_be_subw = uc.mem_read(
            target_lib_base + target_function.value - 1 + 8, 0x4
        )
        if should_be_subw[0] != 0xAD:
            return 0
        # adf2144d -> read 0x14 and 0x4d bytes -> convert it to 0x414

        stack_size = should_be_subw[2] | (((should_be_subw[3] & 0xF0) >> 4) << 8)
        self.logger.info(f"Stack size must be {hex(stack_size)}")
        return stack_size

    # def hook_code(self,uc: unicorn.unicorn.Uc, address, size, user_data):
    # global rc4_key
    # if address == coper_base + java_func_obj.address + (0x2198 - 0x1FC1):
    # sp = uc.reg_read(UC_ARM_REG_SP)
    # rc4_key = read_utf8(uc, sp + 0x46F)

    # print(
    # "# Tracing instruction at 0x%x, instruction size = 0x%x, instruction = %s"
    # % (address, size, instruction_str)
    # )
    # if instruction[0] == 0xA0 and instruction[1] == 0x47 and len(instruction) == 2:
    # r1 = uc.reg_read(UC_ARM_REG_R1)
    # print(r1)
    # print(uc.mem_read(r1, 1))
