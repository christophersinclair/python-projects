# This is a fun little game/project with my very first time creating a simple gaming algorithm from scratch


import random   # needed to make random number
import math		# needed for fraction splitting

def main():
	print "Welcome to sticks.py!\nThe goal of this game is to take a number of sticks (up to 5) from a pile and whoever can't pick up anymore sticks loses!\nGood luck!"
	global total_count
	total_count = random.randint(6, 75)                     # create a random integer between 6 and 100
	print "The total number of sticks is: %d" % total_count  # print the randomly generated integer
	take_turns()                                             # start the turn-based sequence



def take_turns():
	while total_count > 0:  # while no one has won the game...
		user_select()		# ...let the player go first...
		AI_take()			# ...then the computer

def user_select():
	user_selected = input("Please select an amount to take between 1 and 5: ")											# let the user select a number to take
	if user_selected != 1 and user_selected != 2 and user_selected != 3 and user_selected != 4 and user_selected != 5:	# sanitize inputs for only 1 through 5
		print "Try again."
		user_select()																									# go back to beginning of function if not correct input
	total_count = take(user_selected)																					# call the take function
	print "After your move, there are now %d sticks" % total_count														# print new total sticks
	return

def take(amount):
	global total_count						# call global variable
	total_count = (total_count - amount)	# subtract specified amount from total count
	return(total_count)

def AI_take():
	global total_count						# call global variable
	print "AI moves..."
	float_number = total_count / 6.0		# create a float by dividing by 6
	frac, whole = math.modf(float_number)   # grab the decimal portion of float_number

	frac = round(frac,4)					# round the decimal portion

	if (frac) == 0:							# take a certain number of sticks based on what the decimal portion earlier is
		sticks_taken = 5
		total_count = take(5)
	elif (frac) == (round(1.0/6,4)):
		sticks_taken = 1
		total_count = take(1)
	elif (frac) == (round(1.0/3,4)):
		sticks_taken = 2
		total_count = take(2)
	elif (frac) == (round(1.0/2,4)):
		sticks_taken = 3
		total_count = take(3)
	elif (frac) == (round(2.0/3,4)):
		sticks_taken = 4
		total_count = take(4)
	elif (frac) == (round(5.0/6,4)):
		sticks_taken = 5
		total_count = take(5)
	else:
		print "AI admits it is stupid..."			# if all else fails, sweep any mathematical problems under the rug...

	print "AI takes %d sticks..." % sticks_taken
	print "There are now %d sticks" % total_count
	take_turns()									# switch to player's turn

if __name__ == "__main__":
	main()
