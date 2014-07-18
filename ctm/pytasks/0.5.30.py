
def dict2list(dct, keylist): return [dct[x] for x in keylist]

print dict2list({"a":"A", "b":"B", "c":"C"}, ["b", "c", "a"])

