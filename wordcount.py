def word_counter(text):
    words = text.split() 
    
    num_words = len(words)
    return num_words

def main():
    
    user_input = input("Enter a sentence or paragraph: ")
    num_words = word_counter(user_input)
    print(f"Number of words: {num_words}")

if __name__ == "__main__":
    main()