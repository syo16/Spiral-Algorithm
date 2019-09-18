def search(a, n, key):
    i = 0
    a.append(key)
    while a[i] != key:
        i += 1
    a.pop()
    return i != n


n = int(input())
a = list(map(int, input().split()))
q = int(input())
t = list(map(int, input().split()))

sum = 0
for i in t:
    if search(a, n, i):
        sum += 1

print(a)
print(sum)

