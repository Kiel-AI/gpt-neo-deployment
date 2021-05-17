FROM python:3.9.5-slim-buster

WORKDIR /app

COPY . .

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["opyrator", "launch-ui", "app:generate_text", "--port", "8000"]