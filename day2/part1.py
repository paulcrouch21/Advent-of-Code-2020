import re

with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

counter = 0
for x in input:
        r1 = re.split(r"\s", x)
        r2 = re.split(r"-", r1[0])
        min = int(r2[0])
        max = int(r2[1])
        letter = re.findall(r"\w", r1[1])

        counter2 = 0
        for index in r1[2]:
                if index == letter[0]:
                        counter2 += 1

        if counter2 >= min and counter2 <= max:
                counter += 1

print("The answer is: " + str(counter))