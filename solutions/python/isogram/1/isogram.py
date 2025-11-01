ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def is_isogram(string):
    string = string.lower()
    present_chars = []
    for x in string:
        print(f"string:{string}, present_chars:{present_chars}")
        if x in present_chars:
            return False
        else:
            if x in ALPHABET:
                present_chars.append(x)
    return True
