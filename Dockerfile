# Use python base image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy files
COPY . .

# Install dependencies (flask)
RUN pip install flask

# Command to run on container start
CMD ["python", "app.py"]