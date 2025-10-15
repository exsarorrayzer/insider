import os
from typing import List, Optional
from insider.core.transformers import (
    VariableRenamer, 
    StringObfuscator, 
    ImportObfuscator, 
    CommentRemover,
    MarshallTransformer,
    ZlibTransformer
)

class Obfuscator:
    
    def __init__(self):
        self.transformers = {
            'rename_variables': VariableRenamer(),
            'obfuscate_strings': StringObfuscator(),
            'obfuscate_imports': ImportObfuscator(),
            'remove_comments': CommentRemover(),
            'marshall_encode': MarshallTransformer(),
            'zlib_compress': ZlibTransformer()
        }
    
    def obfuscate_code(self, code: str, methods: Optional[List[str]] = None) -> str:
        
        if methods is None:
            methods = ['rename_variables', 'obfuscate_strings', 'remove_comments']
        
        obfuscated_code = code
        
        if 'rename_variables' in methods:
            self.transformers['rename_variables'].analyze_and_create_mapping(code)
        
        regular_methods = [m for m in methods if m not in ['marshall_encode', 'zlib_compress']]
        special_methods = [m for m in methods if m in ['marshall_encode', 'zlib_compress']]
        
        for method in regular_methods:
            if method in self.transformers:
                obfuscated_code = self.transformers[method].transform(obfuscated_code)
        
        for method in special_methods:
            if method in self.transformers:
                obfuscated_code = self.transformers[method].transform(obfuscated_code)
        
        return obfuscated_code
    
    def obfuscate_file(self, input_file: str, output_file: str, methods: Optional[List[str]] = None):
        
        if not os.path.exists(input_file):
            raise FileNotFoundError(f"Input file not found: {input_file}")
        
        with open(input_file, 'r', encoding='utf-8') as f:
            code = f.read()
        
        obfuscated_code = self.obfuscate_code(code, methods)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(obfuscated_code)
        
        print(f"Obfuscated: {input_file} -> {output_file}")
        
        original_size = len(code)
        obfuscated_size = len(obfuscated_code)
        
        print(f"Original size: {original_size} bytes")
        print(f"Obfuscated size: {obfuscated_size} bytes")
        print(f"Size ratio: {obfuscated_size/original_size:.2%}")