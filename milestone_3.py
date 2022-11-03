secret_word = "apple"

def check_guess(letter):
    if letter.lower() in secret_word:
        print(f"Good guess! {letter.lower()} is in the word.")
    else:
        print(f"Sorry, {letter.lower()} is not in the word. Try again.")
    
        
def ask_for_input():
    while True:
        guess = input("Enter a letter: ")
        
        if len(guess) == 1:
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
            
    check_guess(guess)
            
ask_for_input()        