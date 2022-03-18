sum_n = 0
n = int(input())

nums = input()
num_arr = nums.split()

for i in range(n - 1):
    sum_n += int(num_arr[i])

real_sum = (n*(n+1))/2
print(int(real_sum - sum_n))


