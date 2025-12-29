# 1. Base image (Python runtime)
FROM python:3.10-slim

# 2. Set working directory inside container
WORKDIR /app

# 3. Copy dependency file first (for caching)
COPY requirements.txt .

# 4. Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the rest of the project files
COPY . .

# 6. Expose Flask port
EXPOSE 5000

# 7. Run the Flask app
CMD ["python", "app/app.py"]

