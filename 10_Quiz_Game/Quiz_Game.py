import random
import quiz_art as art

class Quiz:
    ques_no=0
    score=0
    question=""
    allready_ask=[]

    def ask_question(self):
        self.question=random.choice(art.question_data)
        if self.score==0:
            self.allready_ask.append(self.question["number"])
            return 

        while self.question["number"] in self.allready_ask:
            self.question=random.choice(art.question_data)

        self.allready_ask.append(self.question["number"])
        return 

    def check_answer(self,user_answer):
        correct_answer=self.question["answer"]
        if user_answer==correct_answer:
            self.score+=1
            print("Your answer is Correct.")

        else:
            print("Your answer is Wrong.")

        print(f"Correct Answer is : {correct_answer.capitalize()}")
        print(f"Your Current Score is :{self.score}/{self.ques_no}")

    def display_question(self):
        self.ask_question()
        self.ques_no+=1
        user_answer=input(f"\nQ{self.ques_no}. {self.question['question']} [True or False] : ").capitalize()
        self.check_answer(user_answer)


ob=Quiz()
print(art.logo)
gameover=False

while not gameover:
    if len(ob.allready_ask)!=12:
        ob.display_question()
        if ob.score==12:
            print(f"\nCongratulation You Win the Game. Your Score is {ob.score}/{ob.ques_no}")
            gameover=True
    else:
        print(f"\nQuiz Game is Completed. Your Score is {ob.score}/{ob.ques_no}")
        gameover=True