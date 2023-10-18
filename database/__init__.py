# Шаблон базы данных для любого проекта (для всех)

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Ссылка на базу данных
# SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'                                          # Это база на SQLite следующее на POSTGRES
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@database/postgres'             # database название берем из docker-compose 5 строчка

# Подключение к базе
engine = create_engine(SQLALCHEMY_DATABASE_URI)

# Соединение с базой
SessionLocal = sessionmaker(bind=engine)

# Класс для наследования в таблицах
Base = declarative_base()

# Импорт всех моделей
from database import models


# генератор соединений к базе
def get_db():
    db = SessionLocal()
    try:
        yield db

    except Exception:
        db.rollback()
        raise

    finally:
        db.close()

