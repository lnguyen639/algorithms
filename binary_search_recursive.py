array = [1,4,6,8,23,45,67,90]  #has to be a sorted array

def binsearch(A,v,low,high):
    if low<=high:
        mid = (high+low)/2
        if A[mid] == v:
            return mid
        elif v > A[mid]:
            return binsearch(A,v,mid+1,high)
        else:
            return binsearch(A,v,low,mid-1)
    else:
        #eventually mid=low=high, then next loop low=mid+1 > high
        return "NIL"

print binsearch(array,23,0,len(array)-1)
