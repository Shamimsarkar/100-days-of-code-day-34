from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brian: QuizBrain):
        self.quiz = quiz_brian

        self.window = Tk()
        self.window.title("Quiz Game")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text= "Score: 0", background=THEME_COLOR, font=("Arial", 20, "bold"), fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, background="white")
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Question to be show here", font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        false_image = PhotoImage(file="images/false.png")
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_press)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_press)
        self.false_button.grid(row=2, column=1)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text =q_text)
        else:
            self.canvas.itemconfig(self.question_text, text= "There is no more question remain.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_press(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_press(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_ture):
        if is_ture:
            self.canvas.config(bg="green")

        else:
            self.canvas.config(bg="red")
        self.window.after(100, self.get_next_question)


