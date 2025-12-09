def create_sample_file(filename):
    """Create the numbers.txt file if it doesn't exist"""
    with open(filename, 'w') as f:
        f.write("10\n20\n30\nabc\n40")

def sum_valid_numbers(filename):
    """Read file and return sum of valid integers"""
    total = 0
    
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  
                    try:
                        total += int(line)
                    except ValueError:
                        pass
    except FileNotFoundError:
        create_sample_file(filename)
        return sum_valid_numbers(filename)
    
    return total

def main():
    filename = "numbers.txt"
    result = sum_valid_numbers(filename)
    print(f"Sum = {result}")


main()