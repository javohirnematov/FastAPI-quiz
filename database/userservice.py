from datetime import datetime

from database import get_db
from database.models import User, UserAnswer, Rating


# Регистрация
def register_user_db(name: str, phone_number: str) -> int:
    # сгенерировать подключение
    db = next(get_db())

    # получить определенного пользователя
    exact_user = db.query(User).filter_by(phone_number=phone_number).first()

    # если есть пользователь в базе, то мы отправляем id пользователя
    if exact_user:
        return exact_user.id

    # если пользователь не найден в базе
    else:
    # Регистрируем
        new_user = User(name=name,
                        phone_number=phone_number,
                        reg_date=datetime.now())

        # Добавляем в базу
        db.add(new_user)

        # сохраняем изменения в базе
        db.commit()

        # запись в таблицу рейтинга
        score_table = Rating(user_id=new_user.id)
        db.add(score_table)
        db.commit()

        return new_user.id



# Вывод результатов
def get_user_score_db(user_id: int) -> int:
    db = next(get_db())

    # проверить есть ли пользователь в базе
    checker = db.query(UserAnswer).filter_by(user_id=user_id, correctness=True)

    if checker:
        return len(checker)

    return 0


# Вывод таблицы лидеров
def show_leaders_db() -> list:
    db = next(get_db())

    rating = db.query(Rating).order_by(Rating.user_score.desc()).all()

    return rating[:5]


# Записи результатов в базу
def add_user_answer_db(user_id: int, question_id: int, user_answer: int, correctness: bool) -> bool:
    db = next(get_db())
    new_user_answer = UserAnswer(user_id=user_id, question_id=question_id,
                                 user_answer=user_answer, correctness=correctness,
                                 answer_date=datetime.now())

    # Если ответил правильно на вопрос, то увеличить рейтинг
    exact_user_score = db.query(Rating).filter_by(user_id=user_id).first()
    if correctness:
        print(exact_user_score.user_fk.name)
        exact_user_score.user_score += 1

    else:
        exact_user_score.user_score -=1

    db.add(new_user_answer)
    db.commit()

    return True if correctness else False
