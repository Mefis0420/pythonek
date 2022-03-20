import random
import os
import time
clear = lambda: os.system('cls')
clear()
time.sleep(1.1)
newgame = 1
points = 0
###QUESTIONS
q1question = ("Who is The chosen one?")
q2question = ("Who is The most known captain of 501st legion")
q3question = ("Whats the name of Green Ogr Jedi general")
q4question = ("Who is The Dual Lighstaber owner from prequels")
q5question = ("Have Anakin married Padme?")
q6question = ("How old anakin is in Atack of Clones")
q7question = ("Number of null-arc troopers")
q8question = ("Number of 'sith' word uses in Original Trilogy ")
q9question = ("Whats the name of CT-1004 Commandor ")
###RIGHT ANSWERS
q1rightanswer = ("Anakin Skywalker")
q1ranswerforstupidpeoples = ("anakin skywalker")
q2rightanswer = ("Rex")
q2ranswerforstupidpeoples = ("rex")
q3rightanswer = ("Yoda")
q3ranswerforstupidpeoples = ("yoda")
q4rightanswer = ("Darth Maul")
q4ranswerforstupidpeoples = ("darth maul")
q5rightanswer = ("Yes")
q5ranswerforstupidpeoples = ("yes")
q6rightanswer = ("19")
q6ranswerforstupidpeoples = ("nineteen")
q7rightanswer = ("12")
q7ranswerforstupidpeoples = ("12")
q8rightanswer = ("0")
q8ranswerforstupidpeoples = ("zero")
q9rightanswer = ("Gree")
q9ranswerforstupidpeoples = ("gree")
###EASTER EGGS
q3afuckyou = ("your mom")
### end of questions
print("Welcome to Star Wars knowledge test")
playername = input(" Whats your name? ")
clear()
while newgame == 1:
    newgame = 0
    level = input(" Select mode \n easy | Medium | Hard | :")
### easy mode start
    if level == "easy" or level == "Easy":
        print("Easy mode?! For real? Damn bro why u do this to me :( ")
        print(q1question)
###first one
        q1answer = input(" Whats your answer? ")
        if q1answer == q1rightanswer or q1answer == q1ranswerforstupidpeoples:
            print("Great your answer was correct, IT SHALL BE COZ YOU PICKED THE EASY MODE BASTARD")
            points = points + 1
        else:
            print("wtf man XDDD why you so stupid")
        time.sleep(4.0)
        clear()
        print(q2question)
###second one
        q2answer = input(" Whats your answer? ")
        if q2answer == q2rightanswer or q2answer == q2ranswerforstupidpeoples:
            print("Great your answer was correct again")
            points = points + 1
        else:
            print("to be honest, u should leave.. Like now before i beat your ass up")
        time.sleep(4.0)
        clear()
        print(q3question)
###third one
        q3answer = input(" Whats your answer? ")
        if q3answer == q3rightanswer or q3answer == q3ranswerforstupidpeoples:
            print("You passed This question, but still shall not be proud of yourself")
            points = points + 1
        elif q3answer == q3afuckyou:
            print("No, yours")
            exit()
        else:
            print("You are joking right? Thats hell nah funny mate")
        time.sleep(4.0)
        clear()
###points
        print("Your score is: ",points)
        if points == 0:
            print("Your amount of points is similar to you, you are also a living zero.")
        if points == 1:
            print("it could be worse, you are still an idiot")
        if points == 2:
            print("thats still not good score go away")
        if points == 3:
            print("You passed the stupidity test, now go pass the medium mode, dont be pussy")
### easy mode end
### mid mode start
    if level == "Medium" or level == "medium":
        print("So medium mode right? lets start ")
        print(q4question)
###first one
        q4answer = input(" Whats your answer? ")
        if q4answer == q4rightanswer or q4answer == q4ranswerforstupidpeoples:
            print("Correct one, good job")
            points = points + 5
        else:
            print("Good luck next time mate")
        time.sleep(4.0)
        clear()
        print(q5question)
###second one
        q5answer = input(" Whats your answer? ")
        if q5answer == q5rightanswer or q5answer == q5ranswerforstupidpeoples:
            print("Another one! great")
            points = points + 5
        else:
            print("Try Harder!")
        time.sleep(4.0)
        clear()
        print(q6question)
###third one
        q6answer = input(" Whats your answer? ")
        if q6answer == q6rightanswer or q6answer == q6ranswerforstupidpeoples:
            print("You succesfull passed This question")
            points = points + 5
        else:
            print("Ok i googled it also")
        time.sleep(4.0)
        clear()
                        ###points
        print("Your score is: ",points)
        if points == 0:
            print("Your amount of points is similar to you, you are also a living zero.")
        if points == 5:
            print("its ok, dont cry")
        if points == 10:
            print("medium mode medium points, good one")
        if points == 15:
            print("well done soldier u may be prouf of yourself!!")
### mid mode end
### mid mode start
    if level == "Hard" or level == "hard":
        print("lets burn the hell ")
        print(q7question)
###first one
        q7answer = input(" Whats your answer? ")
        if q7answer == q7rightanswer or q7answer == q7ranswerforstupidpeoples:
            print("You got lucky.")
            points = points + 50
        else:
            print("maybe you should go back to medium mode?")
        time.sleep(4.0)
        clear()
        print(q8question)
###second one
        q8answer = input(" Whats your answer? ")
        if q8answer == q8rightanswer or q8answer == q8ranswerforstupidpeoples:
            print("wait what?! UR NOT SUPOSED TO BE THAT GOOD")
            points = points + 50
        else:
            print("okay, thats normal who the fuck would know it")
        time.sleep(4.0)
        clear()
        print(q9question)
###third one
        q9answer = input(" Whats your answer? ")
        if q9answer == q9rightanswer or q9answer == q9ranswerforstupidpeoples:
            print("HELL NAH YOUR A LIVING DATABASE MAN")
            points = points + 50
        else:
            print("That one was hard dont be mad")
        time.sleep(4.0)
        clear()
                        ###points
        print("Your score is: ",points)
        if points == 0:
            print("life is hard, those questions are such worse")
        if points == 50:
            print("you got lucky but still better than Easy mode pussies")
        if points == 100:
            print("woah, you may be the real choosen one")
        if points == 150:
            print("you just googled it, dont you?")
    end = input("| Again | exit  | :")
    if end == "Again" or "again":
        print("less go")
        newgame = 1
        clear()
exit()
### hard mode end
