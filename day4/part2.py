import re

with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

#This function checks whether or not the data is valid
def validate(c2, x, index, fields):
        if x == 'byr':
                newString = re.findall(r'byr:\d\d\d\d', index)
                newString = re.findall(r'\d\d\d\d', newString[0])
                if (int)(newString[0]) >= 1920 and (int)(newString[0]) <= 2002:
                        fields[c2] = 'Y'
        elif x == 'iyr':
                newString = re.findall(r'iyr:\d\d\d\d', index)
                newString = re.findall(r'\d\d\d\d', newString[0])
                if (int)(newString[0]) >= 2010 and (int)(newString[0]) <= 2020:
                        fields[c2] = 'Y'
        elif x == 'eyr':
                newString = re.findall(r'eyr:\d\d\d\d', index)
                newString = re.findall(r'\d\d\d\d', newString[0])
                if (int)(newString[0]) >= 2020 and (int)(newString[0]) <= 2030:
                        fields[c2] = 'Y'
        elif x == 'hgt':
                newString = re.findall(r'hgt:\d+\D\D', index)
                measurement = []
                if isEmpty(newString) == False:
                        newString = re.findall(r'\d+\D\D', newString[0])
                        measurement = re.findall(r'\D\D', newString[0])
                
                if isEmpty(measurement) == False:
                        if measurement[0] == 'in' or measurement[0] == 'cm':
                                if measurement[0] == 'in':
                                        height = re.findall(r'\d+', newString[0])
                                        if (int)(height[0]) >= 59 and (int)(height[0]) <= 76:
                                                fields[c2] = 'Y'
                                elif measurement[0] == 'cm':
                                        height = re.findall(r'\d+', newString[0])
                                        if (int)(height[0]) >= 150 and (int)(height[0]) <= 193:
                                                fields[c2] = 'Y'
        elif x == 'hcl':
                newString = re.findall(r'hcl:#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]', index)
                if isEmpty(newString) == False:
                        fields[counter2] = 'Y'
        elif x == 'ecl':
                newString = re.findall(r'ecl:[a-z][a-z][a-z]', index)
                colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                if isEmpty(newString) == False:
                        for c in colors:
                                if c in newString[0]:
                                        fields[counter2] = 'Y'
        elif x == 'pid':
                newString = re.findall(r'pid:\d+', index)
                if isEmpty(newString) == False:
                        newString = re.split(r':', newString[0])
                        pidNumber = (int)(newString[1])
                        if pidNumber <= 999999999 and pidNumber >= 1:
                                fields[counter2] = 'Y'

#Checks whether or not a list is empty
def isEmpty(myList):
        if myList:
                return False
        else:
                return True

counter = 0
c4 = 1
for c3, index in enumerate(input):

        if index == '' or c3 == len(input) - 1:
                if c3 == len(input) - 1:
                        for counter2, x in enumerate(fields):
                                if x in index:
                                        validate(counter2, x, index, fields)
                check = True
                print(fields)
                for x in fields[:-1]:
                        if x != 'Y':
                                check = False
                if check:
                        counter += 1
                fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
                print('Iteration: ' + str(c4))
                c4 += 1
        else:
                for counter2, x in enumerate(fields):
                        if x in index:
                                validate(counter2, x, index, fields)

print("The answer is: " + str(counter))        