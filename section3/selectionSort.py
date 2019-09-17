n = int(input())
a = list(map(int, input().split()))

def selectionSort(a, n):
    for i in range(n):
        minj = i
        for j in range(i, n):
            if a[j] < a[minj]:
                minj = j
        a[i], a[minj] = a[minj], a[i]

selectionSort(a, n)
print(a)

