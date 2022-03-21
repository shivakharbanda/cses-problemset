n = input()
n = int(n)

total = 1
m = (10**9)+7

for i in range(n):
    total = 2*total
    total = total % m
    print("total:", total)    
print(total)