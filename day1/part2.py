


with open("input.txt", 'r') as f:
        input = [(int)(line.strip()) for line in f]

c1 = 0
firstNumber = 0
secondNumber = 0
thirdNumber = 0
for x in input:
        c2 = 0
        while c2 < len(input):
                c3 = 0
                while c3 < len(input):
                        firstNumber = input[c1]
                        secondNumber = input[c2]
                        thirdNumber = input[c3]
                        
                        if firstNumber + secondNumber + thirdNumber == 2020:
                                print(firstNumber * secondNumber * thirdNumber)
                                break
                        c3 += 1
                c2 += 1
        
        c1 += 1