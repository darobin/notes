
S = { -4, -2, 1, 2, 5, 0 }
print [(i, j, k) for i in S for j in S for k in S if i + j + k == 0 and not(i == j and j == k)][0]
