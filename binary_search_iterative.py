#Run time is f(log2(n))
array = [1,4,6,8,23,45,67,90]  #has to be a sorted array

def binsearch(A,value,low,high):
    while low <= high:
        mid = (high+low)/2
        if value == A[mid]:
            return mid
        if value < A[mid]:
            high = mid -1
        else:
            low = mid + 1
    return "NIL"

print binsearch(array,90,0,len(array)-1)
