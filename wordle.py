import random
from colorama import Fore, Back, Style

#Reading the words file
file = open("words.txt", "r")
words = file.read()
words = words.split() #spliting the words into a list

#choosing a random word
word_pos = random.randint(0, len(words)-1)
word = words[word_pos]

def dup_letters(letter, guessed_letters, word):
    
    count = 0
    
    for i in guessed_letters:
        if i == letter:
            count += 1

    for j in range(5, 0):
        if letter == word[j]:
            check = True
    
    if count > 1:
        print(Fore.RED + f"{letter}", end=" ")
    else:
        print(Fore.YELLOW + f"{letter}", end=" ")


#Main Function to check the letters entered into the terminal
def checker(guess, word):
    guessed_letters = []
    for i in range(0,5):
        if guess[i] in word:
            guessed_letters.append(guess[i])
            if word[i] == guess[i]:
                print(Fore.GREEN + f"{guess[i]}", end=" ")
            else:
                dup_letters(guess[i], guessed_letters, word)
        else:
            print(Fore.RED + f"{guess[i]}", end=" ")
    print(Style.RESET_ALL)


#input function: checks if user guess is more than five letters and splits guess & word into lists
def into(word):
    print("enter 5 letters - ")
    guess = input()
    guess = guess.lower()
    letters = guess.isalpha() #checks if guess are all alphabets and stores the boolean in letters

    if len(guess) != 5 or letters == False:
        print(Fore.RED + "Error, ENTER 5 Letters")
        print(Style.RESET_ALL)
        return 'n', 'n' #if user enters more than 5 letters or less than 5 letters or enters a non-alphabet, this is sent to the function call
    elif guess not in words:
        print(Fore.RED + "Word Not in List") #if the guessed word is not in the list, ths is sent to the function call
        print(Style.RESET_ALL)
        return 'n', 'n'
    else:
        guess = list(guess)
        word = list(word)
        checker(guess, word)
        return guess, word

#into function call
guess, word = into(word)

count = 1 #var to count number of tries

#This terminates the program when user guesses correctly or when number of tries have run out
while count < 6:
    if guess == 'n' and word == 'n': #from the into function if guess and word = 'n': redo the into function without adding to number of tries
        guess, word = into(words[word_pos]) #words[word_pos] sends to the into function the random word at the begining of the program 
    elif guess == word:
        count = 6
        print("WOW! You're so SMort ;)")
    else:
        count += 1
        guess, word = into(word)

if count >= 6 and guess != word:
    print(f"Oops you've run out of tries, \nThe word for the day: {words[word_pos]}")