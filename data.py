#import json

def legal(inp):
    inp = list(str(inp)) # make each digit into a str in a list
    if '0' not in inp: # if the is no zero
        return bool(len(inp) == len(set(inp))) # if all numbers are not repeating

all_raw = [] # all legal numbers
current = 1234 # lowest posible number

while len(str(current)) == 4: # while number is 4 digits
    if legal(current): # check legality
        all_raw.append(current) # add number to the all_raw list
    current += 1 # move to next number

BvC = [(4,0), (2,2), (1,3), (0,4), (3,0), (2,1), (1,2), (0,3), (2,0), (1,1), (0,2), (1,0), (0,1), (0,0)] # all BULL to COW ratios

guess = 1234 # the first guess
BC1r = input(f"{guess}>>>") # ask the result and store it raw
BC1rt = BC1r.split(",") # format the raw into a temp list
BC1 = (BC1rt[0],BC1rt[1]) # format the temp into a perm tuple

guess_split = [str(guess)[0], str(guess)[1], str(guess)[2], str(guess)[3]] # turn int into a list of spilits

pos1 = [] # possible numbers after first guess
for current in all_raw:
    if 1==1:
        if 1==1: # temp
            pos1.append(current)

# https://en.wikipedia.org/wiki/Bulls_and_Cows
