"""
Copyright 2015 Daniel Rosensweig

quiz.py is based on a project at Treehouse, in the course "Dates and Times in Python". My version was completed before viewing the professor's solution, and extends the original project considerably beyond what was asked. Some overall structure was given in the assignment, but implementation is my own. Comments with a single '#' were given, so they indicate what was given/expected. (Treehouse is an educational site, with courses aimed at learning to code in a variety of programming and scripting languages. For more info see https://teamtreehouse.com )

My extensions: 
- Allows subtraction and division problems, as well as addition and multiplication
- Allows user to decide length of quiz
- Tells user how long they took to solve each question
- Tells user total quiz time, and average question time
- Allows user to decide what types of problems to include (addition, subtraction, multiplication, division)
- Allows user to choose how large the numbers will be in quiz questions.
"""

import datetime
import random

from questions import Add, Subtract, Multiply, Divide


class Quiz:
    questions = []
    answers = []
    correct = 0
    times = []
    start = None
    end = None
    length = None
    
    def __init__(self):
        #generate 10 random questions with numbers from 1 to 10
        # add these questions into self.questions
        ## Allow user to specify how many questions in each quiz
        try:
            self.length = int(input("Welcome to math quiz. How many questions would you like? (Default 10):\n"))
        except:
            print("Using default, 10 question quiz.")
            self.length = 10
        print("="*10)
        ## Allow user to choose what types of questions they'd like to include.
        print("What types of questions would you like to answer?")
        print("(A)ddition, (S)ubtraction, (M)ultiplication, (D)ivision.")
        inp = input("Enter any or all letters ASMD. Default Addition and Subtraction.\n").lower()
        ops = []
        if 'a' in inp:
            ops.append('a')
        if 's' in inp:
            ops.append('s')
        if 'm' in inp:
            ops.append('m')
        if 'd' in inp:
            ops.append('d')
        if len(ops) == 0:
            print("Using default: addition and subtraction")
            ops.append('a')
            ops.append('s')
        print("="*10)
        ## Allow user to decide how large they'd like the numbers in quiz questions to be
        print("What is the largest number you'd like to add or multiply? (Total or answer may be higher)")
        print("For division and subtraction, chosen max will apply to two smaller terms, ")
        print("but may start with larger number in order to keep whole number answers.")
        try:
            max = int(input("Please enter a whole number. (Default is 10).\n"))
        except:
            max = 10
        for x in range(0,self.length):
            one = random.randint(0, max)
            two = random.randint(0, max)
            op = random.randint(0,len(ops)-1)
            if ops[op] == 'a':
                self.questions.append(Add(one, two))
            elif ops[op] == 's':
                self.questions.append(Subtract(one, two))
            elif ops[op] == 'm':
                self.questions.append(Multiply(one, two))
            else:
                self.questions.append(Divide(one, two))

    def take_quiz(self):
        #log the start time
        self.start = datetime.datetime.now()
        # ask all of the questions
        for question in self.questions:
            result = self.ask(question)
        # log if they got the question right
            self.answers.append(result[0])
            self.times.append(result[1])
            if result[0]:
                self.correct += 1            
        # log the end time
        self.end = datetime.datetime.now()
        # show a summary
        self.summary()

    def ask(self, question):
        # log the start time
        start1 = datetime.datetime.now()
        print("="*10)
        # capture the answer
        while True:
            try:
                answer = int(input('{}?\n'.format(question.text)))
                break
            except:
                print("Please enter a number!")
        # check the answer
        corr = answer == question.answer
        # log the end time
        end1 = datetime.datetime.now()
        time = end1 - start1
        print(time)
        if corr:
            print("Good job! That's correct.")
        else:
            print("Sorry, the correct answer was {}.".format(question.answer))
        print("You answered this question in {} seconds.".format(time.seconds))
        # if the answer's right, send back True
        # otherwise, send back false
        # send back the elapsed time, too
        return (corr, (time))
        
    def summary(self):
        # print how many you got right and the total # of questions
        print("="*10)
        print("You got {} questions out of {} correct.".format(self.correct, len(self.answers))) 
        # print the total time for the quiz
        time = (self.end - self.start).seconds
        print("You completed the quiz in {} seconds.".format(time))
        print("You averaged {} seconds to answer each question.".format(time/len(self.answers)))
        
quiz = Quiz()
quiz.take_quiz()
