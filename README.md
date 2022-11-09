# Python Hangman Project

A hangman game that allows user to guess what is the fruit that is randomly selected from a word_list. The word_list consist of the following fruits:

* Watermelon
* Honeydew
* Orange
* Mango
* Apple

## Milestone 1 
* Setup of GitHub repository to store project files.

## Milestone 2
* Created a list of fruits and assigning it with the name `word_list`.

    ```go
    word_list = ["Watermelon", "Honeydew", "Mango", "Apple", "Orange"]
    ```

* Import the random module to access the `random.choice()`. This method allow use to randomly select an element from the sequence that is passed it. The element is then assigned to a variable called `word`.
  
    ```go
     word = random.choice(word_list) 
    ```
* To get user input, the `input()` function is used. The input function also allows custom messages to be displayed when the function is called. Subsequently, the user input is then store in the variable named `guess` as a string.
  
    ```go
    guess = input("Guess the fruit : ")
    ```
* To check for the length of the user input, an `if` statement is used. If the length of the user input is equals to 1, "Good guess!" will be printed, else "Oops! Input is greater than 1" is printed. 
  
    ```go
    if len(guess) == 1:
        print("Good guess!")
    else:
        print("Oops! Input is greater than 1")
    ```
## Milestone 3
* By using a `while` loop with a `True` condition, this allows the loop to run indefinitely. In the while loop, the `input()` function is used to obtain the user input and store in a variable named `guess`. 
* An `if` statement is also used to validate the length of the user input. If the length of user input equals to 1, a break statement is used to break out of the while loop. Else, the message "Invalid number of letters. Please, enter a single alphabetical character." will be printed. 

    ```go
    while True:
        guess = input("Enter a letter: ")
        
        if len(guess) == 1:
            break
        else:
            print("Invalid number of letters. Please, enter a single alphabetical character.")
    ```
* Created a `check_guess(letter)` function. This function takes in a letter to check if the letter is in the secret word. If the letter is in the secret_word, "Good guess! {letter.lower()} is in the word." will be printed or else, "Sorry, {letter.lower()} is not in the word. Try again.".

    ```go
    def check_guess(letter):
    if letter.lower() in secret_word:
        print(f"Good guess! {letter.lower()} is in the word.")
    else:
        print(f"Sorry, {letter.lower()} is not in the word. Try again.")
    ```
* Created an `ask_for_input()` function. This function uses the `while` loop built early as well as the `check_guess(letter)` function.

    ```go
    def ask_for_input():
    while True:
        guess = input("Enter a letter: ")
        
        if len(guess) == 1:
            break
        else:
            print("Invalid number of letters. Please, enter a single alphabetical character.")
            
    check_guess(guess)
    ```
## Milestone 4
- Used OOP to build out the hangman class.
- Created check_guess method to determine if the user's guess is in the word.
- Replace blank underscore with corrently guessed letters
- Deduct lives if guess is incorrect

## Milestone 5
- Added play_game function to run the game.
- Play_game function uses hangman class to create instance
- Added while loop to check for game condition  

## Conclusion