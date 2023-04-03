from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
#for i in range(len(question_data)):
for q in question_data:
    if "&quot;" in q['question']:
        q['question'] = q['question'].replace("&quot;", "\"")
    if "&#039;" in q['question']:
        q['question'] = q['question'].replace("&#039;", "'")
    question_bank.append(Question(q['question'], q['correct_answer'] ))

#print(question_data)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"""Congrats! You finished the quiz.
You final score is: {quiz.score}/{len(quiz.question_list)}""")



