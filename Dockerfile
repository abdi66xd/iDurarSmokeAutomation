FROM python:3.12.3

# Instalar dependencias necesarias para Chrome y ChromeDriver
RUN apt-get update && apt-get install -y wget gnupg unzip

# Descargar e instalar Chrome
RUN wget -q -O /tmp/google-chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i /tmp/google-chrome.deb || apt-get -fy install \
    && rm /tmp/google-chrome.deb

# Descargar e instalar ChromeDriver
RUN CHROMEDRIVER_VERSION=$(curl -sS https://chromedriver.storage.googleapis.com/LATEST_RELEASE) \
    && wget -q -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROMEDRIVER_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/bin \
    && rm /tmp/chromedriver.zip \
    && chmod +x /usr/bin/chromedriver

WORKDIR /app

COPY requirements.txt .
COPY features ./features
COPY configurations ./configurations
COPY utilities ./utilities

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["behave"]
