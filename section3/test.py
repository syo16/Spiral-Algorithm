def selectionSort(a, n):
    for i in range(n):
        minv = (i, a[i])
        for j in range(i+1, n):
            if a[j] < minv[1]:
                minv = (j, a[j])
        a[i], a[minv[0]] = a[minv[0]], a[i]
    print(a)


selectionSort([5, 6, 4, 2, 1, 3], 6)
