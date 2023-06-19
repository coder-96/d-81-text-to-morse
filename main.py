MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ',': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


def encrypt(text):
    encrypted = ""
    for n in text:
        if n == " ":
            encrypted += ""
        else:
            encrypted += MORSE_CODE_DICT[n]
            encrypted += " "
    return encrypted

def decrypt(text):
    decrypted = []
    if " " in text:
        text = text.split()
        for n in text:
            for x, y in MORSE_CODE_DICT.items():
                if y == n:
                    decrypted.append(x)
    else:
        for x, y in MORSE_CODE_DICT.items():
            if y == text:
                decrypted.append(x)
    decode = "".join(decrypted)
    return decode


question = input("Do you want to encode or decode, type (encode/decode): ").lower()
if question == "encode":
    encode_text = input("Please type your text: ").upper()
    print(f"Here's the Morse Code for your text: {encrypt(encode_text)}")
else:
    decode_text = input("Please type Morse Code, separate your each letter with a space: ").upper()
    print(f"Here's the text from your Morse Code: {decrypt(decode_text)}")
