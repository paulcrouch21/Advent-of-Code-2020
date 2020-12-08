import re

with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

counter = 0
for x in input:
        if counter == 0 or counter == 1:
                input[counter] = x * 1
        elif counter != 0 or counter != 1:
                input[counter] = x * counter
        counter += 1

right = 3
counter = 0
for x in input[1:]:
        if x[right] == '#':
                counter += 1
        right = right + 3

print("The answer is: " + str(counter))