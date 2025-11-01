def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if int(number) != number or number <=0:
        raise ValueError("Classification is only possible for positive integers.")
    divisors = get_divisors(number)
    if sum(divisors) == number and number not in divisors:
        return "perfect"
    if sum(divisors) > number:
        return "abundant"
    return "deficient"

def get_divisors(n) :
    divisors=[]
    for i in range(1,n) :
        if (n % i == 0) :
            divisors.append(i)     
    print(f"divisors of {n}: {divisors}")
    return divisors # return sum
    
