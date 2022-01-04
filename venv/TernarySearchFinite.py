def TernarySearch(A):
    # Span containg the global minimum
    h = len(A)  # exslusive upperbound
    l = 0       # inclusive lowerbound
    while l +1 <h:
        m = (l+h)//2


        v = A[m]
        vP = float("inf")
        if m+1 < len(A):
            vP = A[m+1] # v pluss 1
        vM = float("inf")
        if m-1 >= 0:
            vM = A[m-1] # v minus 1

        if v < vP and v < vM:
            return v
        
        elif vP < v < vM:
            l = m+1
        elif vM < v <vP:
            h = m # exslusive upperbound

        else:
            raise Exception("List non convex.")
    return A[l]
