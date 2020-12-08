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

slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]

def traverse(right, down):
        counter = 0
        d = right
        if down == 1:
                for x in input[1:]:
                        if x[d] == '#':
                                counter += 1
                        d += right
        else:
                index = 0
                for x in input[2:]:
                        if x[d] == '#' and index % down != 0:
                                counter += 1
                        d += right
                        index += 1
        return counter

answer = 1
for i in slopes:
        answer *= traverse(i[0], i[1])

print("The answer is: " + str(answer))