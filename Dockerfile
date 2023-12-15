FROM python:3.10-slim

EXPOSE 8000

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
