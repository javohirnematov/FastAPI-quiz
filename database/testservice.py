from datetime import datetime

from database.models import Question
from database import get_db


# Добавление вопросов
def add_question_db(q_text, answer, v1, v2, v3=None, v4=None):
    db = next(get_db())
    new_question = Question(q_text=q_text, answer=answer,
                            v1=v1, v2=v2, v3=v3, v4=v4, reg_date=datetime.now())
    db.add(new_question)
    db.commit()

    return 'вопрос добавлен в базу данных'


# Функция получения вопросов (20 штук)
def get_20_questions_db():
    db = next(get_db())
    all_questions = db.query(Question).all()

    return all_questions[:20]
