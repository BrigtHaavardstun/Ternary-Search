from TernarySearchContinus import TernarySearchContinusFunc

listOfHouses = []
def maxDistForAChild(endPosX):
    global listOfHouses
    return max([((house[0]-endPosX)**2+house[1]**2) for house in listOfHouses])

def main():
    global listOfHouses
    # use ternary search on a fun
    nrHouses = int(input())
    while nrHouses != 0:
        new_list_houses = []
        minX = float("inf")
        maxX = float("-inf")
        for _ in range(nrHouses):
            x,y = list(map(float, input().split()))
            if x < minX:
                minX = x
            if x > maxX:
                maxX = x
            new_list_houses.append((x,y))
        listOfHouses = new_list_houses
        opt_x = TernarySearchContinusFunc(minX, maxX, maxDistForAChild, 10**(-6))
        print(opt_x, maxDistForAChild(opt_x)**0.5, flush=True)
        input()
        nrHouses = int(input())



    

if __name__ == "__main__":
    main()