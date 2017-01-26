#SECTION 2 - FUNCTIONS (20PTS TOTAL)
import math
import random
#PROBLEM 1 (Length of String - 3pts)
# Make a function which asks the user to enter a string, then prints the length of that string.
# You will need to use the input() function.
# Make a call to that function
'''
def input_length(string):
    str(string)
    print("Your string is:", len(string), "characters")

input_length(input("Input your string here: "))


# PROBLEM 2 (Pythagorean theorem - 4pts)
# The Pythagorean theorem states that of a right triangle, the square of the
# length of the diagonal side is equal to the sum of the squares of the lengths
# of the other two sides (or a^2 + b^2 = c^2).
# Write a program that asks the user for the lengths of the two sides that meet at a right angle.
# Then calculate the length of the third side, and display it in a nicely formatted way.
# You may ignore the fact that the user can enter negative or zero lengths for the sides.

first_leg = input("What is the length of the first leg?: ")
second_leg = input("What is the length of the second leg?: ")
print(math.sqrt(float(first_leg) ** 2 + float(second_leg) ** 2))


# PROBLEM 3 (Biggest, smallest, average - 4pts)
# Make a function to ask the user to enter three numbers.
# Then print the largest, the smallest, and their average, rounded to 2 decimals.
# Display the answers in a "nicely" formatted way.
# Make a call to your function.

def sequence(first_number, second_number, third_number):
    input_list = []
    input_list.append(float(first_number))
    input_list.append(float(second_number))
    input_list.append(float(third_number))
    large = max(input_list)
    small = min(input_list)
    average = round(sum(input_list) / float(len(input_list)), 2)
    print()
    print("max:", large,)
    print("min:", small)
    print("mean:", average)

sequence(input("type your first number: "), input("input your second number: "), input("input your third number: "))

'''

# PROBLEM 4 (e to the... - 3pts)
# Calculate the value of e (from the math library) to the power of -1, 0, 1, 2, and 3.
# display the results, with 5 decimals, in a nicely formatted manner.


def e_raised(power):
    print("e ^", "(" + str(power) + ") = " + str(math.e ** (power)))
e_raised(-1)
e_raised(0)
e_raised(1)
e_raised(2)
e_raised(3)

# PROBLEM 5 (Random int - 3pts)
# Generate a random integer between 1 and 10 (1 and 10 both included),
# but only use the random() function (randrange is not allowed here)

random_number = int(random.random() * 10) + 1
print(random_number)


# PROBLEM 6 (add me, multiply me - 3pts)
# Make a function which takes in two integers and RETURNS their sum AND their product.

def add_multiply(first, second):
    return([first + second, second * first])

print(add_multiply(1,2))