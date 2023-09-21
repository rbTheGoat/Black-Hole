from quiz import Questions, Quiz
from question import question_data

if __name__ == "__main__":
    question_list = [Questions(q["text"], q["answer"]) for q in question_data]
    quiz = Quiz(question_list)
    quiz.start_quiz(60)
