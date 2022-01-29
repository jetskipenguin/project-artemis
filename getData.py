import csv
import random

# Function that gets question and answer data from csv file and returns 
# them as a list of questions and answers.
#
# Input  : Name of csv file.
# Output : A questions list, answers list, and link related to material.
#
def getData( name ):
    # open name.csv, skip first line, and create questions and answers list
    with open( name, 'r' ) as file:
        csvFile = csv.reader( file )
        next( csvFile )
        questions = [ ]
        answers = [ ]
        # iterates throgh file and appends questions and answers to respective lists
        for lines in csvFile:
            q, a, w1, w2, w3, link = lines
            questions.append( q )
            tmp = [ a, w1, w2, w3 ]
            answers.append( tmp )
    return questions, answers, link

# Function that grabs question from questions list and keeps track of what it has seen.
#
# Input  : List of seen questions, questions list, answers list, and a boolean value that turns
#          true when all questions have been seen.
# Output : The random question found, correct answer a, incorrect answers w(1-3), and boolean
#          value keeping track of if all questions have been seen or not.
#
def getQuestion( seen, questions, answers, boolVal ):
    # Sets num to length of questions and initialize answer variables.
    num = len( questions )
    a = w1 = w2 = w3 = ''
    # Prime loop with question. If question has already been seen, find a new question.
    question = random.choice( questions ) 
    while question in seen: 
        question = random.choice( questions ) 
        # If the length of seen questions equals the number of questions, return and set
        # boolean value to True.
        if( len(seen) == num ):
            boolVal = True
            return question, a, w1, w2, w3, seen, boolVal
    # Set answer variables to answers at index of question found. Return question and answers.
    a, w1, w2, w3 = answers[ questions.index( question ) ]
    seen.append( question )
    return question, a, w1, w2, w3, seen, boolVal