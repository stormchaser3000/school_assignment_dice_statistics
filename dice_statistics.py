import random

num_sixes = 0
num_sevens = 0
num_rolls = int(input('Enter number of rolls:\n'))
totals = []

# define a function to get the numbers from the totals list
def times(lst, x):
    times = 0
    for i in lst:
        if i == x:
            times += 1
    return times

while num_rolls >= 1:
    for i in range(num_rolls):
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll_total = die1 + die2

        # add the sum of the dice to a dictionary each roll
        totals.append(roll_total)

    max_dice_num = 12

    # print the statistics
    print("\nDice rolling statistics:")
    for i in range(max_dice_num):
        print(f"{i + 1}s: {times(totals, i)}")

    num_rolls = int(input('Enter number of rolls:\n'))
else:
    print('Invalid number of rolls. Try again.')
