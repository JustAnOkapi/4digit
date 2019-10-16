#import json

def legal(inp):
    inp = list(str(inp)) # make each digit into a str in a list
    if '0' not in inp: # if the is no zero
        return bool(len(inp) == len(set(inp))) # if all numbers are not repeating

current = 1234 # lowest posible number
all_raw = [] # create non-formatted data
while len(str(current)) == 4: # while number is 4 digits
    if legal(current): # check legality
        all_raw.append(current) # add number to the all_raw list
        current += 1 # move to next number
    else: # if not legal
        current += 1 # skip to next number

data = {} # create formatted data

for current in all_raw:
    for current2 in all_raw:
        continue # i dont know what i was doing

print(all_raw)
print(data)


# https://en.wikipedia.org/wiki/Bulls_and_Cows
