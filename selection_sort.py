
array = [4,6,2,3,13,22,87,65]

for i in range(len(array)-1):
    smallest = i
    j = i+1
    while j < len(array):
        if array[j] < array[smallest]:
            smallest = j
        j = j + 1
    temp = array[i]
    array[i] = array [smallest]
    array[smallest] = temp

print array
