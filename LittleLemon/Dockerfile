# Use official Python 3.11 slim image
FROM python:3.11-slim

# Set environment variables to prevent Python from writing pyc files and buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install OS-level dependencies (gcc, libpq-dev for psycopg2 or similar packages)
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the whole project into the container
COPY . /app/

# Upgrade pip and install Python packages
RUN pip install --upgrade pip
RUN pip install -r LittleLemon/requirements.txt

# Expose the port that Django will run on
EXPOSE 8000

# Start Django development server
CMD ["python", "LittleLemon/manage.py", "runserver", "0.0.0.0:8000"]
