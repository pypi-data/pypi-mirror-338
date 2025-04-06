import subprocess

MORSE_CODE_DICT = {
    '.-': 'a', '-...': 'b', '-.-.': 'c', '-..': 'd', '.': 'e', '..-.': 'f',
    '--.': 'g', '....': 'h', '..': 'i', '.---': 'j', '-.-': 'k', '.-..': 'l',
    '--': 'm', '-.': 'n', '---': 'o', '.--.': 'p', '--.-': 'q', '.-.': 'r',
    '...': 's', '-': 't', '..-': 'u', '...-': 'v', '.--': 'w', '-..-': 'x', '-.--': 'y', '--..': 'z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '/': ' ', '.-.-.-': '.', '--..--': ',', '..--..': '?', '-.-.--': '!', '-..-.': '/', '.-..-.': '"',
    '-.--.': '(', '-.--.-': ')', '[': '[', ']': ']', '{': '{', '}': '}', '-...-': '='
}

def morse_to_text(morse_code):
    words = morse_code.strip().split(' / ')
    decoded_words = []
    for word in words:
        letters = word.split()
        decoded_word = ''.join(MORSE_CODE_DICT.get(letter.upper(), '?') for letter in letters)
        decoded_words.append(decoded_word)
    return ' '.join(decoded_words)

def text_to_morse(python_code):
    morse_code = []
    for char in python_code:
        if char == " ":
            morse_code.append("/")
        else:
            for key, value in MORSE_CODE_DICT.items():
                if value == char.lower():
                    morse_code.append(key)
                    break
    return " ".join(morse_code)

def execute_morse_code(morse_code):
    translated_code = morse_to_text(morse_code)
    try:
        output = subprocess.check_output(['python', '-c', translated_code], stderr=subprocess.STDOUT, text=True)
    except subprocess.CalledProcessError as e:
        output = e.output
    except Exception as e:
        output = str(e)
    print(output)
