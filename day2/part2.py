import re

with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

counter = 0
counter3 = 1
for x in input:
        print("---------------" + str(counter3) + "---------------")
        r1 = re.split(r"\s", x)
        r2 = re.split(r"-", r1[0])
        index1 = int(r2[0])
        index2 = int(r2[1])
        letter = re.findall(r"\w", r1[1])

        print("Index1: " + str(index1))
        print("Index2: " + str(index2))
        print("Letter: " + str(letter[0]))

        if index1 != 0 and index2 != 0:
                counter2 = 1
                for i in r1[2]:
                        print(counter2)
                        print(i)
                        if ((counter2 == index1 and counter2 != index2) or (counter2 != index1 and counter2 == index2)) and i == letter[0]:
                                counter += 1
                        counter2 += 1
        print(counter)

        #if counter2 >= min and counter2 <= max:
        #       counter += 1
        counter3 += 1

print("The answer is: " + str(counter))