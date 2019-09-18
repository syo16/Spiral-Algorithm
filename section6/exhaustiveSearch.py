n = 5
a = [1, 5, 7, 10, 21]
def solve(i, m):
    if m == 0:
        return 1
    if i >= n:
        return 0
    res = solve(i+1, m) or solve(i+1, m-a[i])
    return res


q = 4
m = [2, 4, 17, 8]
for i in range(q):
    if solve(0, m[i]):
        print('yes')
    else:
        print('no')

