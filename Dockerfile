# Base image with Python 3.10 + NodeJS 20
FROM nikolaik/python-nodejs:python3.10-nodejs20

# Install system dependencies (ffmpeg + git for pip installs)
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg git \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir --upgrade -r requirements.txt

# Start the bot directly (works for Render background worker)
CMD ["python3", "-m", "SHUKLAMUSIC"]
