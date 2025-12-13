def count_word_frequency():
    sentence = input("Enter a sentence: ").strip()
    words = sentence.split()
     y = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    print(frequency)

def main():
    count_word_frequency()


main()