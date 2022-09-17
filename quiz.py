import random as r
import csv
import os

def loadquiz(csvfile):
    with open(csvfile) as f:
        reader = csv.DictReader(f)
        quiz = list(reader)
    return quiz

def selectquestions(quiz, num):
    return r.sample(quiz, num)

def askquestions(questions, immediateanswer=False):
    score = 0
    wrongequestions=[]
    for q in questions:
        os.system('cls') if os.name == 'nt' else os.system('clear') # clear screen
        print(q['question'])
        print('A: ' + q['A'])
        print('B: ' + q['B'])
        print('C: ' + q['C'])
        print('D: ' + q['D'])
        answer = input('Answer: ')
        if answer.upper() == q['answer'].upper():
            score += 1
        else:
            wrongequestions.append({'question':q['question'], 'wronganswer':q[answer.upper()], 'correctanswer':q[q['answer'].upper()]})
            if immediateanswer:
                print('The correct answer is ' + q[(q['answer'].upper())])
    return (score, wrongequestions)

def printresultes(score):
    os.system('cls') if os.name == 'nt' else os.system('clear') # clear screen
    print('------Score Report-------------')
    print('You got ' + str(score[0]) + ' out of ' + str(len(quiz)) + ' correct')
    print('------Study these questiosn----')
    if (score[0]<numquestions):
        for q in score[1]:
            print('Question: ' + q['question'])
            print('\t Answered: ' + q['wronganswer'])
            print('\t Correct: ' + q['correctanswer'])
    

def getQuiz(invalid=False):
    quizefiles = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.csv')]
    os.system('cls') if os.name == 'nt' else os.system('clear') # clear screen
    if invalid:
        print('Invalid quiz file')
    print('Select a quiz:')
    for i in range(len(quizefiles)):
        print(str(i+1) + ': ' + quizefiles[i])
    quiznum = int(input('Quiz number: '))
    try:
        return quizefiles[quiznum-1]
    except:
        return getQuiz(True)

def getNumQuestions():
    numquestions = int(input('How many questions would you like to answer? '))
    return numquestions

quizfile=getQuiz()
numquestions=getNumQuestions()
questions = loadquiz(quizfile)
try:
    quiz = selectquestions(questions, numquestions)
except ValueError:
    print('The quiz file does not have enough questions, there are only ' + str(len(questions)) + ' questions in the file')
    exit()
score = askquestions(quiz)
printresultes(score)


