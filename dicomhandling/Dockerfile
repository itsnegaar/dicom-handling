FROM python:3.11-slim

LABEL authors="negar"

# Set the working directory in the container
ENV PYTHONUNBUFFERED 1
RUN pip3 install --upgrade pip
RUN mkdir /app
WORKDIR /app

COPY requirements.txt .


RUN pip3 --timeout=5000 install --no-cache-dir -r ./requirements.txt

# Copy the project files into the container
COPY . .

# Expose the port the app runs on
EXPOSE 8000
