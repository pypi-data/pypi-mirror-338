import sys

def dumps(code):
    bytecode = []
    key = 917
    
    for char in code:
        encoded_char = (ord(char) + key) % 256
        bytecode.append(encoded_char)
    
    return bytes(bytecode)

def dec(encoded_code):
    key = 917
    decoded_code = ''.join(chr((byte - key) % 256) for byte in encoded_code)
    s = compile(decoded_code, '<string>', 'exec')
    return s
def start(encoded_code):    
    s = dec(encoded_code)
    sys.settrace(None)
    return exec(s)
