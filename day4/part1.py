with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

counter = 0
for c3, index in enumerate(input):

        if index == '' or c3 == len(input) - 1:
                if c3 == len(input) - 1:
                        for counter2, x in enumerate(fields):
                                if x in index:
                                        fields[counter2] = 'Y'
                check = True
                for x in fields[:-1]:
                        if x != 'Y':
                                check = False
                if check == True:
                        counter += 1
                fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
        else:
                for counter2, x in enumerate(fields):
                        if x in index:
                                fields[counter2] = 'Y'

print("The answer is: " + str(counter))        