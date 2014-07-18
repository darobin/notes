
id2salary = { 0: 1000.0, 3: 990, 1: 1200.50 }
names = ["Larry", "Curly", "", "Moe"]

print {x: id2salary[i] for (x, i) in zip(names, range(len(names))) if i in id2salary}

