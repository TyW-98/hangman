import random

word_list = ["Watermelon", "Honeydew", "Mango", "Apple", "Orange"]

print(word_list)

word = random.choice(word_list)

print(word)

guess = input("Guess the fruit : ")

if len(guess) == 1:
    print("Good guess!")
else:
    print("Oops! Input is greater than 1")