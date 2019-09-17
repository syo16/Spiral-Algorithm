def isStable(i, o):
    for j in range(len(i)):
        for k in range(j+1, len(i)):
            for a in range(len(i)):
                for b in range(a+1, len(i)):
                    if i[j][1] == i[k][1] and i[j] == o[b] and i[k] == o[a]:
                        return False
    return True



def BubbleSort(c, n):
    for i in range(n):
        for j in reversed(range(i+1, n)):
            if c[j][1] < c[j-1][1]:
                c[j], c[j-1] = c[j-1], c[j]

def SelectionSort(c, n):
    for i in range(n):
        mini = i
        for j in range(i+1, n):
            if c[j-1][1] > c[j][1]:
                mini = j
        c[i], c[mini] = c[mini], c[i]

c1 = ['H4', 'C9', 'S4', 'D2', 'C3']
c2 = c1.copy()

BubbleSort(c1, 5)
SelectionSort(c2,5)

print(c1)
print('Stable')

print(c2)

if isStable(c1, c2):
    print('Stable')
else:
    print('Not Stable')
