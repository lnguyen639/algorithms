array = [1,4,6,8,23,45,67,90]  #has to be a sorted array
index = None

def binsearch(A,v,low,high):
    if low<=high:
        global index
        mid = (high+low)/2
        if A[mid] == v:
            index=mid
            return
        elif v > A[mid]:
            index="NIL"
            binsearch(A,v,mid+1,high)
        else:
            index="NIL"
            binsearch(A,v,low,mid-1)

binsearch(array,18,0,len(array)-1)
print index
