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

TOLERANCE = {
    "grey": 0.05,
    "violet": 0.1,
    "blue": 0.25,
    "green": 0.5,
    "brown": 1,
    "red": 2,
    "gold": 5,
    "silver": 10
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
    end = 1
    if len(colors) == 5:
        end = 2
    result = ""
    if len(colors) == 1 and colors[0] == "black":
        return 0
    for i, color in enumerate(colors):
        if i >end:
            break
        result+= str(COLORS[color])
    return int(result)

def end_zeros(num):
    if num == "0":
        return 0
    return len(str(num)) - len(str(num).rstrip("0"))

def make_equivalence(value_ohms):
    print(f"make_equivalence of:{value_ohms}")
    for i in range(9, 1, -3):
        print(f"i:{i}")

        print(f"value_ohms >= pow(10, {i})?: {int(value_ohms) >= pow(10, i)}")
        if int(value_ohms) >= pow(10, i):
            value_after_equivalence = str(int(value_ohms)/pow(10, i))
            if value_after_equivalence.endswith(".0"):
                value_after_equivalence = value_after_equivalence.replace(".0", "")
            return value_after_equivalence+ " " + unit_prefix[i]+"ohms"
    return value_ohms + " ohms"
            
def get_multiplier_index(colors):
    if len(colors) == 5:
        return 3
    return 2

def add_zeros(value, colors):
    value= value.strip()
    if len(colors) == 1:
        print(f"no zero to add for value:{value}, colors:{colors}")
        return value
    multiplier_index = get_multiplier_index(colors)
    how_many_zero_add = COLORS[colors[multiplier_index]]
    print(f"value before ljust:{value}, color:{colors[multiplier_index]}, how_many_zero_add:{how_many_zero_add}")
    length= len(value)+how_many_zero_add
    print(f"length:{length}")
    result= value.ljust(length, '0')
    print(f"value after ljust:{result}")
    return result
    
def label(colors):
    value = get_value(colors)
    print(f"got value:{value}")
    result = str(value)
    result = add_zeros(result, colors)
    return make_equivalence(result)

def resistor_label(colors):
    lab = label(colors)
    print(f"before tolerance:{lab}")
    if len(colors) == 1 and colors[0] == "black":
        return lab
    color = colors[-1]
    return lab + " ±"+ str(TOLERANCE[color]) + "%"
