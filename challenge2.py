'''XOR Combination of two equal-length buffers'''

import base64

def xor_strings(input1, input2):
    return bytes([b1 ^ b2 for b1, b2 in zip(input1, input2)])


def main():
    byte1 = bytes.fromhex('1c0111001f010100061a024b53535009181c')
    byte2 = bytes.fromhex('686974207468652062756c6c277320657965')

    print(xor_strings(byte1, byte2).hex())

if __name__ == "__main__":
    main()   