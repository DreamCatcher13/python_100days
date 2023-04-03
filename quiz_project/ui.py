from tkinter import *
from quiz_brain import QuizBrain # so our program can understand the data type

THEME_COLOR = "#375362"
FONT = ("Arial", 15, "italic")

class QuizInterface():
    
    def __init__(self, quiz_brain: QuizBrain): #we tell everyone that parameter quiz_brain should be of class QuizBrain
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: ", fg="white", bg=THEME_COLOR, font=("Arial", 15))
        self.score_label.grid(column=2, row=1)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question = self.canvas.create_text(150, 125, width=200, font=FONT, fill="black")
        self.canvas.grid(column=1, row=2, columnspan=2, pady=50)
        # self means property and we can access it everywhere; but we don't need to access images elsewhere
        true_img = PhotoImage(file="images/true.png")
        self.true_b = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_b.grid(column=1, row=3)

        false_img = PhotoImage(file="images/false.png")
        self.false_b = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_b.grid(column=2, row=3)  

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score} / 10")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text )
        else:
            self.canvas.itemconfig(self.question, text="Congrats! You finished the quiz.")
            self.true_b.config(state="disabled")
            self.false_b.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)


