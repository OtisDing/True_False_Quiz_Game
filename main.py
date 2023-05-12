from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

questionBank = []

for question in question_data:
    qText = question["question"]
    qAnswer = question["correct_answer"]
    newQuest = Question(qText, qAnswer)
    questionBank.append(newQuest)

quiz = QuizBrain(questionBank)


while quiz.stillHasQuestions():
    quiz.nextQuestion()

print("Congratulations! You've completed the quiz.")
print(f"Your final score was: {quiz.score}/{quiz.questionNumber}")
