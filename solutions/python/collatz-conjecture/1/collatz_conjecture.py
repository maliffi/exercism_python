def steps(number):
    return inner_steps(number, 0)

def inner_steps(number, step_number):
    if number <=0:
        raise ValueError("Only positive integers are allowed")
    if number == 1:
        return step_number
    step_number+=1
    if is_even(number):
        number = number/2
    else:
        number = (number*3) + 1
    print(f'number:{number}, step:{step_number}')
    return inner_steps(number, step_number)


def is_even(num):
    return num % 2 == 0
