# Используем официальный Python образ
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем системные зависимости для PostgreSQL
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Копируем файл зависимостей
COPY requirements.txt .

# Устанавливаем Python зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь проект
COPY jobparser/ .

# Собираем статические файлы (будет выполнено при запуске)
# Создаем директорию для статических файлов
RUN mkdir -p /app/staticfiles

# Устанавливаем переменные окружения
ENV PYTHONUNBUFFERED=1
ENV PYTHONIOENCODING=utf-8
ENV DJANGO_SETTINGS_MODULE=jobparser.settings

# Открываем порт
EXPOSE 8000

# Команда по умолчанию (будет переопределена в docker-compose)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

