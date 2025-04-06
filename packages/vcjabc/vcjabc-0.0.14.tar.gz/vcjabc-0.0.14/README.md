This is a small and minimal project for DOCX/DOCM formats manipulation. Module is a wrapper on the document handler executable. 
Document handler is a standalone `C#/.NET` application based on OpenXmlLibrary. 
For now the Windows and Linux are supported.


## Install

    pip install vcjabc


## Usage
```
from vcjabc import Word

manager = Word()

# Create empty DOCX file:
manager.create_docx(file_name="example.docx")

# Create empty DOCM file:
manager.create_docm(file_name="example.docm")

# Convert DOCX to DOCM:
manager.convert_docx_to_docm("example.docx", "example_converted_docx_to_docm.docm")

# Convert DOCM to DOCX:
manager.convert_docm_to_docx("example.docm", "example_converted_docm_to_docm.docx.docx")

# Add macro to DOCM file (source `vbaProject.bin` would be prepared beforehand, use MS Word for that):
manager.add_macro_to_docm("test_macro_document.docm", vba_project_file_path, "test_macro_document_with_macro.docm")

# Add custom property to DOCX/DOCM file:
manager.add_custom_properties("test_macro_document_with_macro.docm", paramz)

```


## TODO
Enhance functionality.


## BUGS
Present.


## Useful linkx
- [Github](https://github.com/sphynkx) with sources
- [PyPI](https://pypi.org/project/vcjabc) release

