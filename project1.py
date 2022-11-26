# Python program to design a biased dice throw
# function

# Importing random library
import random

# Function to give a biased dice throw
def dice_throw():
	
	# Declaring the sequence
	
	sequence = [1, 1, 1, 2, 3, 3, 4, 5, 6, 6, 6, 6]
	
	# using random.random() to
	# get a random number
	rand_idx = int(random.random() * len(sequence))

	# Printing the random result
	print(sequence[rand_idx])

# Driver Code
# Calling the function
dice_throw()