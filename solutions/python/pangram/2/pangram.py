import string

ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def is_pangram(sentence):
    present_chars = []
    if len(sentence) <=0:
        return False
    sentence = sentence.lower()
    for x in ALPHABET:
        try:
            if sentence.index(x) >=0 and x not in present_chars:
                present_chars.append(x)
        except ValueError:
            print("do nothing")
        if len(present_chars) == len(ALPHABET):
            return True
    return False


def is_pangram_short(sentence):
    return all(char in sentence.lower() for char in string.ascii_lowercase)
            
        
