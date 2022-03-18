string = input()
size = (len(string) - 1)

count = 0 
subsequence = 0

for i in range(size):
    if string[i] != string[i+1]:
        count += 1
    
    else:
        count +=1
        if count > subsequence:
            subsequence = count
            count = 0

print(subsequence)