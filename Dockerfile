FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install dependencies
RUN apt-get update && apt-get install -y \
    wget \
    unzip \
    xvfb \
    libnss3 \
    libxss1 \
    libappindicator3-1 \
    libgbm1 \
    libasound2 \
    fonts-liberation \
    libgtk-3-0 \
    && apt-get clean

# Install Chrome and Chromedriver
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i google-chrome-stable_current_amd64.deb || apt-get -f install -y \
    && rm google-chrome-stable_current_amd64.deb

RUN wget -q https://chromedriver.storage.googleapis.com/$(wget -q -O - "https://chromedriver.storage.googleapis.com/LATEST_RELEASE")/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/local/bin \
    && rm chromedriver_linux64.zip

# Install Python dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy bot files
WORKDIR /app
COPY . /app

# Run the bot script
CMD ["python", "runbots.py"]
