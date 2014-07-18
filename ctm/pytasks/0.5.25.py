
# works for bases <=10
base = 5
digits = set(range(base))

print {int(str(x)+str(y)+str(z), base): [x, y, z] for x in digits for y in digits for z in digits}

