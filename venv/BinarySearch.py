def BinarySeach(A, X):
    n = len(A)# The size of the list
    # We are trying to narrow down an interval where X might be.
    h = n #exlusive upper bound
    l = 0 #inclusive lower bound
    while ( l+1<h):
        m = (l+h)//2 # by looking at the middle of high and low we guarantee cutting 
                     # down the interval by half. 
        y = A[m]
        if X == y:
            return True # We found the value we are looking for
        elif y > X:
            # Since y > X, so is A[m+1], A[m+2], ..., A[n-1], as the list is sorted
            # We therfore conclude that the index holding X is located between
            # l and m-1
            h= m
        else: #y < X
            # Since y < X, so is A[m-1], A[m-2],..., A[0], as the list is sorted
            # We therfore conclude that the index holding X is located between
            # m and h
            l = m
        
    return A[l] == X

A =[-10,-4,-3,0,4,7,22]
print(BinarySeach(A, 0))# == True
print(BinarySeach(A, 3))# == False
