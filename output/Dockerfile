# Use the latest official Python runtime as a parent image
FROM python:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy only the necessary files
COPY ./merge_csv.py ./requirements.txt ./

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Run merge_csv.py when the container launches
CMD ["python", "./merge_csv.py"]
