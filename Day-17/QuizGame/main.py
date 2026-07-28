from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for ques in question_data:
    ques_text = ques["text"]
    ques_ans = ques["answer"]
    new_question = Question(q_text=ques_text , q_answer=ques_ans)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.q_number}")