# Используем официальный образ Python 3.12 как базовый образ
FROM python:3.12

# Устанавливаем необходимые пакеты
RUN apt-get update && apt-get install -y build-essential

# Устанавливаем необходимые Python библиотеки
RUN pip install sentence-transformers chromadb fastapi sentence_transformers pydantic uvicorn 

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем рабочую директорию в /app
WORKDIR /app

# Устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Устанавливаем команду для запуска приложения
CMD ["python", "./src/main.py"]
