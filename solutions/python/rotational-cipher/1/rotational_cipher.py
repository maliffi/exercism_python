ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def rotate(text, key):
    text_lower = text.lower()
    result = ""
    for i, x in enumerate(text_lower):
        print(f"searching {x} into ALPHABET..")
        try:
            index = ALPHABET.index(x)
            print(f"{x} into ALPHABET={index}")
            shift = (index+key) %len(ALPHABET)
            print(f"shift:{shift}")
            c = ALPHABET[shift]
            if text[i].isupper():
                c = c.upper()
        except ValueError as e:
            c = text[i]
        result += c
        print(f"result:{result}")
    return result
