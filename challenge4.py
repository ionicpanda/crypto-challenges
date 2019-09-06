# Detecting Single Byte XOR 
import re
from challenge3-2 import solve_single_xor

def detect_single_xor(lines):
    res = []
    for line in lines:
        line = bytearray(re.sub('[\n]','', line).decode('hex'))
        res.append(solve_single_xor(line))
    return(max(res, key=lambda x: x[0]))

def main():
    with open('file.txt', 'r') as f:
        lines=f.readlines()
    print detect_single_xor(lines)

if __name__ == "__main__":
    main()
