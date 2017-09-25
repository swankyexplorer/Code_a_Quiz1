import time
from time import sleep #time to the "new start" after lost or won game
#Introduction:
name = raw_input("Hello, F1 Fan! What's your name? ") #Basic raw_input of the user name
intro = "Welcome to my Formula 1 quiz " + name + "!"  #displays text plus value of "name"
note = "Make sure all inputs are in lowercase"
print intro #prints Welcome message "intro"
print note #prints notification message "note"

blanks = ["__1__","__2__","__3__", "__4__"] #defines number of blanks to fill out in the quiz
answers = blanks

questions_rookie = '''\nFormula One is the __1__ class of single-seat auto
racing that is sanctioned by the FIA. The "__2__", designated in the name,
refers to a set of __3__, to which all participants' cars must __4__.\n'''
#question option for level "rookie"

questions_pro = '''\nThe F1 season consists of a series of races, known as
__1__, held worldwide on purpose-built F1 __2__ and several events in city
centres throughout the world. Some city races currently the calendar: night
race in __3__, new circuit in Baku and the __4__ Grand Prix being the most
well-known among them.\n''' #question option for level "pro"

questions_champ = '''\nThe cars are very dependent on __1__ (although __2__
control and other driving aids have been banned since 2008) and also on __3__,
suspension, and __4__. The formula has radically evolved and changed through
the history of the sport since the inaugural season in 1950.\n'''
#question option for level "champ"

#list of correct answers for level "rookie"
answers_rookie = ["highest", "formula", "rules", "obey"]
#list of correct answers for level "pro"
answers_pro = ["grand prix", "circuits", "singapore", "monaco"]
#list of correct answers for level "champ"
answers_champ = ["electronics", "traction", "aerodynamics", "tyres"]

#definition of the 3 senarios with the display messages upon selection
quiz_data = {
   'rookie': {
        'quiz': questions_rookie,
        'answers': answers_rookie,
        'message': "Rookie! Well, they say you crawl 'fore you walk! Good luck!"
    },
   'pro': {
        'quiz': questions_pro,
        'answers': answers_pro,
        'message': "Pro! A brave start! Good luck!"
    },
   'champ': {
        'quiz': questions_champ,
        'answers': answers_champ,
        'message': "Champ! Quite an adventurous! Good luck!"
    }
}

#Input of the quiz level: rookie, pro or champ. Output is relevant questions and answers.
def get_level():
    """
    get_level() returns quiz level
    inputs: rookie, pro or champ.
    outputs: if correct prints the message relevant to the quiz level.
    If incorrect asks to repeat the input.
    """
    quiz_level = raw_input("Choose your difficulty level: rookie, pro or champ: ")
    while quiz_level not in ["rookie", "pro", "champ"]:
        quiz_level = raw_input("Incorrect input, please try again. Choose from: rookie, pro or champ: ")
    print quiz_data[quiz_level]['message']
    return quiz_level


#checking the answers: inputs - users answers, output - False or Correct
def check_answer(user_answer, answers_list, answers_index):
    """
    Checking the answers:
    Inputs - users answers, Output - False or Correct
    see play_game
    """
    if user_answer == answers_list[answers_index]:
        return "correct_answer"
    return "False"
    pass

def you_lost(): #output for the "Lost game"
    print "Ahh, you lost... Have a pit stop and try again!"
    time.sleep (3)
def you_win(): #output for teh "Win game"
    print "Checkered Flag!!! You are a winner!"
    time.sleep (3)


def play_game(): #full game scenario set up
    """
    Input: level, Output: questions for chosen level and answers for the same
    """
    level = get_level()
    quiz = quiz_data[level]['quiz']
    print quiz
    answers_list =  quiz_data[level]['answers']
    answers_index = 0
    guesses = 3

#1 def set_up_quiz(play_game): #helper function (for the play_game) to simplify the code.
#     return play_game
    set_up_quiz = play_game()
    print set_up_quiz
    while answers_index < len(answers):
        """
        Checking if teh anwer is correct.
        Input: answers, Output: message according to correct or wrong answer.
        If wrong, asks to try once again and shows number of guesses left.
        """
        user_answer = raw_input("And the answer for " + answers[answers_index] + " is?:")
        if check_answer(user_answer,answers_list,answers_index) == "correct_answer":
            print "Well done! Correct!"
            quiz = quiz.replace(answers[answers_index], user_answer.upper())
            answers_index += 1
            guesses = 3
            print quiz
            if answers_index == len(answers):
                return you_win()

        else:
            guesses -= 1
            if guesses == 0:
                return you_lost()
                break
            print "Not quite!!! You've got " + str (guesses) + " guesses left!"




play_game()
#while working on this project I have used some references from GitHub and forum.
