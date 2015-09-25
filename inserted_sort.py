
array = [1,5,6,2,99,45,63,17,68,4]
array = [134,23,63,234,435,1,34,34,67]

print array
for j in range(1,len(array)):
    key = array[j]
    i = j-1
    while key < array[i] and i>=0:
        array[i+1] = array[i]
        i = i-1
    array[i+1] = key

print array

