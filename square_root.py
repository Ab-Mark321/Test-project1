def mySqrt(x: int) -> int:
    if x < 2:
        return x
    
    low, high = 0, x
    ans = 0
    
    while low <= high:
        mid = low + (high - low) // 2
        square = mid * mid
        
        if square == x:
            return mid
        elif square < x:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    
    return ans

def main():
    x = 8
    result = mySqrt(x)
    print(f"Floor square root of {x} is: {result}")


main()