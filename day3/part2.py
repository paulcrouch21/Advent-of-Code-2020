with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

#counter = 0
#for x in input:
#        if counter == 0 or counter == 1:
#                input[counter] = x * 1
#        elif counter != 0 or counter != 1:
#                input[counter] = x * counter
#        counter += 1

slopes = [(1,1), (3, 1), (5, 1), (7, 1), (1, 2)]

def traverse(right, down):
        counter = 0
        d = right
        maxD = len(input[0])
        for index, x in enumerate(input[down:]):
                if index % down != 0:
                        continue
                if x[d] == '#':
                        counter += 1
                d += right
                #This will loop the input horizontally
                d %= maxD
        return counter

answer = 1
for i in slopes:
        answer *= traverse(i[0], i[1])

print(f'The answer is: {answer}')