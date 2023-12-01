# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Ensure the package database is up to date
RUN apt-get update

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run solution.py when the container launches
CMD ["python", "./solution.py"]
