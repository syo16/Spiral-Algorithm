n = int(input())
a = list(map(int, input().split()))

def bubbleSort(a, n):
    count = 0
    flag = 1
    while flag:
        flag = 0
        for j in reversed(range(1, n)):
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
                flag = 1
                count += 1
    print(count)

bubbleSort(a, n)
