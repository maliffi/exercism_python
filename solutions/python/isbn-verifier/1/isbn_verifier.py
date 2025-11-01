def is_valid(isbn):
    isbn = isbn.replace("-", "").strip().upper()
    print(f"isbn:{isbn}")
    check = 0
    if len(isbn) < 9 or len(isbn) >10:
        return False
    for i in reversed(range(10)):
        index = len(isbn)-i-1
        print(f"i:{i}, index:{index}")
        if isbn[index] == 'X' and index == 9:
            print(f"{isbn[index]} is X")
            num = 10
        elif not isbn[index].isdigit():
            print(f"{isbn[index]} is not a digit")
            return False
        else:
            print(f"{isbn[index]} is a digit")
            num = int(isbn[index])
        print(f"{num}*{i}")
        check = check + (num * (i+1))
    
    if check % 11 == 0:
        return True
    return False
