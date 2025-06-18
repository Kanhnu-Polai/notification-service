# Use official lightweight Python image
FROM python:3.11-slim

# Set working directory in container
WORKDIR /app

# Copy dependency file and install requirements
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code into the container
COPY . .

# Expose the port your app runs on (adjust if needed)
EXPOSE 5000

# Run the main application
CMD ["python", "run.py"]