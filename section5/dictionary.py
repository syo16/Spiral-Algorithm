m = 1046527
nil = -1
l = 14

def getChar(ch):
    if ch == 'A':
        return 1
    elif ch == 'C':
        return 2
    elif ch == 'G':
        return 3
    elif ch == 'T':
        return 4
    else:
        return 0


def getKey(s):
    sum = 0
    p = 1
    for i in s:
        sum += p * getChar(i)
        p *= 5
    return sum

def h1(key):
    return key % m

def h2(key):
    return 1 + (key % (m-1))

def find(s):
    key = getKey(s)
    i = 0
    while True:
        h = (h1(key) + 1 * h2(key)) % m
        if ()

def insert(s):
    key = getKey(s)


def main():
    n = int(input())
    for i in range(n):
        c, s = list(map(str, input().split()))
        if c[0] == 'i':
            insert(s)
        else:
            if find(s):
                print('Yes')
            else:
                print('No')

if __name__ == '__main__':
    main()
