#import time
#start_time = time.time()
""" this is a faster version"""
def sum_of_all_n_numbers(n):
    sumer = (n*(n+1))/2
    return int(sumer)

def can_or_cant(sum_of_n_nums):
    
    if sum_of_n_nums % 2 == 0:
        return "true"
    else:
        return "false"
        

def two_sets(n):
    arr1 = []
    arr2 = []

    arr1_sum = 0
    arr2_sum = 0

    summ = can_or_cant(sum_of_all_n_numbers(n))

    if summ == "true":

        for i in range(n,0, -1):
            #print("arr1_sum:", arr1_sum, "arr2_sum:", arr2_sum)
            if arr1_sum == arr2_sum or arr1_sum < arr2_sum:
                arr1.append(i)
                arr1_sum += i

            else:
                arr2.append(i)
                arr2_sum += i
            
            #print("arr1:", arr1, "arr2:", arr2)

        print("YES")
        if len(arr1) > len(arr2):
            print(len(arr1))
            print(' '.join(map(str, arr1)))
            print(len(arr2))
            print(' '.join(map(str, arr2)))
        else:
            print(len(arr2))
            print(' '.join(map(str, arr2)))
            print(len(arr1))
            print(' '.join(map(str, arr1)))
    else:
        print("NO")

n = input()
n = int(n)
#n = 26560
two_sets(n)

#print("--- %s seconds ---" % (time.time() - start_time))