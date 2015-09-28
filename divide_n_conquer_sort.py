#Left = [2,6,9,18]
#Right = [1,3,5,9,24]
#Array = Left + Right
Array = [2,6,9,18,1,3,5,9,24]

def merge(A,p,q,r):
    n1 = q-p+1
    n2 = r-(q+1)+1
    for i in range(n1-1):
        Left[i] = Array[p+i]
    for j in range(n2-1):
        Right[j] = Array[q+1+j]
    Left.append('NOP')
    Right.append('NOP')

    i = 0
    j = 0
    for k in range(p,r):
        if Left[i] <= Right[j]:
            Array[k] = Left[i]
            i = i+1
        else:
            Array[k] = Right[j]
            j = j+1
    print Array

def merge_sort(A,p=None,r=None):
    if p<r:
        #round down
        q = (p+r)/2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

merge_sort(Array,0,8)
