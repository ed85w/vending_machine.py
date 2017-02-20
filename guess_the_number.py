import random

TOTAL_GUESSES = 10
RANGE_TOP = 10


def guess_number():
    # give the user a certain amount of guesses
    for i in range(TOTAL_GUESSES):
        guesses_left = 10 - i
        print "You have " + str(guesses_left) + " guesses left"
        guess = int(raw_input("guess the number: "))
        if guess == random_number:
            print "Well Done"
            break
        elif guess > random_number:
            print "Too High"
        else:
            print "Too Low"


while True:
    #generate the random number
    random_number = random.randint(0,RANGE_TOP)
    print "Guess between 0 and " + str(RANGE_TOP)

    guess_number()

    print "Lets try a new number!"
