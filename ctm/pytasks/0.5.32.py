
def all_3_digit_numbers(base):
    digits = set(range(base)) # works for bases <=10, otherwise type in set
    return {int(str(x)+str(y)+str(z), base) for x in digits for y in digits for z in digits}

print all_3_digit_numbers(3)

