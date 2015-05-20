"""
Copyright 2015 Daniel Rosensweig
questions.py provides helper classes for quiz.py
"""

class Question:
    answer = None
    text = None

class Add(Question):
    def __init__(self, num1, num2):
        self.text = '{} + {}'.format(num1, num2)
        self.answer = num1 + num2
        
class Subtract(Question):
    def __init__(self, num1, num2):
        top = num1 + num2
        self.text = '{} - {}'.format(top, num1)
        self.answer = num2
        
class Multiply(Question):
    def __init__(self, num1, num2):
        self.text = '{} * {}'.format(num1, num2)
        self.answer = num1 * num2

class Divide(Question):
    def __init__(self, num1, num2):
        ##Make sure you're not dividing by zero. We'll just make all the zero divisors into 1 instead.
        if num1 == 0:
            num1 += 1
        top = num1 * num2
        self.text = '{} / {}'.format(top, num1)
        self.answer = num2
