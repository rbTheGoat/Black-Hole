import random
import time
from question import question_data

class Questions:
    def __init__(self,text,answer):
        self.text= text
        self.answer = answer

class Quiz:
    def __init__(self,question_list):
        self.question_list = question_list
        self.remaining_questions = list(question_list)
        self.score = 0
    
    def get_next_question(self):
        if len(self.remaining_questions)!= 0:
            return self.remaining_questions.pop(0) 
        else:
            return None
        
    def check_answer(self,question,user_answer):
        if question.answer == user_answer:
            self.score += 2
        else:
            self.score -= 1

    def start_quiz(self,time_limit):
        print("Welcome to this Quiz show!")
        print("You have", str(time_limit), "seconds to complete the quiz!!!!")
        start_time = time.time()

        while True:
            time_elapsed = time.time()-start_time
            if time_elapsed >= time_limit:
                print("BEEEEEP! Time's up, You took too long. :( ")
                break

            current_question = self.get_next_question()
            if current_question is None:
                break

            print("\nQuestion")
            print(current_question.text)
            user_answer = input("Enter 'True' or 'False': ")
            user_answer = user_answer.strip()
            user_answer = user_answer.capitalize()

            if user_answer == "True" or user_answer == "False":
                self.check_answer(current_question,user_answer)
            else:
                print("Invalid input! Please enter only 'True' or 'False'.")
            
        print("\nTime for the Quiz results")
        round_score = round(self.score / len(self.question_list), 1)
        print("Your score was:", round_score)
        print("Thank you for playing!")
