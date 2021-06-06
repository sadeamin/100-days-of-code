class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_number].text
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {question} (True/False)?: ")

        self.check_answer(user_answer=user_answer, correct_answer=self.question_list[self.question_number-1].answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")

        else:
            print("That's wrong.")

        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is : {self.score}/{self.question_number}")
        print("\n")
