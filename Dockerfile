# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the rest of the application code into the working directory
COPY . .

# Define the command to run the application
CMD ["python", "udp_flood_test.py"]
