# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем системные зависимости
RUN apt-get update && apt-get install -y \
    wget \
    bzip2 \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /miniconda.sh && \
    bash /miniconda.sh -b -p /opt/conda && \
    rm /miniconda.sh && \
    /opt/conda/bin/conda init bash

# Добавляем Miniconda в PATH
ENV PATH=/opt/conda/bin:$PATH

# Копируем файл environment.yml
COPY environment.yml /tmp/environment.yml

# Создаем виртуальное окружение и устанавливаем Python-зависимости
RUN conda env create -f /tmp/environment.yml && conda clean -a

# Проверяем установленные зависимости
RUN /opt/conda/envs/pythontest3_env/bin/pip list | grep "Django\|python-dotenv"

# Устанавливаем Node.js и npm
RUN curl -fsSL https://deb.nodesource.com/setup_18.x | bash - && apt-get install -y nodejs

# Копируем package.json в контейнер
COPY package.json /app/package.json

# Удаление кеша npm и старых данных
RUN npm cache clean --force && rm -rf node_modules package-lock.json

# Устанавливаем JavaScript-зависимости
WORKDIR /app
RUN npm install

# Копируем все файлы проекта
COPY . /app

# Указываем порт приложения
EXPOSE 8000

# Запуск Django-сервера
CMD ["/opt/conda/envs/pythontest3_env/bin/python", "manage.py", "runserver", "0.0.0.0:8000"]
