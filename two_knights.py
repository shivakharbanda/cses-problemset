def total_combinations(n):
    n_sq = n*n
    combinations = (n_sq * (n_sq - 1))/2
    return int(combinations)

def invalid_combinations(n):
    invalid = 2*(2*((n-1)*(n-2)))
    return invalid

def two_knights(n):
    if n ==1:
        return 0 
    elif n == 2:
        return total_combinations(n)
    else:    
        total = total_combinations(n)
        invalid = invalid_combinations(n)
        return int(total - invalid)

n = int(input())

for i in range(1, n+1,1):
    print(two_knights(i))