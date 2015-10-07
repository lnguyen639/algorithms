Array = [4,2,19,1,7,3,15,14]

def merge(A,start,mid,end):
    Left=A[start:mid+1]+ [float("inf")] #slicing doesn't include the last element
    Right=A[mid+1:end+1] + [float("inf")] #also need the last element to be infinity for the sort to work

    li = 0  #left index
    ri = 0  #right index
    for k in range(start,end+1): #range also doesn't include last element
        if Left[li] <= Right[ri]:
            Array[k] = Left[li]
            li = li+1
        else:
            Array[k] = Right[ri]
            ri = ri+1

    print Array

def merge_sort(A,start=None,end=None):
    if start<end:
        #round down
        mid = (start+end)/2
        merge_sort(A,start,mid)
        merge_sort(A,mid+1,end)
        merge(A,start,mid,end)

merge_sort(Array,0,7)
