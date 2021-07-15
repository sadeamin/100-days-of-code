from tkinter import *
from quiz_brain import QuizBrain

# from tkinter import *
# from Intermediate.day_34.quiz_brain import QuizBrain


THEME_COLOR = "#343637"
class QuizInterface():
    def __init__(self, quiz_brain : QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=(24))
        self.score_label.grid(row=0, column=1, pady=5)

        self.canvas = Canvas(height=250, width=300)
        self.quesion_text = self.canvas.create_text(150, 125, width=280, text="THIS IS THE TEXT", font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2)
        
        self.wrong_img = PhotoImage(file="Intermediate/day_34/images/false.png")
        
        self.right_img = PhotoImage(file="Intermediate/day_34/images/true.png")

        # self.wrong_img = PhotoImage(file="images/true.png")

        # self.right_img = PhotoImage(file="images/false.png")

        self.button_right = Button(image=self.right_img, highlightthickness=0, command=self.right)
        self.button_right.grid(row=2, column=0, pady=30)
        
        self.button_wrong = Button(image=self.wrong_img, highlightthickness=0, command=self.wrong)
        self.button_wrong.grid(row=2, column=1, pady=30)
        
        self.get_next_question()
        
        self.window.mainloop()

    def get_next_question(self):
        
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score = self.quiz.score
            self.score_label.config(text=f"score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.quesion_text, text=q_text)
        else:
            self.canvas.itemconfig(self.quesion_text, text="You've reached the end of the quiz.")
            self.button_right.config(state="disabled")
            self.button_wrong.config(state="disabled")
        
    def right(self):
        self.give_feedback(self.quiz.check_answer("True"))


    
    def wrong(self): 

        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)


    def give_feedback(self, is_right):
        if is_right:

            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)