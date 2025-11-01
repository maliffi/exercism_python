def is_armstrong_number(number):
    if number == 0:
        return True
    num_as_string = str(number)
    num_digits = len(num_as_string)
    if num_digits == 1:
        return True
    total = 0
    for x in num_as_string:
        print(f'x:{int(x)}, len:{num_digits}, x^len:{pow(int(x),num_digits)}')
        total += pow(int(x), num_digits)
    return total == number
