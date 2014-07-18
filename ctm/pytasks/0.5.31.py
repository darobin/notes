
def list2dict(L, keylist): return {keylist[i]: L[i] for i in range(len(keylist))}

print list2dict(["A", "B", "C"], ["a", "b", "c"])

