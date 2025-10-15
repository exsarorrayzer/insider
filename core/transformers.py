import re
import base64
import random
from insider.encryption.marshall_encoder import MarshallEncoder
from insider.encryption.zlib_compressor import ZlibCompressor
from insider.core.utils import CodeUtils

class VariableRenamer:
    
    def __init__(self):
        self.mapping = {}
        self.utils = CodeUtils()
    
    def transform(self, code: str) -> str:
        lines = code.split('\n')
        transformed_lines = []
        
        for line in lines:
            for old_name, new_name in self.mapping.items():
                line = re.sub(r'\b' + re.escape(old_name) + r'\b', new_name, line)
            transformed_lines.append(line)
        
        return '\n'.join(transformed_lines)
    
    def analyze_and_create_mapping(self, code: str):
        variables = self.utils.extract_variables(code)
        
        for var in variables:
            if not self.utils.is_protected_name(var):
                self.mapping[var] = self.utils.generate_random_name()

class StringObfuscator:
    
    @staticmethod
    def transform(code: str) -> str:
        
        def replace_string(match):
            string_content = match.group(1)
            encoded = base64.b64encode(string_content.encode()).decode()
            return f'__decode_str__("{encoded}")'
        
        code = re.sub(r'"([^"\\]*(\\.[^"\\]*)*)"', replace_string, code)
        code = re.sub(r"'([^'\\]*(\\.[^'\\]*)*)'", replace_string, code)
        
        decode_func = '''
def __decode_str__(s):
    import base64
    return base64.b64decode(s.encode()).decode()
'''
        return decode_func + '\n' + code

class ImportObfuscator:
    
    @staticmethod
    def transform(code: str) -> str:
        
        code = re.sub(
            r'^import\s+([a-zA-Z_][a-zA-Z0-9_]*(?:\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*)*)$',
            lambda m: f"{m.group(1).replace(' ', '')} = __import__('{m.group(1).split(',')[0]}')",
            code,
            flags=re.MULTILINE
        )
        
        code = re.sub(
            r'^from\s+([a-zA-Z_][a-zA-Z0-9_.]*)\s+import\s+([a-zA-Z_][a-zA-Z0-9_]*(?:\s*,\s*[a-zA-Z_][a-zA-Z0-9_]*)*)$',
            lambda m: f"{m.group(2).replace(' ', '')} = __import__('{m.group(1)}').{m.group(2).split(',')[0]}",
            code,
            flags=re.MULTILINE
        )
        
        return code

class CommentRemover:
    
    @staticmethod
    def transform(code: str) -> str:
        
        code = re.sub(r'#.*$', '', code, flags=re.MULTILINE)
        code = re.sub(r"'''.*?'''", '', code, flags=re.DOTALL)
        code = re.sub(r'""".*?"""', '', code, flags=re.DOTALL)
        
        return code

class MarshallTransformer:
    
    @staticmethod
    def transform(code: str) -> str:
        return MarshallEncoder.transform(code)

class ZlibTransformer:
    
    @staticmethod
    def transform(code: str) -> str:
        return ZlibCompressor.transform(code)