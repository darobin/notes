
dlist = [
    { "Bilbo": "Ian", "Frodo": "Elijah" }
,   { "Bilbo": "Martin", "Thorin": "Richard" }
]
k = "Frodo"

print [x[k]  if k in x else "NOT PRESENT" for x in dlist]
