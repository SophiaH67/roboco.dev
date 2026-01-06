FROM nikolaik/python-nodejs:python3.12-nodejs22-bookworm

ENV PYTHON_ENV production
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN python manage.py tailwind build
RUN python manage.py collectstatic --no-input

EXPOSE 8000

CMD ["gunicorn", "roboco.wsgi", "--bind", "0.0.0.0:8000", "--log-level", "debug", "--error-logfile", "-", "--access-logfile", "-", "--capture-output"]