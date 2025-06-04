FROM nikolaik/python-nodejs:python3.11-nodejs16-bullseye

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .


RUN python manage.py tailwind build

ENV PYTHON_ENV production
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]