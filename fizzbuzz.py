def fizzbuzz(n):
    lists=[]
    for num in range(1,n+1):
        if num%3==0 and num%5==0:
            lists.append("Fizzbuzz")
        elif num%3== 0:
            lists.append("Fizz")
        elif num%5==0:
            lists.append("Buzz")
        else:
            lists.append(num)
    return lists

def main():
    print("\n"+"="*20)
    print('FIZZBUZZ\n')
    print("\n"+"="*20)
    while True:
        number=input("enter any number(quit to return)\n")
        if number.lower()=="quit":
            print("goodbye")
            break
        try:
            number=int(number)
            if number<0:
                print("please enter a positive number!")
            else:
                output= fizzbuzz(number)
                print(output)
        except ValueError:
            print("please enter a number")
main()