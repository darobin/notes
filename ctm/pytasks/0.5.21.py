
dlist = [
    { "James": "Sean", "director": "Terence" }
,   { "James": "Roger", "director": "Lewis" }
,   { "James": "Pierce", "director": "Roger" }
]
k = "James"

print [x[k] for x in dlist]
