from question import question1Dictionary
from question import question2Dictionary 
from question import question3Dictionary
from question import question4Dictionary
from question import question5Dictionary
from question import question6Dictionary
from question import question7Dictionary
from question import question8Dictionary
from question import question9Dictionary
from question import question10Dictionary
from question import possibleQuestions

DICTIONARYRANGE = 2
COUNTERGROWTH = 1
speficDictionaryInList = 0

#sets up a while true loop for my program to run

while True:
    print(" ")
    print("""Welcome, to my Quiz. It is about Maori custom in nz""")

    diffcultly= str(input("""what diffcult do you want to do
easy where the question are in a set and there is no score.
Or hard mode, where a score is kept, you are timed and the question are random: """))
    
    if diffcultly.lower() == "easy":
         
         # sets up a for loop to repeat for the number of questions
         for x in possibleQuestions:
              
              theQuestions = possibleQuestions[speficDictionaryInList]
               
              
              print(theQuestions["question"])
              print("what is the ans:")
              print(theQuestions["ans"])

              correctAnswer = theQuestions.value("correctAns")
              userAns = str(input())

              if correctAnswer.lower() == userAns.lower():
                   print("you got the question right")
              speficDictionaryInList =+ 1
                