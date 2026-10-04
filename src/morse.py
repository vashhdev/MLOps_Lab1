MORSE_CODE = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.",
    "G": "--.", "H": "....", "I": "..", "J": ".---", "K": "-.-", "L": ".-..",
    "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
    "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-",
    "Y": "-.--", "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
}

REVERSE_MORSE_CODE = {code: char for char, code in MORSE_CODE.items()}


def encode(text):
    """
    Encodes plain text into Morse code.
    Letters are separated by a single space, words by " / ".
    Args:
        text (str): Text containing letters, digits and spaces.
    Returns:
        str: Morse code representation of the text.
    Raises:
        ValueError: If text is not a string or has unsupported characters.
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")

    encoded_words = []
    for word in text.upper().split():
        letters = []
        for char in word:
            if char not in MORSE_CODE:
                raise ValueError(f"Unsupported character: {char}")
            letters.append(MORSE_CODE[char])
        encoded_words.append(" ".join(letters))
    return " / ".join(encoded_words)


def decode(code):
    """
    Decodes Morse code back into plain text.
    Args:
        code (str): Morse code, letters separated by spaces, words by " / ".
    Returns:
        str: Decoded uppercase text.
    Raises:
        ValueError: If code is not a string or contains an invalid symbol.
    """
    if not isinstance(code, str):
        raise ValueError("Input must be a string.")

    decoded_words = []
    for word in code.split("/"):
        letters = []
        for symbol in word.split():
            if symbol not in REVERSE_MORSE_CODE:
                raise ValueError(f"Invalid Morse symbol: {symbol}")
            letters.append(REVERSE_MORSE_CODE[symbol])
        if letters:
            decoded_words.append("".join(letters))
    return " ".join(decoded_words)


def count_signals(code):
    """
    Counts dots and dashes in a Morse code string.
    Args:
        code (str): Morse code string.
    Returns:
        tuple: (number of dots, number of dashes).
    Raises:
        ValueError: If code is not a string.
    """
    if not isinstance(code, str):
        raise ValueError("Input must be a string.")
    return code.count("."), code.count("-")


def add_morse(x, y):
    """
    Morse calculator: adds two numbers written in Morse code.
    Args:
        x (str): First number in Morse code (e.g. ".---- -----" for 10).
        y (str): Second number in Morse code.
    Returns:
        str: Sum of x and y, encoded in Morse code.
    Raises:
        ValueError: If x or y does not decode to a non-negative integer.
    """
    a = decode(x).replace(" ", "")
    b = decode(y).replace(" ", "")
    if not (a.isdigit() and b.isdigit()):
        raise ValueError("Both inputs must be numbers in Morse code.")
    return encode(str(int(a) + int(b)))


# print(encode("SOS"))                # ... --- ...
# print(decode("... --- ..."))        # SOS
# print(add_morse("..---", "...--"))  # .....  (2 + 3 = 5)
