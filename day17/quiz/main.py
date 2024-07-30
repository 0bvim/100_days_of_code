from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = [Question(item["text"], item["answer"]) for item in question_data]

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
	quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(quiz.questions_list)} ")

