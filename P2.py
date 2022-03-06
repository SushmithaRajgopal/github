sample_list =[1,1,1,1,22,2,22,2,3,33,3333,3,33,3333,55,4,55,44,5,6,77,88]
occurrences = {}
for i in sample_list:
    if i in occurrences:
        occurrences[i] += 1
    else:
        occurrences[i] = 1

print(occurrences)

