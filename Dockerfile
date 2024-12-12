# Dockerfile

# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script into the container
COPY fibonacci.py .

# Install any dependencies (none in this case, but you could add them here)
# RUN pip install -r requirements.txt  # Uncomment this if you have a requirements file

# Command to run the Python script
CMD ["python", "fibonacci.py"]
