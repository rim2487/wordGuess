import random


global n

# printing out the clues to a list
def clue_list():
    clue = (str(n+1) + "-" + secret_word[n])
    clues.append(clue)
    print(clues)

  # Getting a random number without repeating the same number
  # you must give the user unique clues. Hence the random numbers cannot be the same.
  # With this function you get a list of non repetitive list of random numbers
def randomNumber():
    rand_numbers = []
    for i in range(word_length):
        x= random.randint(1,word_length-1)
        if x not in rand_numbers: rand_numbers.append(x)

    return rand_numbers






clues = []
guesses_counter = 5
words = ["explicit", "applied", "favour", "simplicity", "pride", "emotion", "confrontation", "lease", "condition",
         "countryside", "chemistry"]
secret_word = random.choice(words)
word_length = len(secret_word)
print(words)
print(word_length)



guess = input("Guess the word: ")

while guesses_counter != 0:

    randomNumber()
    n = random.choice(randomNumber())
    if guess == secret_word:
        print("Congratulations. You guessed the correct word!")
        break
    else:
        print("try again!")
        print("Here are some clues. The " + str(n + 1) + " letter of the word is ", secret_word[n])
        guesses_counter -= 1
        print("You have ",guesses_counter," guesses remaining")
        clue_list()
        guess = input("Guess again : ")

if guesses_counter==0:
    print("Looks like you have no guesses left! Try harder next time.")

print("Thank you for playing the game!")
