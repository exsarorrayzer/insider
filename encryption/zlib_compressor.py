import zlib
import base64

class ZlibCompressor:
    
    @staticmethod
    def compress_and_encode(code: str) -> str:
        try:
            encoded_code = code.encode('utf-8')
            compressed = zlib.compress(encoded_code, level=9)
            encoded = base64.b64encode(compressed).decode('utf-8')
            return encoded
        except Exception as e:
            raise ValueError(f"Zlib compression failed: {e}")
    
    @staticmethod
    def create_decompressor(encoded_data: str) -> str:
        decompressor_code = f'''
import zlib
import base64

def __decompress_and_execute__():
    compressed_data = "{encoded_data}"
    try:
        compressed = base64.b64decode(compressed_data.encode('utf-8'))
        decompressed = zlib.decompress(compressed)
        code = decompressed.decode('utf-8')
        exec(code)
    except Exception as e:
        print(f"Decompression error: {{e}}")

__decompress_and_execute__()
'''
        return decompressor_code
    
    @staticmethod
    def transform(code: str) -> str:
        encoded = ZlibCompressor.compress_and_encode(code)
        return ZlibCompressor.create_decompressor(encoded)