Array = [4,2,19,1,7,3,15,14]

def merge(A,p,q,r):
    Left=A[p:q+1]+ [float("inf")] #slicing doesn't include the last element
    Right=A[q+1:r+1] + [float("inf")] #also need the last element to be infinity for the sort to work

    i = 0
    j = 0
    for k in range(p,r+1):
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

merge_sort(Array,0,7)
