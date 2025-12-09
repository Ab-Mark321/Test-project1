def invert_dictionary():
    grades = {"John": "A", "Mark": "B", "Moses": "C"}
    
    swap = {}
    for key, value in grades.items():
        if value not in swap:
            swap[value] = []
        swap[value].append(key)
    
    print(swap)

def main():
    invert_dictionary()


main()