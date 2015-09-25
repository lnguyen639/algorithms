
array = [1,5,6,2,99,45,63,17,68,4]
num = 16

i = 'NIL'
for j in range(len(array)):
    key = array[j]
    if num == key:
        i = j

print i
