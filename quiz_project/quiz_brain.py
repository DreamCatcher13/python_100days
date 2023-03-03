class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_q = self.question_list[self.question_number].text
        answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_q} (True/False)?: ")
        self.check_answer(user_answer, answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_ans, correct_ans):
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            print("You are right!")
        else:
            print("You are wrong!")
        print(f"The right answer was: {correct_ans}")
        print(f"Your score is {self.score}/{self.question_number}\n")
        


        
