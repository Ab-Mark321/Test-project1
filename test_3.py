'''i have taken it a little further than the assigned :)'''
from datetime import datetime

def login_checker(Username, action="logged in"):
    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry= f'{timestamp} user {Username} {action}\n'
    with open("log.txt","a") as log_file:
        log_file.write(log_entry)

    print(f"Activity; {log_entry.strip()}")


def history():
    try:
        with open("log.txt", "r") as log_file:
            logs= log_file.readlines()
            if logs:
                print("="*20)
                print("full log history\n")
                print('\n'+"="*20)
                for log in logs:
                    print(log)
                    print('\n'+"="*20)
            else:
                print('log file is empty!')
    except FileNotFoundError:
        print("file log isn't found, it will be created shortly")

def main():
    print('\n'+"="*20)
    print("user activity log")
    print('\n'+"="*20)
    Username=input("please enter your user name(you can just press enter if you want to browse as a guest); \n")
    if not Username:
        Username="guest"
    login_checker(Username)


    while True:
        print("\nOptions:")
        print("1. Log another action")
        print("2. View log history")
        print("3. Exit")
        
        choice = input("Select option (1-3): ").strip()

        if choice=="1":
            action= input('enter an action \n')
            if action:
                login_checker(Username, action)
            else:
                print('action cannot be empty!')
        elif choice=="2":
            history()
        elif choice=="3":
            print('good bye')
            break
        else:
            print("invalid input please try again!")
        

main()




    