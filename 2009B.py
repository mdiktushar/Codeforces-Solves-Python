t = int(input())

while t:
    
    arr = []
    n = int(input())

    for i in range(n):
        arr.append(input())


    for i in range(n-1, -1, -1):
        print(arr[i].find('#') + 1)

    t -= 1
