FROM python:3.11-slim

WORKDIR /app

RUN pip install flask

COPY app.py .

RUN mkdir -p /app/collected

EXPOSE 8666

CMD ["python", "app.py"]
