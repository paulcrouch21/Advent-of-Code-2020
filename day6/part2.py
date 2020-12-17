with open("input.txt", 'r') as f:
        input = [line.strip() for line in f]

#answer is 3125

def main():
        questions = list(map(chr, range(97, 123)))
        numberOfAnswers = [0] * len(questions)
        print(f'The answer is {groupByGroup(input, questions, numberOfAnswers)}')

#function to iterate through the groups
def groupByGroup(input, questions, numberOfAnswers):
        answer = 0
        people = 0
        for counter, i in enumerate(input):
                if i == '' or counter == len(input) - 1:
                        for counter2, x in enumerate(questions):
                                if x in i:
                                        numberOfAnswers[counter2] += 1
                                        if counter == len(input) - 1:
                                                people += 1

                        print(f'People are: {people}')

                        answer += counts(numberOfAnswers, people)
                        print(f'The new answer is {answer}')

                        #resets the values
                        questions = list(map(chr, range(97, 123)))
                        numberOfAnswers = [0] * len(questions)
                        people = 0

                else:
                        for counter2, x in enumerate(questions):
                                if x in i:
                                        numberOfAnswers[counter2] += 1
                        people += 1
        return answer

def counts(numberOfAnswers, people):
        print(numberOfAnswers)
        answer = 0
        for i in numberOfAnswers:
                if i == people:
                        answer += 1
        print(f'Answer is {answer}')
        print('\nThe next one is:')
        return answer

if __name__ == '__main__':
        main()