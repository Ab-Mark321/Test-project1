def simple_logger():
    with open("log.txt", "a") as file:
        file.write("User logged in\n")
    

    print("Full Log History:")
    print("=" * 30)
    try:
        with open("log.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Log file created - this is the first entry.")


simple_logger()      