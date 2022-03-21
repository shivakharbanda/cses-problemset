#import time
#start_time = time.time()

""" this is a slower version"""

def sum_of_all_n_numbers(n):
    sumer = (n*(n+1))/2
    return int(sumer)

def can_or_cant(sum_of_n_nums):
    
    if sum_of_n_nums % 2 == 0:
        return "true"
    else:
        return "false"
        
def two_sets(n):
    summ = sum_of_all_n_numbers(n)
    can_we = can_or_cant(summ)

    if can_we == "true":
        arr = list(range(1, n+1, 1))

        arr1 = []
        arr2 = []
        z = 0
        if len(arr) % 2 != 0:
            max_element = max(arr)
            arr1.append(max_element)
            arr.remove(max_element)
            z = 1

        while len(arr) >0:
            A = max(arr)
            B = min(arr)
            #print("A:", A, "B:", B)
            if A != B:
                #print(arr)
                arr.remove(A)
                arr.remove(B)
            else:
                arr.remove(A)
            
            
            if z == 0:
                if A != B:
                    arr1.append(A)
                    arr1.append(B)
                else:
                    arr1.append(A)
                z = 1
            else:
                if A != B:    
                    arr2.append(A)
                    arr2.append(B)
                else:
                    arr2.append(B)
                z = 0

            
        print("YES")
        
        if len(arr1) > len(arr2):
            print(len(arr1))
            s1= ' '.join([str(elem) for elem in arr1])
            print(s1)
            print(len(arr2))
            s2 = ' '.join([str(elem) for elem in arr2])
            print(s2)
        else:
            print(len(arr2))
            s1= ' '.join(map(str, arr2))
            print(s1)
            print(len(arr1))
            s2 = ' '.join(map(str, arr1))
            print(s2)
            
    else:
        print("NO")

n = input()
n = int(n)
two_sets(n)

#print("--- %s seconds ---" % (time.time() - start_time))