numbers=[2,4,8,6,0,54,7,4,9]
def target_finder(target):
    i=0
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[j]+numbers[i]==target:
                print(f"Output: {i, j}")
                print(f"Explanation: Because {numbers[i]} + {numbers[j]} == {target}.")
                return []
      


def main():
    print("\n"+"="*20)
    print("Target Number Finder")
    print("\n"+"="*20)
    target= 16
    target_finder(target)


main()
        