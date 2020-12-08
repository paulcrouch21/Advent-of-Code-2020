import re

with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

counter = 0
for x in input:
        r1 = re.split(r"\s", x)
        r2 = re.split(r"-", r1[0])
        index1 = int(r2[0])
        index2 = int(r2[1])
        letter = re.findall(r"\w", r1[1])

        phrase = r1[2]
        if (phrase[index1 - 1] == letter[0] and phrase[index2 - 1] != letter[0]) or (phrase[index1 - 1] != letter[0] and phrase[index2 - 1] == letter[0]):
                counter += 1

print("The answer is: " + str(counter))