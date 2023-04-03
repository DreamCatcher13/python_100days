from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

question_bank = []
#for i in range(len(question_data)):
for q in question_data:
    question_bank.append(Question(q['question'], q['correct_answer'] ))

#print(question_data)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)





