# Use Python Official Image as Base
FROM python:3

# Create a working directory
WORKDIR /app

# Copy all files from Build Context (folder) to Working Directory
COPY . .

# Install required Libraries & Modules
RUN pip install -r requirements.txt

# Start-up Command (same as gunicorn --bind=0.0.0.0:8000 --workers=1 chocolates:app)
CMD ["gunicorn", "--workers=1", "--bind=0.0.0.0:5000", "chocolates:app"]
