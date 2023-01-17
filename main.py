char_to_code = {
    'A': ".-",
    'B': "-...",
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'H': '....',
    'I': '..',
    'K': '.---',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
}
code_to_char = {
    ".-": 'A',
    "-...": 'B',
    '-.-.': 'C',
    '-..': 'D',
    '.': 'E',
    '..-.': 'F',
    '....': 'H',
    '..': 'I',
    '.---': 'K',
    '.-..': 'L',
    '--': 'M',
    '-.': 'N',
    '---': 'O',
    '.--.': 'P',
    '--.-': 'Q',
    '.-.': 'R',
    '...': 'S',
    '-': 'T',
    '..-': 'U',
    '...-': 'V',
    '.--': 'W',
    '-..-': 'X',
    '-.--': 'Y',
    '--..': 'Z',
    '.----': '1',
    '..---': '2',
    '...--': '3',
    '....-': '4',
    '.....': '5',
    '-....': '6',
    '--...': '7',
    '---..': '8',
    '----.': '9',
    '-----': '0',
}

encode_decode = input("Do you want to Encode or Decode Morse Code: ").lower()
if encode_decode == "encode" or encode_decode == "e":
    code = input("Enter what you want to encode as Morse Code: ").upper()
    encoded_mc = ' '.join([char_to_code[letter] for letter in code])
    print(f"Your Encoded Morse Code is: {encoded_mc}")

elif encode_decode == "decode" or encode_decode == "d":
    code = input("Enter the Morse Code to decode: ")
    mc_list = code.split()
    decoded_mc = ''.join([code_to_char[code] for code in mc_list]).lower()
    print(f"Your Encoded Morse Code is: {decoded_mc}")

else:
    print("You did not enter a valid response.")
