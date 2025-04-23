from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizUi:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Score Label
        self.score_label = Label(self.window, text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0)

        # Question Label
        self.q_label = Canvas(self.window, width=300, height=250, bg="white", highlightthickness=0)
        self.q_text = self.q_label.create_text(
            150,
            125,
            width=280,
            text="Amazon acquired Twitch in August 2014 for $970 million dollars.",
            fill=THEME_COLOR,
            font=("Arial", 15, "italic"),
        )
        self.q_label.grid(column=0, row=1, columnspan=2, pady=20)

        # Buttons
        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=1, row=2, pady=20)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=0, row=2, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.q_label.config(bg="white")
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q = self.quiz.next_question()
            self.q_label.itemconfig(self.q_text, text=q)
        else:
            self.q_label.itemconfig(self.q_text, text="Finish")
            self.q_label.config(bg="white")
            self.true_button.config(state=DISABLED)
            self.false_button.config(state=DISABLED)

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        print(is_right)
        if is_right == True:
            self.q_label.config(bg="green")
        else:
            self.q_label.config(bg="red")
        self.window.after(1000, self.get_next_question)



