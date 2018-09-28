import random

# get input from the user
num_rolls = int(input('Enter number of rolls:\n'))

# print a newline to make the output cleaner
print()

# make a dictionary to store the dice roll values
totals = {}

# define a function to get the numbers from the totals list
def times(value):
    if value > 0:
        for i in range(value):
            print('*', end=' ')

while num_rolls >= 1:
    # get the total of each roll and then add the data to the dictionary
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2
        if str(roll_total) in totals:
            totals[str(roll_total)] += 1
        else:
            totals[str(roll_total)] = 1

    # print the statistics
    for i in totals:
        print(f"{i}s:", end=' ')
        times(totals[i])
        print()


    # print a newline for cleanliness
    print()

    # get the next number of rolls
    num_rolls = int(input('Enter number of rolls:\n'))
else:
    print('Invalid number of rolls. Try again.')
