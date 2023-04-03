import html

class QuizBrain():

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.current_question = None

    def next_question(self):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.current_question.text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {self.current_question.text}"
 #       user_answer = input(f"Q.{self.question_number}: {current_q} (True/False)?: ")
 #       self.check_answer(user_answer, answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
    
    def check_answer(self, user_ans):
        correct_ans =  self.current_question.answer
        if user_ans.lower() == correct_ans.lower():
            self.score += 1
            return True
        else:
            return False
        


        
