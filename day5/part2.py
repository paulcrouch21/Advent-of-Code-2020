with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

def toBinary(stringToChange):
        binaryString = stringToChange.replace('B', '1')
        binaryString = binaryString.replace('F', '0')
        binaryString = binaryString.replace('R', '1')
        binaryString = binaryString.replace('L', '0')
        return int(binaryString, 2)

values = []
for counter, indexString in enumerate(input):
        values.append(toBinary(indexString))

values.sort()

counter = values[0]
for i in values:
        if counter != i:
                mySeat = counter
                print(f'The answer is {mySeat}')
                exit()
        counter += 1