new_array=[1,2,6,0,45,0,34]

def order():
    zeroes=new_array.count(0)

    while 0 in new_array:
        new_array.remove(0)
    for _ in range(zeroes):
        new_array.append(0)
    print(new_array)      

def main():
        print("\n"+"="*20)
        print("NUMBER SORTER\n")
        print("\n"+"="*20)
        order()

main()
