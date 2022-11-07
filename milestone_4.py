import random

class Hangman:
    
    def __init__(self, word_list,num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(self.word_list).lower()
        self.word_guessed = ["_"] *len(self.word)
        self.num_letters = len(set(self.word))
        self.list_of_guesses = []
    
    def check_guess(self,guess):
        guess = guess.lower()
        
        if guess in set(self.word):
            
            print("Good guess! {guess} is in the word")

            for letters in range(len(self.word)):
                if guess == self.word[letters]:
                    self.word_guessed[letters] = guess     
                    
                    print(self.word_guessed)
                    
        else:
             self.num_lives -= 1  
             
             print(f"Oops! {guess.upper()} is not in the word")     
             print(f"You have {self.num_lives} lives left")

        
        
    def ask_for_input(self):
        while True:
            guess = input("Enter a letter to guess the fruit: ")
            
            if len(guess) != 1:
                print("Please only enter a single alphabetical character")
            elif guess in self.list_of_guesses:
                print(f"{guess} has already been tried")
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)

x1= Hangman(["apple"])

x1.ask_for_input()

print(x1.list_of_guesses)