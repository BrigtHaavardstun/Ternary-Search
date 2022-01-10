def TernarySearchContinusFunc(left,right, f, tolerance):
   # As long as our tolerance is not forfilled, we continue to search.
    while right-left > tolerance:
    
        # We divid our search span into three segments.
        left_third=left + (right-left)/3
        right_third=right -(right-left)/3

        """ 
        if the left_third point is lower then right_thirdpoint,
        we know there can not be a decrease 
        in value between right and right_third.
        Using similar arguments we get new bounds on all three cases.
        """
        if f(left_third)<f(right_third):
            right=right_third
        elif f(left_third)>f(right_third):
            left = left_third
        else:
            left  = left_third
            right = right_third

    return (left+right)/2
import math
def convexFunc(val):
    return (val)**2 - 3*val + 70


def findStartLefAndRight(f):
    # Many functions we are working with don't give us a segment containing the global minimum. 
    # To Find this efficently we "binary search" for starting (left) and ending (right) points.


    # When we are looking for a left value we are seaching for a point, such that 
    # at least one value to the right is smaller, with respect to f. If we find such,
    # a point we know the global minimum is to the right.
    # 'prev' creates this witness, as left only gets more negative 
    # (moving to the left on the number line).
    left = -1
    prev = left
    while(f(left)<=f(prev)):
        prev = left
        left *=2
    
    # When we are looking for a right value we are seaching for a point, such that 
    # at least one value to the left is smaller, with respect to f. If we find such,
    # a point we know the global minimum is to the left.
    # 'prev' creates this witness, as right only gets more positive
    # (moving to the right on the number line).
    right = 1
    prev = right
    while(f(right)<=f(prev)):
        prev = right
        right *= 2
    return left,right

if __name__ == "__main__":
    left,right = findStartLefAndRight(convexFunc)
    tolerance = 10**(-7)
    ans = TernarySearchContinusFunc(left,right,convexFunc, tolerance)
    print(ans, convexFunc(ans))
