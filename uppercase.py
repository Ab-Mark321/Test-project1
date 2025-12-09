def read_and_uppercase(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read().upper())
    except FileNotFoundError:
        print("File not found. Creating one...")
        with open(filename, 'w') as file:
            file.write("Hello World\nPython is fun")
    
        with open(filename, 'r') as file:
            print(file.read().upper())

def main():
    filename = "message.txt"
    read_and_uppercase(filename)


main()