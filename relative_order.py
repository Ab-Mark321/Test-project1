def order(n):
    n=int(n)
    new_array=[]

    print(f"enter {n} number/s.")
    for num in range(1,n+1):
        elements=input("\n")
        new_array.append(elements)
    new_array.sort()

    zeroes=new_array.count('0')

    while '0' in new_array:
        new_array.remove('0')

    for _ in range(zeroes):
        new_array.append('0')
        
    print(new_array)      

def main():
        print("\n"+"="*20)
        print("NUMBER SORTER\n")
        print("\n"+"="*20)
        while True:
            test=input("Enter the number of elements you want your array to have.\n")
        
            try :
                if int(test)<=0:
                    print("please enter a positive number!")
                else:
                    order(test)
                    break
            except ValueError:
                print('please enter a number!\n')

main()