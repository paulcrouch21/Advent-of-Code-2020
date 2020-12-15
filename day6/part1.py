with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

questions = list(map(chr, range(97, 123)))

def main():
        totalYes = 0
        print(f'The total yes\'s are {groupByGroup(input, questions, totalYes)}')

#function to iterate through the groups
def groupByGroup(input, questions, totalYes):
        for counter, i in enumerate(input):
                if i == '' or counter == len(input) - 1:
                        for counter2, x in enumerate(questions):
                                if x in i:
                                        questions[counter2] = 'Y'
                        for i in questions:
                                if i == 'Y':
                                        totalYes += 1
                        questions = list(map(chr, range(97, 123)))
                else:
                        for counter2, x in enumerate(questions):
                                if x in i:
                                        questions[counter2] = 'Y'
        return totalYes

if __name__ == '__main__':
        main()