import sys

def dumps(code):
    bytecode = []
    key = 91700001
    
    for char in code:
        encoded_char = (ord(char) + key) % 256
        bytecode.append(encoded_char)
    
    return bytes(bytecode)

def loads(encoded_code):
    key = 91700001
    decoded_code = ''.join(chr((byte - key) % 256) for byte in encoded_code)
    s = compile(decoded_code, '<string>', 'exec')
    sys.settrace(None)
    return s
