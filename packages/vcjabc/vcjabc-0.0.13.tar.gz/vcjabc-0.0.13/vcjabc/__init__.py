#!/usr/bin/python
import os
import subprocess
import platform
import os
import stat



class Word:
    def __init__(self, file_path=None):
        self.file_path = file_path
        self.os_name = platform.system()
        self.exe_path = self._get_executable_path()


    def _get_executable_path(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        bin_dir = os.path.join(script_dir, "bin")
        
        if self.os_name == 'Windows':
            return os.path.join(bin_dir, "handler_windows.exe")
        elif self.os_name == 'Linux':
            exe_path = os.path.join(bin_dir, "handler_linux")
            
            # Check and set executable attribute for Linux bunary
            if not os.access(exe_path, os.X_OK):
                try:
                    os.chmod(exe_path, stat.S_IXUSR | stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH)
                except PermissionError:
                    raise PermissionError(f"Cannot set attribute for {exe_path}. Check access rights.")
            
            return exe_path
        else:
            raise ValueError("Unsupported OS")


    def _call_binary(self, command, *args, paramz=None):
        cmd = [self.exe_path, command] + [os.path.abspath(arg) for arg in args]
        ## Xack-fix for add_custom_properties() to exclude paramz from adding path
        if paramz != None: cmd += [paramz]
        print(f"\nRunning command (document_manager.py): {' '.join(cmd)}\n")
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0:
            print(f"Command failed with error: {result.stderr}")
            raise RuntimeError(f"Error running command: {cmd}\n{result.stderr}")
        return result.stdout


    def create_docx(self, file_name="new_document.docx"):
        self._call_binary("create_docx", file_name)
        self.file_path = file_name
        print(f"Document '{self.file_path}' created successfully.")


    def create_docm(self, file_name="new_document.docm"):
        self._call_binary("create_docm", file_name)
        self.file_path = file_name
        print(f"Document '{self.file_path}' created successfully.")


    def convert_docx_to_docm(self, input_file, output_file=None):
        if output_file is None:
            output_file = input_file.replace(".docx", ".docm")
        self._call_binary("convert_docx_to_docm", input_file, output_file)
        print(f"File '{input_file}' converted to '{output_file}' successfully.")


    def convert_docm__to_docx(self, input_file, output_file=None):
        if output_file is None:
            output_file = input_file.replace(".docm", ".docx")
        self._call_binary("convert_docm__to_docx", input_file, output_file)
        print(f"File '{input_file}' converted to '{output_file}' successfully.")


    def add_macro_to_docm(self, docm_file, vba_project_file, output_file=None):
        if output_file is None:
            output_file = docm_file
        self._call_binary("add_macro_to_docm", docm_file, vba_project_file, output_file)
        print(f"Macro added to file '{output_file}' successfully.")


    def add_custom_properties(self, docm_file, paramz):
        self._call_binary("add_custom_properties", docm_file, paramz=f"{paramz}")
        print(f"DBG (document_manager.py): {paramz=}")
        print(f"Custom property added to file '{docm_file}' successfully.")



if __name__ == '__main__':
    manager = Word()
    try:
        manager.create_docx(file_name="example.docx")
        manager.create_docx(file_name="test_document.docx")
        manager.convert_docx_to_docm("test_document.docx", "test_document_converted.docm")
        manager.convert_docx_to_docm("example.docx", "example_converted.docm")

        if os.path.exists("test_document_converted.docm"):
            print("Test passed: DOCM file created successfully.")
        else:
            print("Test failed: DOCM file not created.")

        manager.create_docm(file_name="test_macro_document.docm")
        manager.convert_docm_to_docx("test_macro_document.docm", "test_macro_document_converted.docx")

        if os.path.exists("test_macro_document_converted.docx"):
            print("Test passed: DOCX file created successfully.")
        else:
            print("Test failed: DOCX file not created.")

        vba_project_file_path = "vbaProject.bin"
        manager.add_macro_to_docm("test_macro_document.docm", vba_project_file_path, "test_macro_document_with_macro.docm")

        if os.path.exists("test_macro_document_with_macro.docm"):
            print("Test passed: Macro added to DOCM file successfully.")
        else:
            print("Test failed: Macro not added to DOCM file.")

        paramz = "Test custom paramenter"
        manager.add_custom_properties("test_macro_document_with_macro.docm", paramz)

    except Exception as e:
        print(f"Test error: {e}")
