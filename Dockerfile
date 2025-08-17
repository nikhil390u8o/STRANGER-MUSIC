# Base image with Python 3.10 + NodeJS 20
FROM nikolaik/python-nodejs:python3.10-nodejs20

# Install ffmpeg (required for music streaming)
RUN apt-get update \
    && apt-get install -y --no-install-recommends ffmpeg \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir --upgrade pip \
    && pip3 install --no-cache-dir --upgrade -r requirements.txt

# Start the bot directly (no ports needed, works as Render background worker)
CMD ["python3", "-m", "SHUKLAMUSIC"]
