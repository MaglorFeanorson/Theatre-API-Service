FROM python:3.11.9-alpine3.18.6
LABEL maintainer="daniilrog17@gmail.com"

ENV PYTHONNBUFFERED=1

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]