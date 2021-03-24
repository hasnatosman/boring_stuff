import random


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is one'
    elif answerNumber == 2:
        return 'It is two'
    elif answerNumber == 3:
        return 'It is four'
    if answerNumber == 4:
        return 'It is one'
    elif answerNumber == 5:
        return 'It is five'
    elif answerNumber == 6:
        return 'It is six'


r = random.randint(1, 6)
fortune = getAnswer(r)
print(fortune)
