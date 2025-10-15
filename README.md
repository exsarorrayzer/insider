Insider - Python Code Obfuscation Library

(https://img.shields.io/badge/version-1.1.0-blue)
(https://img.shields.io/badge/python-3.7%2B-green)
(https://img.shields.io/badge/license-MIT-yellow)

Insider is a powerful and modular Python code obfuscation library designed to protect your Python source code from reverse engineering and unauthorized analysis. It provides multiple obfuscation techniques that can be used individually or combined for maximum protection.

🚀 Features

• Variable Renaming: Automatically renames variables, functions, and classes to random names

• String Obfuscation: Encodes string literals using Base64 encoding

• Import Obfuscation: Transforms import statements to dynamic imports

• Comment Removal: Strips all comments from the source code

• Marshall Encoding: Compiles and encodes code using Python's marshal module

• Zlib Compression: Compresses code using zlib with Base64 encoding

• Modular Design: Use individual obfuscation methods or combine them

• CLI Interface: Easy-to-use command-line interface

• Colorful Output: Beautiful colored terminal output with Colorama

📦 Installation

### From GitHub

```bash
pip install git+https://github.com/exsarorrayzer/insider.git
```

### Local Development Installation

```bash
git clone https://github.com/exsarorrayzer/insider.git
cd insider
pip install -e .
```

🛠 Quick Start

Command Line Usage

```bash
# Basic obfuscation
insider -file main.py -to obfuscated_main.py

# Advanced obfuscation with specific methods
insider -file main.py -to protected.py -methods rename_variables obfuscate_strings marshall_encode

# Show all available methods
insider --show-methods

# Recommended
insider -file main.py -to obfuscated_main.py
```

Python API Usage

```python
from insider import Obfuscator

# Create obfuscator instance
obfuscator = Obfuscator()

# Obfuscate code string
code = """
def calculate_area(radius):
    return 3.14159 * radius ** 2
"""

obfuscated_code = obfuscator.obfuscate_code(code)

# Obfuscate file
obfuscator.obfuscate_file("input.py", "output.py")
```

📋 Available Obfuscation Methods

• rename_variables: Renames variables, functions, and classes to random names

• obfuscate_strings: Encodes all string literals with Base64

• obfuscate_imports: Converts import statements to dynamic imports

• remove_comments: Removes all comments and docstrings

• marshall_encode: Compiles and encodes code using marshal module

• zlib_compress: Compresses code using zlib compression

🏗 Project Structure

```
insider/
├── __init__.py
├── core/
│   ├── obfuscator.py          # Main Obfuscator class
│   ├── transformers.py        # Obfuscation transformers
│   └── utils.py              # Utility functions
├── encryption/
│   ├── marshall_encoder.py   # Marshall encoding
│   └── zlib_compressor.py    # Zlib compression
├── cli/
└── └── main.py               # CLI 
```

🔧 Advanced Usage

Custom Obfuscation Methods

```python
from insider import Obfuscator

obfuscator = Obfuscator()

# Use specific methods only
methods = ['rename_variables', 'marshall_encode']
obfuscated = obfuscator.obfuscate_code(code, methods=methods)

# Obfuscate with all methods
all_methods = [
    'rename_variables',
    'obfuscate_strings', 
    'obfuscate_imports',
    'remove_comments',
    'marshall_encode',
    'zlib_compress'
]
obfuscator.obfuscate_file("app.py", "protected_app.py", methods=all_methods)
```

Using Individual Components

```python
from insider.encryption import MarshallEncoder, ZlibCompressor

# Direct marshall encoding
encoded_code = MarshallEncoder.encode_code(source_code)
loader_code = MarshallEncoder.create_loader(encoded_code)

# Direct zlib compression
compressed = ZlibCompressor.compress_and_encode(source_code)
decompressor = ZlibCompressor.create_decompressor(compressed)
```

📊 Performance Notes

• Marshall Encoding: Provides strong protection but increases file size

• Zlib Compression: Can reduce file size while providing obfuscation

• Variable Renaming: Minimal performance impact, good readability reduction

• String Obfuscation: Small runtime overhead for string decoding

⚠️ Limitations

• Not 100% secure - determined reverse engineers can still analyze the code

• Some obfuscation methods may break certain Python features

• Always test obfuscated code thoroughly before deployment

• Not recommended for performance-critical applications

🤝 Contributing

We welcome contributions! Please feel free to submit pull requests, report bugs, or suggest new features.

1. Fork the repository
2. Create your feature branch (git checkout -b feature/AmazingFeature)
3. Commit your changes (git commit -m 'Add some AmazingFeature')
4. Push to the branch (git push origin feature/AmazingFeature)
5. Open a Pull Request

📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

🆘 Support

If you encounter any issues or have questions:

• Open an issue on GitHub

🔄 Version History

• 1.1.0: Added Marshall and Zlib support, improved CLI interface
•1.0.0: Initial release with basic obfuscation features

---

Note: This tool is designed for code protection and should be used responsibly. Always ensure you have the right to obfuscate and distribute the code you're working with.