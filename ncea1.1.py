import random
from question import questionDictionary
question = questionDictionary["questions"]
answer1 = questionDictionary["possible answers 1"]
answer2 = questionDictionary["possible answers 2"]
answer3 = questionDictionary["possible answers 3"]
answer4 = questionDictionary["possible answers 4"]
correctAnswer = questionDictionary["correct answers"]


#sets up a while true loop for my program to run
while True:
    score = 0
    print(" ")
    print("""Welcome, to my Quiz. It is about Maori custom in nz""")

    diffcultly= str(input("""what diffcult do you want to do
\n easy where the question are in a set and there is no score.
\n Or hard mode, where a score is kept, you are timed and the question are random: """))
    
    if diffcultly.lower() == "easy":
         
         # sets up a for loop to repeat for the number of questions
         for x in range(10):
              
              print(question[x])
              
              # makes the possible answer that don't hold value not appear to make the UI look cleaner
              if answer1[x] != "":
               print(answer1[x])
              
              if answer2[x] != "":
               print(answer2[x])
              
              if answer3[x] != "":
               print(answer3[x])
              
              if answer4[x] != "":
               print(answer4[x])

              userInput = input()

              # converts the user input into a string or float when needed
              try:
               userInput = float(userInput)
              except:
               userInput = str(userInput)
               
               # if the user enters a letter the user input is converted to something the correct answer 
               match userInput.lower():
                
                case "a":
                        userInput = answer1[x]
                  
                case"b":
                        userInput = answer2[x]
                  
                case "c":
                        userInput = answer3[x]
                  
                case "d":
                        userInput = answer4[x]
               
              if userInput == correctAnswer[x]:
                   print("you got the question right")
                   score += 1
              
              else:
                 print('you got the question wrong')
              
         print(f"well done you have finished the quiz and have scored {score} out of 10")

    if diffcultly.lower() == "hard":
        
        hardQuestionOrder = {}
        if len(hardQuestionOrder) != 10:
         hardQuestionOrder.add(random.randint(1,11))
                               # sets up a for loop to repeat for the number of questions
         for x in range(10):
              
              print(question[hardQuestionOrder[x]])
              
              # makes the possible answer that don't hold value not appear to make the UI look cleaner
              if answer1[hardQuestionOrder[x]] != "":
               print(answer1[hardQuestionOrder[x]])
              
              if answer2[hardQuestionOrder[x]] != "":
               print(answer2[hardQuestionOrder[x]])
              
              if answer3[x] != "":
               print(answer3[hardQuestionOrder[x]])
              
              if answer4[hardQuestionOrder[x]] != "":
               print(answer4[hardQuestionOrder[x]])

              userInput = input()

              # converts the user input into a string or float when needed
              try:
               userInput = float(userInput)
              except:
               userInput = str(userInput)
               
               # if the user enters a letter the user input is converted to something the correct answer 
               match userInput.lower():
                
                case "a":
                        userInput = answer1[hardQuestionOrder[x]]
                  
                case"b":
                        userInput = answer2[hardQuestionOrder[x]]
                  
                case "c":
                        userInput = answer3[hardQuestionOrder[x]]
                  
                case "d":
                        userInput = answer4[hardQuestionOrder[x]]
               
              if userInput == correctAnswer[hardQuestionOrder[x]]:
                   print("you got the question right")
                   score += 1
              
              else:
                 print('you got the question wrong')
              
         print(f"well done you have finished the quiz and have scored {score} out of 10")