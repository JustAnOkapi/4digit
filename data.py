#import json

def legal(input):
    input = list(str(input))
    if '0' not in input: 
        if len(input) == len(set(input)):
            return True
        else: 
            return False
    else: 
        return False

current = 1234
all_raw = []
while len(str(current)) == 4:
    if legal(current):
        all_raw.append(current)
        current += 1
    else:
        current += 1
        continue

data = {}

for current in all_raw:
    for current2 in all_raw:
        

print(all_raw)
print(data)