def number_spiral(x, y):
    mx = max(x, y)
    mx_sq = mx*mx

    if x == 1 and y == 1:
        
        return 1

    elif mx % 2 == 0:
        a = mx
        b = mx
        center = mx_sq - (mx - 1)
        
        if b == y:
            sub = a - x
            ans = center - sub
            return ans
        
        elif a == x:
            sub = b - y
            ans = center + sub
            return ans

    else:
        a = mx
        b  = mx
        center = mx_sq - (mx - 1)

        if a == x:
            sub = b - y
            ans = center - sub
            return ans
        
        elif b == y:
            sub = a - x
            ans = center + sub
            return ans


n = int(input())

while n >0:
    l = input()
    x, y = l.split(" ")
    x, y = int(x), int(y)

    print(number_spiral(x, y))
    n -= 1