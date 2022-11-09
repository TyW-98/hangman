# Python Hangman Project

A hangman game that allows user to guess what is the fruit that will be randomly selected from a word_list. The word_list consist of the following fruits:

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
* Using a `while` loop with a `True` condition, this allows the loop to run indefinitely. In the while loop, the `input()` function is used to obtain the user input and store in a variable named `guess`. 
* An `if` statement is also used to validate the length of the user input. If the length of user input equals to 1, a break statement is used to break out of the while loop. Else, the message "Invalid number of letters. Please, enter a single alphabetical character." will be printed. 

    ```go
    while True:
        guess = input("Enter a letter: ")
        
        if len(guess) == 1:
            break
        else:
            print("Invalid number of letters. Please, enter a single alphabetical character.")
    ```
* Created a `check_guess(letter)` function. Creating a custom function allows the block of code within the body of the function to be reuse multiple times without the need to rewrite the block of code hence reduces duplication of code. In the `check_guess(letter)` function, it takes in a letter to check if the letter is in the secret word. If the letter is in the secret_word, "Good guess! {letter.lower()} is in the word." will be printed or else, "Sorry, {letter.lower()} is not in the word. Try again." will be printed.

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
* A hangman class was created using object oriented programming paradigm. To initailise the attributes of the class `__init__` was used. 
    ```go
    def __init__(self, word_list,num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ["_"] *len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    ```
    ### Attribute list
    1. word: The word to be gussed which will be randomly selected from word_list.
    2. word_gueesed: Displays the correctly guessed letters and which letter of the word is missing.
    3. num_letters: Number of unique letters in the word that has have not been guessed.
    4. num_lives: Number of lives the player starts with.
    5. word_list: The list of fruits.
    6. list_of_guesses: A list of letters that have already been tried. 
 
* Created a `check_guess(self,guess)` method which will first check if the letter guessed is in the word. If the letter is in the word, a `for` loop is then used to loop through the word in order to replace the underscore with the correctly guessed letter.
* If the guessed letter is not in the word, 1 life will be taken away and the message "Oops! {guess.upper()} is not in the word" together with "You have {self.num_lives} lives left" will be printed.
  
    ```go
    def check_guess(self,guess):
        guess = guess.lower()
        
        if guess in set(self.word):
            
            print("Good guess! {guess} is in the word")

            for letters in range(len(self.word)):
                if guess == self.word[letters]:
                    self.word_guessed[letters] = guess     
                    
                    print(self.word_guessed)
            
            self.num_letters -= 1
            #print(self.num_letters)
                         
        else:
             self.num_lives -= 1  
             
             print(f"Oops! {guess.upper()} is not in the word")     
             print(f"You have {self.num_lives} lives left")
    ```
* Created a `ask_for_input(self)` method. This method takes in the user input to check if the length of the input is equals to 1 and the letter inputed has not attempted before using `if` statements. 

    ```go
    def ask_for_input(self):
        
        print(self.word_guessed)
        
        while True:
            guess = input("Enter a letter to guess the fruit: ")
            
            if len(guess) != 1:
                print("Please only enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print(f"{guess} has already been tried")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
    ```
## Milestone 5
- Added play_game function to run the game.
- Play_game function uses hangman class to create instance
- Added while loop to check for game condition  

## Conclusion