# Use a lightweight Python base image
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PIP_NO_CACHE_DIR=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install pipenv and dependencies
COPY Pipfile Pipfile.lock* /app/
RUN pip install --upgrade pip pipenv && pipenv install --system --deploy --ignore-pipfile

# Copy project files
COPY . /app/

# Collect static files (optional but recommended for Django)
RUN python LittleLemon/manage.py collectstatic --noinput || true

# Expose the port Gunicorn will run on
EXPOSE 8000

# Start the Gunicorn server
CMD ["gunicorn", "LittleLemon.wsgi:application", "--chdir", "LittleLemon", "--bind", "0.0.0.0:8000"]
