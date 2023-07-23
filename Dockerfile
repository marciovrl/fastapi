# Use an official Python slim-buster image
FROM python:3.8-slim-buster

# Set work directory
WORKDIR /src

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./requirements.txt /src/requirements.txt
RUN pip install --no-cache-dir -r /src/requirements.txt

# Copy the app code
COPY ./app /src/app

# Set the default command to run the FastAPI server using uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

