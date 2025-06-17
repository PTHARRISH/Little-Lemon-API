FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY Pipfile Pipfile.lock* /app/
RUN pip install pipenv && pipenv install --system

COPY . /app/

# Optional: collect static files (you can remove if not needed)
RUN python LittleLemon/manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["gunicorn", "LittleLemon.wsgi:application", "--chdir", "LittleLemon", "--bind", "0.0.0.0:8000"]
