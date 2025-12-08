# Simple version - exactly as described in your requirements
def simple_logger():
    # Write login message
    with open("log.txt", "a") as file:
        file.write("User logged in\n")
    
    # Read and print full history
    print("Full Log History:")
    print("=" * 30)
    try:
        with open("log.txt", "r") as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print("Log file created - this is the first entry.")

# Run the simple logger
if name == "main":
    simple_logger()      