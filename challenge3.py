'''XOR Combination of two equal-length buffers'''

import base64

#variable
b = bytes.fromhex('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

def xor_strings(input1, input2):
    return bytes([b1 ^ b2 for b1, b2 in zip(input1, input2)])

def xor_single_char(byte_input, char_val):
    byte_output = b''
    for byte in byte_input:
        byte_output += bytes([byte ^ char_val])
    return byte_output

def english_score(byte_input):
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in byte_input.lower()])

for i in range(256):
    xor_single_char(b, i)

def main():
    hex = ('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')
    b = bytes.fromhex(hex)
    potential = []
    for key_value in range(256):
        message = xor_single_char(b, key_value)
        score = english_score(message)
        data = {
            'message': message,
            'score': score,
            'key': key_value
        }
        potential.append(data)

    best_score = sorted(potential, key=lambda x: x['score'], reverse=True)[0]
    for item in best_score:
        print("{}: {}".format(item.title(), best_score[item]))

if __name__ == "__main__":
    main()   