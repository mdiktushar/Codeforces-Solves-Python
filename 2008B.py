import math


t = int(input())

while t:
    n = int(input())
    s = input()
    sqrt = math.sqrt(n)

    if sqrt.is_integer():
        zero = s.count('0')
        one = s.count('1')

        if one <=4 and zero == 0:
            print("YES")
            t = t-1
            continue

        if zero > 0:
            zeroSqrt = math.sqrt(zero)
            if zeroSqrt.is_integer():
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        print("NO")
    
    t = t-1