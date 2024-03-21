# Use the official Python image as the base image
FROM python:3.12

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from the current directory into the container
COPY . .

# Set environment variables
ENV PYTHONUNBUFFERED 1

# Run the Python script
CMD ["python", "whisper.py"]
