a = []
n = 0
def binarySearch(key):
    left = 0
    right = n
    while left < right:
        mid = (left + right) // 2
        if key == a[mid]:
            return 1
        if key > a[mid]:
            left = mid + 1
        elif key < a[mid]:
            right = mid

    return 0


def main():
    global n, a
    n = int(input())
    a = list(map(int, input().split()))
    q = int(input())
    t = list(map(int, input().split()))
    sum = 0

    for i in t:
        if binarySearch(i):
            sum += 1

    print(sum)

if __name__ == '__main__':
    main()
