from question_model import Question
from data import question_data1
from quiz_brain import QuizBrain

question_bank=[]
l1 = question_data1["results"]


for ques in l1:
    question_text = ques["question"]
    question_ans = ques["correct_answer"]
    new_question = Question(question_text, question_ans)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print("You have completed your quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")