# указываем язык программирования
FROM python:3.10

#
WORKDIR /quiz

# копировать все папки/файлы в Докер
COPY . /quiz

# установка необходимых компонентов
RUN pip install -r requirements.txt

# команда для запуска
CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--port=8000"]
