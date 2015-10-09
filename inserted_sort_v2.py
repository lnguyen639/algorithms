#Run time is f(n^2)
#This is not recursive
#This tries to loops through array

Array = [3,41,52,26,38,57,9,49]
#Array = [1,3,4,45,49,32]

#Insert last item of array into the right position of a sorted array
def insertion(A,len):
    key = A[len-1]
    i = len-2 #2nd to last spot on array
    while key <= A[i] and i >= 0:
        A[i+1] = A[i]
        i = i -1
    A[i+1] = key

def isort(A):
    i = 2
    while i<(len(A)+1):
        insertion(A,i)
        i = i + 1

isort(Array)
print Array
