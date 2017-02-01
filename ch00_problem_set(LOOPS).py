# LOOPS (22pts TOTAL)
import random

# PROBLEM 1 (Fibonacci - 4pts)
## The Fibonacci sequence is a sequence of numbers that starts with 1, followed by 1 again.
# Every next number is the sum of the two previous numbers.
# I.e., the sequence starts with 1, 1, 2, 3, 5, 8, 13, 21,...
# Write a program that calculates and prints the Fibonacci sequence
# until the numbers get higher than 1000.

number = 1
sequence_list = [1, 1]
index = 2
while number <= 1000:
    number = sequence_list[index - 2] + sequence_list[index - 1]
    sequence_list.append(number)
    index += 1
print(sequence_list)



# PROBLEM 2 (Number Guessing Game - 6pts)
# Write a program that takes a random integer between 1 and 1000
# The program then asks the user to guess the number.
# After every guess, the program will say either “Lower”
# if the number it took is lower, “Higher” if the number it took is higher,
# and “You guessed it!” if the number it took is equal to the number
# It might be wise, for testing purposes, to also display the number that the
# program randomly picks, until you are sure that the program works correctly

computer_selection = random.randrange(1, 1001)
print("The computer selection is:", computer_selection)

correct = False
while not correct:
    user_guess = input("Please enter your guess: ")
    if int(user_guess) > computer_selection:
        print("Lower")
    elif int(user_guess) < computer_selection:
        print("Higher")
    else:
        print("Correct!!")
        correct = True


# PROBLEM 3 (Dice Hi-Low - 6pts)
# You roll five six-sided dice, one by one.
# How big is the probability that the value of each die
# is greater than or equal to the value of the previous die that you rolled?
# For example, the sequence “1, 1, 4, 4, 6” is a success,
# but “1, 1, 4, 3, 6” is not. Determine the
# probability of success using a simulation of a large number of trials.
done = False
total_trials = 0
failures = 0
while not done:
    roll_list = []
    finished = False # finished with an individual series of rolls
    for i in range(5):
        roll = random.randrange(1 ,7)
        roll_list.append(roll)
        if (roll_list[i] < roll_list[i-1] and i != 0) and not finished:
            failures += 1
            finished = True
    total_trials += 1
    if total_trials > 100000:
        done = True

print("The probability of success is:", (total_trials - failures) / total_trials * 100, "percent")


# PROBLEM 4 (Number Puzzler - 6pts)
# A, B, C, and D are all different digits.
# The number DCBA is equal to 4 times the number ABCD.
# What are the digits?
# Note: to make ABCD and DCBA conventional numbers, neither A nor D can be zero.
# Use a quadruple-nested loop to solve.
for a in range(10):
    for b in range(10):
        for c in range(10):
            for d in range(10):
                first_value = (d * 1000) + (c * 100) + (b * 10) + a
                second_value = (a * 1000) + (b * 100) + (c * 10) + d
                if first_value == 4 * second_value and a != 0 and d != 0:
                    print("a =", a)
                    print("b =", b)
                    print("c =", c)
                    print("d =", d)

