# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:27:43 2018

Collatz Conjecture Script

@author: Christopher Sinclair
"""

#%% - Necessary Imports
import matplotlib.pyplot as plt

#%% - Introductory explanation about the conjecture
print("Let's experiment with some basic number theory. Let's create a sequence of numbers with the following rules. For any integer n > 1, if n is odd, the next number will be n multiplied by three and one added to it: (3n+1). If n is even, let's divide by two to get the next number: (n/2).")
print("We will halt the sequence when we get to 1. For example, if we start with 5, we will multiply by three and add one to get 16. Divide by two and get 8. Divide by two and get 4. Divide by 2 and get 2. Divide by 2 and get 1. Stop. The resulting sequence is now 5, 16, 8, 4, 2, 1. Make sense?")
print("\n")
print("The Collatz Conjecture states that if you start the sequence off with any positive integer greater than one, it will always halt at 1 over some finite amount of steps.")
print("Can you find a starting integer which will lead to a sequence that never terminates at 1 thus breaking Collatz Conjecture and earning $500?")
print("\n") 

#%% - Main logic
sequence = []
def run_conjecture_test():
    number = int(input("Give me an integer greater than one (n > 1)!: "))
    counter = 0 # set the counter
    while(number != 1): # while we haven't hit the stopping point...
        if(number % 2 == 0): # if the number is even...
            number = number // 2 # divide by two
            sequence.append(number) # append to the list
            counter += 1 # increment the counter
        else: # if the number is odd...
            number = (3 * number) + 1 # multiply by 3 and add 1
            sequence.append(number) # append to the list
            counter += 1 # increment the counter

    steps = str(counter) # convert the counter to a string for total steps
    print("Completed in " + steps + " steps.")
    print_sequence = input("Would you like to see the sequence? (y/n): ")
    if(print_sequence == "y"):
        for i in range(len(sequence)):
            if i == (len(sequence) - 1): # if last number...
                print(str(sequence[i])) # don't print a comma
            else:
                print(str(sequence[i]) + ', ', end='') # include a comma without a line break
        x = range(0, len(sequence)) # x axis is the number of steps it took to converge
        plt.figure(figsize=(15,15))
        plt.plot(x, sequence) # plot number of steps versus value at that step
        plt.show()

#%% - Main text interface
play_again = True
while(play_again != False):
    run_conjecture_test()
    play_again_input = input("Play again? (y/n): ")
    if(play_again_input == "y"):
        play_again = True
        continue
    elif(play_again_input == "n"):
        print("Confounded by Collatz! Thanks for playing!")
        break
    else:
        print("Unidentified input. Assuming abort.")
        break
