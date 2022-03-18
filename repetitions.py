string = input()

size = len(string) - 1

count = 1
subsequence = 1

for i in range(size):
    #print('string[i]:', string[i], 'string[i + 1]:', string[i+ 1], 'count:', count)
    
    if string[i] != string[i+1]:
        if count > subsequence:
            subsequence = count
        count = 1

    else:
        count += 1

    #print('count:', count, 'subsequence:', subsequence)
#print("count:", count, "subsequence:", subsequence)
print(max(count, subsequence))


