COLORS = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9,
}

unit_prefix= {
    3: "kilo",
    4: "kilo",
    5: "kilo",
    6: "mega",
    7: "mega",
    8: "mega",
    9: "giga"
}

equivalence= {
    "": 0,
    "kilo": 3,
    "mega": 6,
    "giga": 9
}

def get_value(colors):
    result = ""
    for i, color in enumerate(colors):
        if i >1:
            break
        result+= str(COLORS[color])
    return int(result)

def end_zeros(num):
    return len(str(num)) - len(str(num).rstrip("0"))

def make_equivalence(value_ohms):
    print(f"make_equivalence of:{value_ohms}")
    amount_of_zeros = end_zeros(value_ohms)
    try:
        prefix = unit_prefix[amount_of_zeros]
    except KeyError as e:
        prefix = ""
    print(f"before equivalence:{value_ohms}, amount_of_zeros:{amount_of_zeros}, unit_prefix[amount_of_zeros]:{prefix}")
    zero_to_remove = equivalence[prefix]
    base = str(value_ohms)
    if zero_to_remove != 0:
        base =str(value_ohms)[0:-zero_to_remove]
    return base + " " + prefix + "ohms"
    # if str(value_ohms).endswith("000000000"):
    #     return value_ohms[0:-9]+" gigaohms"
    # if str(value_ohms).endswith("000000"):
    #     return value_ohms[0:-6]+" megaohms"
    # if str(value_ohms).endswith("000"):
    #     return value_ohms[0:-3]+" kiloohms"
    # return value_ohms+" ohms"
    
def label(colors):
    value = get_value(colors)
    result = str(value)
    how_many_zero_add = COLORS[colors[2]]
    print(f"value:{result}, color:{colors[2]}, how_many_zero_add:{how_many_zero_add}")
    result = result.ljust(len(result)+how_many_zero_add, '0')
    return make_equivalence(result)
