# Magic-8-Ball to practice conditional statements, this program will answer "Yes" o "No" based on your fortune :)
import random

name = input("What's your name?: ")
question = input("What's your question?: ")

answer = ""
random_number = random.randint(1,9)

# print(random_number) test out random number generation

# Conditional selection

if random_number == 1:
    answer = "Yes - definitely"
elif random_number == 2:
    answer = "It is decidedly so"
elif random_number == 3:
    answer = "Without a doubt"
elif random_number == 4:
    answer = "Reply hazy, try again"
elif random_number == 5:
    answer = "Ask again later"
elif random_number == 6:
    answer = "Better not tell you know"
elif random_number == 7:
    answer = "My sources say no"
elif random_number == 8:
    answer = "Outlook not so good"
elif random_number == 9:
    answer = "Very doubtful"
else:
    answer = "Error"

if name == "":
    print ("Magic 8-Ball's answer: " + answer)
else:
    print ("\n" + name + " asks: " + question)
    print ("Magic 8-Ball's answer: " + answer)

