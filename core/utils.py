import re
import random
import string
from typing import Set

class CodeUtils:
    
    @staticmethod
    def generate_random_name(length: int = 8) -> str:
        chars = string.ascii_letters + string.digits
        return '_' + ''.join(random.choice(chars) for _ in range(length))
    
    @staticmethod
    def extract_variables(code: str) -> Set[str]:
        patterns = [
            r'\b([a-zA-Z_][a-zA-Z0-9_]*)\s*=',
            r'def\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            r'class\s+([a-zA-Z_][a-zA-Z0-9_]*)',
            r'for\s+([a-zA-Z_][a-zA-Z0-9_]*)\s+in',
            r'with\s+([a-zA-Z_][a-zA-Z0-9_]*)'
        ]
        
        variables = set()
        for pattern in patterns:
            matches = re.findall(pattern, code)
            variables.update(matches)
        
        return variables
    
    @staticmethod
    def is_protected_name(name: str) -> bool:
        protected = {
            '__name__', '__main__', '__file__', '__doc__', '__package__',
            '__builtins__', '__all__', '__version__', '__author__',
            'self', 'cls', 'True', 'False', 'None'
        }
        return name in protected or name.startswith('__') and name.endswith('__')