import re

with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']

def byr(byrString, indexInList):
        word = re.findall(r'byr:\d\d\d\d', byrString)
        word = re.findall(r'\d\d\d\d', word[0])
        byrToken = (int)(word[0])
        if byrToken >= 1920 and byrToken <= 2002:
                fields[indexInList] = 'Y'

def iyr(iyrString, indexInList):
        word = re.findall(r'iyr:\d\d\d\d', iyrString)
        word = re.findall(r'\d\d\d\d', word[0])
        iyrToken = (int)(word[0])
        if iyrToken >= 2010 and iyrToken <= 2020:
                fields[indexInList] = 'Y'

def eyr(eyrString, indexInList):
        word = re.findall(r'eyr:\d\d\d\d', eyrString)
        word = re.findall(r'\d\d\d\d', word[0])
        eyrToken = (int)(word[0])
        if eyrToken >= 2020 and eyrToken <= 2030:
                fields[indexInList] = 'Y'

def hgt(hgtString, indexInList):
        word = re.findall(r'hgt:\d+\D\D', hgtString)
        measurement = []
        if word:
                word = re.findall(r'\d+\D\D', word[0])
                measurement = re.findall(r'\D\D', word[0])
                
        if measurement:
                if measurement[0] == 'in' or measurement[0] == 'cm':
                        if measurement[0] == 'in':
                                word = re.findall(r'\d+', word[0])
                                hgtToken = (int)(word[0])
                                if hgtToken >= 59 and hgtToken <= 76:
                                        fields[indexInList] = 'Y'
                        elif measurement[0] == 'cm':
                                word = re.findall(r'\d+', word[0])
                                hgtToken = (int)(word[0])
                                if hgtToken >= 150 and hgtToken <= 193:
                                        fields[indexInList] = 'Y'

def hcl(hclString, indexInList):
        word = re.findall(r'hcl:#[0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f][0-9a-f]', hclString)
        if word:
                fields[indexInList] = 'Y'

def ecl(eclString, indexInList):
        word = re.findall(r'ecl:[a-z][a-z][a-z]', eclString)
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if word:
                for c in colors:
                        if c in word[0]:
                                fields[indexInList] = 'Y'

def pid(pidString, indexInList):
        word = re.findall(r'pid:\d+', pidString)
        if word:
                word = re.split(r':', word[0])
                pidNumber = (int)(word[1])
                if len(word[1]) == 9:
                        if pidNumber <= 999999999 and pidNumber >= 1:
                                fields[indexInList] = 'Y'

#This function checks whether or not the data is valid
def validate(indexInList, x, indexString, fields):
        if x == 'byr':
                byr(indexString, indexInList)
        elif x == 'iyr':
                iyr(indexString, indexInList)
        elif x == 'eyr':
                eyr(indexString, indexInList)
        elif x == 'hgt':
                hgt(indexString, indexInList)
        elif x == 'hcl':
                hcl(indexString, indexInList)
        elif x == 'ecl':
                ecl(indexString, indexInList)
        elif x == 'pid':
                pid(indexString, indexInList)

counter = 0
c4 = 1
for c3, index in enumerate(input):

        if index == '' or c3 == len(input) - 1:
                if c3 == len(input) - 1:
                        for counter2, x in enumerate(fields):
                                if x in index:
                                        validate(counter2, x, index, fields)
                check = True
                for x in fields[:-1]:
                        if x != 'Y':
                                check = False
                if check:
                        counter += 1
                fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
                c4 += 1
        else:
                for counter2, x in enumerate(fields):
                        if x in index:
                                validate(counter2, x, index, fields)

print("The answer is: " + str(counter))        