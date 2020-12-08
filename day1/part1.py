<<<<<<< HEAD
=======



>>>>>>> 63508801467b18cd6c7f368d27a39538fe9ea66b
with open("input.txt", 'r') as f:
        input = [(int)(line.strip()) for line in f]

c1 = 0
firstNumber = 0
secondNumber = 0
for x in input:
        c2 = 0
        while c2 < len(input):
                firstNumber = input[c1]
                secondNumber = input[c2]
                if firstNumber + secondNumber == 2020:
                        print(firstNumber * secondNumber)
                        exit()
                c2 += 1
        
        c1 += 1