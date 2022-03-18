size = input()
arr = input().split()

maximum = 0
moves = 0

for i in range(len(arr)):
    x = int(arr[i])

    maximum = max(x, maximum)

    moves = moves + (maximum - x)

print(moves)