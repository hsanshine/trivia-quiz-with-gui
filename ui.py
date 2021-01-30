from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"  # midnight blue


class QuizInterface:
    '''will be the class that creates the quiz interface window when an object is created'''

    def __init__(self, quiz: QuizBrain):
        # init will be called each time a new object is created from this class and all that is here will happen\
        self.quiz = quiz
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=250,
            text='question goes here',
            font=('Arial', 20, 'italic')
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        self.questions_number_label = Label(
             text=f'No. of questions: {len(self.quiz.question_list)}',
            font=('Arial', 12, 'normal'),
            fg='white',
            bg=THEME_COLOR
        )
        self.questions_number_label.grid(column=0, row=0, padx=20, pady=20)

        self.score_label = Label(
            text=f'Score : {0}',
            font=('Arial', 12, 'normal'),
            fg='white',
            bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0, padx=20, pady=20)
        self.score_text = None

        right_image_img = PhotoImage(file='./images/true.png')
        wrong_image_img = PhotoImage(file='./images/false.png')

        self.right_button = Button(image=right_image_img, highlightthickness=0, command=self.true_pressed)
        self.right_button.grid(column=0, row=2)

        self.wrong_button = Button(image=wrong_image_img, highlightthickness=0, command=self.false_pressed)
        self.wrong_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()  # infinite while loop that listens for events in the window

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_text = f'Score: {self.quiz.score} / {self.quiz.question_number+1}'
            self.score_label.config(text=self.score_text)

            q_text = self.quiz.next_question()  # call this method from the quiz_object to give us the next question instead
            # of printing it on the screen before. we get this question from this quiz object and print in the GUI
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text=f'Quiz is finished!\n  {self.score_text}')
            self.right_button.config(state='disabled')
            self.wrong_button.config(state='disabled')

    def true_pressed(self):  # check answer already knows the current question and is just waiting for your answer
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000, self.get_next_question)
        # self.window.after(1000, self.canvas.config(bg='white')) # if you put a command here with parenthesis, it will
        # be called immediately this line is reached, not after 1000 seconds, so you must put only the name of the fun
        # don't put it with parenthesis, it will be called right away which you dont want
