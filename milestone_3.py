while True:
    guess = input("Enter a letter: ")
    
    if len(guess) == 1:
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        
secret_word = "apple"

if guess in secret_word:
    print(f"Good guess! \033[1m{guess}\033[0m is in the word.")
else:
    print(f"Sorry, {guess} is not in the word. Try again.")