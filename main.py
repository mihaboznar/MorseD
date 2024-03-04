# define morse code mapping
morse_code_mapping = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', 'Č': '--.--', 'Ć': '-.-..', 'Đ': '-..--', 'Ž': '--..-', 'Š': '----', 
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': '/',  # Space
    '.': '.-.-.-',  # Period
    ',': '--..--',  # Comma
    '?': '..--..',  # Question mark
    "'": '.----.',  # Apostrophe
    '!': '-.-.--',  # Exclamation mark
    '/': '-..-.',   # Slash
    '(': '-.--.',   # Left parenthesis
    ')': '-.--.-',  # Right parenthesis
    '&': '.-...',   # Ampersand
    ':': '---...',  # Colon
    ';': '-.-.-.',  # Semicolon
    '=': '-...-',   # Equal sign
    '+': '.-.-.',   # Plus sign
    '-': '-....-',  # Hyphen
    '_': '..--.-',  # Underscore
    '"': '.-..-.',  # Quotation mark
    '$': '...-..-', # Dollar sign
    '@': '.--.-.'   # At symbol
}

# define function that loops over the entered uppercase string
def encode(text):
    morse_encoded = ""
    previous_char = None                    # store the previous character to check for consecutive spaces
    for char in text.upper().strip():       # using .strip() to remove spaces at the beginning and at the end of the string
        if char == ' ':
            # if the current character is a space and the previous character was also a space, skip adding it to the morse code
            # only adds "/" for the first space
            if previous_char == ' ':
                continue
            else:
                morse_encoded += '/'  # Add a single "/" to represent a space
        elif char in morse_code_mapping:
            morse_encoded += morse_code_mapping[char] + " "
        else:
            morse_encoded += " "
        previous_char = char  # update the previous character
    return morse_encoded


# define user input
user_string = input("Enter the string you want to encode:\n")

# call the function and output result
print(encode(user_string))