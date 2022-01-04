from TernarySearchFinite import TernarySearchFinite

def BruteForce(A):
    minVal = float("inf")
    for e in A:
        minVal = min(e,minVal)
    return minVal

import random

n = 10**8
maxVal = n*10
TSTime = []
BSTime = []
for i in range(1):
    print("generating numbers...")
    A1 = [i for i in range(n,-n,-1) if random.randint(0,4) != 4]
    A2 = [i for i in range(-n,n) if random.randint(0,4) != 4]
    A = A1 + A2
    B = []
    prev = None
    for e in A:
        if e != prev:
            B.append(e)
            prev = e
    A = B
    if n < 100:
        print(A)

    import time
    print("Solving using Ternary Search...")
    t1 = time.time()
    ans1 = TernarySearchFinite(A)
    t2 = time.time()
    print("Solving using  BruteForce...")
    t3 = time.time()
    ans2 = BruteForce(A)
    t4 = time.time()
    TSTime.append(t2-t1)
    BSTime.append(t4-t3)
    if ans1 != ans2:
        print("Ans1: " + str(ans1))
        print("Ans2: " + str(ans2))
        print(A)
        raise Exception("Ternary Search and Bruteforce disagree on what the solution is")

TSavg = sum(TSTime)/len(TSTime)
BSavg = sum(BSTime)/len(BSTime)
print(f"avgtime diff: ")
print(f"TSavg: {TSavg}")
print(f"BSavg: {BSavg}")
print(f"BSavg/TSavg = {BSavg/TSavg}")