# rytercrypt/cli/main.py
import argparse
import sys
import os
from colorama import init, Fore, Style

init()

def show_banner():
    banner = f"""
{Fore.CYAN}
╔══════════════════════════════════════════════╗
║             {Fore.YELLOW}INSIDER OBFUSCATOR{Fore.CYAN}             ║
║          Advanced Python Code Protection     ║
║
╚══════════════════════════════════════════════╝
{Style.RESET_ALL}
"""
    print(banner)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from ..core.obfuscator import Obfuscator

def main():
    show_banner()
    
    parser = argparse.ArgumentParser(description='RyterCrypt - Python Code Obfuscation Tool')
    
    parser.add_argument('-file', '--input-file', required=True, 
                       help='Input file to obfuscate')
    parser.add_argument('-to', '--output-file', required=True,
                       help='Obfuscated output file')
    parser.add_argument('-methods', '--methods', nargs='+',
                       choices=['rename_variables', 'obfuscate_strings', 
                               'obfuscate_imports', 'remove_comments',
                               'marshall_encode', 'zlib_compress'],
                       default=['rename_variables', 'obfuscate_strings', 
                               'remove_comments'],
                       help='Obfuscation methods to use')
    
    parser.add_argument('--show-methods', action='store_true',
                       help='Show available methods')
    
    args = parser.parse_args()
    
    if args.show_methods:
        print(f"{Fore.GREEN}Available Obfuscation Methods:{Style.RESET_ALL}")
        print(f"  {Fore.YELLOW}rename_variables{Style.RESET_ALL}   - Rename variable names")
        print(f"  {Fore.YELLOW}obfuscate_strings{Style.RESET_ALL}  - Encrypt strings")
        print(f"  {Fore.YELLOW}obfuscate_imports{Style.RESET_ALL}  - Obfuscate imports")
        print(f"  {Fore.YELLOW}remove_comments{Style.RESET_ALL}    - Remove comments")
        print(f"  {Fore.YELLOW}marshall_encode{Style.RESET_ALL}    - Marshal code encoding")
        print(f"  {Fore.YELLOW}zlib_compress{Style.RESET_ALL}      - Zlib compression")
        return
    
    try:
        obfuscator = Obfuscator()
        obfuscator.obfuscate_file(args.input_file, args.output_file, args.methods)
        print(f"{Fore.GREEN}✅ Obfuscation completed successfully!{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}❌ Error: {e}{Style.RESET_ALL}")
        sys.exit(1)

if __name__ == '__main__':
    main()