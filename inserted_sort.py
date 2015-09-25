
array = [1,5,6,2,99,45,63,17,68,4]

print array
for j in range(1,len(array)):
    key = array[j]
    i = j-1
    while key < array[i] and i>=0:
        array[i+1] = array[i]
        array[i] = key
        i = i-1

print array

