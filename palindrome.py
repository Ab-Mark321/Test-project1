def palindrome(n):
    if n<0:
        print(False)
    str_n=str(n)
    reverse= str_n[::-1]
    if reverse==str_n:
        print(True)
    else:
        print(False)


def main():
    print("\n"+"="*20)
    print('Palindrome Checker')
    print("\n"+"="*20)
    number=345
    palindrome(number)

main()