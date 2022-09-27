from question_model import Question
# from data import question_data as qd
from data import Data
from quiz_brain import QuestionBrain

qbank = []

data = Data()
data.create()

for i in data.question_data:
    # print(i)
    q = Question(i['text'], i['answer'],)
    qbank.append(q)

quiz = QuestionBrain(qbank)

print('\n\n\n')
while quiz.still_have_question():
    quiz.nextQuestion()

quiz.finish()