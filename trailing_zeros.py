import sys, math
#import time
#start_time = time.time()

def trailing_zeros(x):
    n = x
    if n < 0:
        return -1

    count = 0

    while n >=5:
        print("n:", n)
        n = n // 5
        count += n
        print("count:",  count)
    

    return count



    
    

x = int(input())

print(trailing_zeros(x))


#print("--- %s seconds ---" % (time.time() - start_time))


