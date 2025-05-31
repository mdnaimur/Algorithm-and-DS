# Use Python base image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy the project files to container
# COPY . /app
COPY . .

# Install dependencies (if any)
# COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Default command
CMD ["python", "main.py"]
