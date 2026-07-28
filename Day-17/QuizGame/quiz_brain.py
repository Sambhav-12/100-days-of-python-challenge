class QuizBrain:
    def __init__(self, q_list):
        self.q_number = 0
        self.list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.q_number < len(self.list)

    def next_question(self):
        current_question = self.list[self.q_number]
        self.q_number += 1
        user_ans = input(f"Q.{self.q_number}: {current_question.text} (True/False): ")
        self.check_ans(user_ans, current_question.answer)

    def check_ans(self, user_ans, correct_answer):   
        if user_ans.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}.")
        print(f"Your current score is: {self.score}/{self.q_number}")
        print("\n" * 3)
