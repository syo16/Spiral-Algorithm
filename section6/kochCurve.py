import collections
import math

Point = collections.namedtuple('Point', ['x', 'y'])

def koch(n, a, b):
    if n == 0:
        return

    th = math.pi * 60.0 / 180.0

    sx = (2.0 * a.x + 1.0 * b.x) / 3.0
    sy = (2.0 * a.y + 1.0 * b.y) / 3.0
    s = Point._make([sx, sy])
    tx = (1.0 * a.x + 2.0 * b.x) / 3.0
    ty = (1.0 * a.y + 2.0 * b.y) / 3.0
    t = Point._make([tx, ty])
    ux = (t.x - s.x) * math.cos(th) - (t.y - s.y) * math.sin(th) + s.x
    uy = (t.x - s.x) * math.sin(th) + (t.y - s.y) * math.cos(th) + s.y
    u = Point._make([ux, uy])

    koch(n-1, a, s)
    print('{:.8f} {:.8f}'.format(s.x, s.y))
    koch(n-1, s, u)
    print('{:.8f} {:.8f}'.format(u.x, u.y))
    koch(n-1, u, t)
    print('{:.8f} {:.8f}'.format(t.x, t.y))
    koch(n-1, t, b)




def main():
    a = Point(0, 0)
    b = Point(100, 0)
    n = 2
    print('{:.8f} {:.8f}'.format(a.x, a.y))
    koch(n, a, b)
    print('{:.8f} {:.8f}'.format(b.x, b.y))




if __name__ == '__main__':
    main()
