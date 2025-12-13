def mySqrt(x: int) -> int:
    if x < 2:
        return x
    
    left, right = 0, x//2
    ans = 0
    
    while left <= right:
        mid = (left +  right - left) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            ans = mid
            left = mid + 1
        else:
         right = mid - 1
    
    return ans

def main():
    x = 8
    
    result = mySqrt(x)
    print(f"Floor square root of {x} is: {result}")


main()