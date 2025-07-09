FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    chromium \
    chromium-driver \
    wget \
    unzip \
    python3-pip \
    fonts-liberation \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libdrm2 \
    libxkbcommon0 \
    libgtk-3-0 \
    libgbm1 \
    libx11-xcb1 \
    libxcomposite1 \
    libxdamage1 \
    libxrandr2 \
    xdg-utils \
    --no-install-recommends \
 && apt-get clean \   
 && rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade pip
RUN pip3 install selenium pytest pytest-bdd pytest-html allure-pytest
RUN wget https://github.com/allure-framework/allure2/releases/download/2.24.0/allure-2.24.0.tgz \
 && tar -xvzf allure-2.24.0.tgz -C /opt/ \
 && ln -s /opt/allure-2.24.0/bin/allure /usr/bin/allure \
 && rm allure-2.24.0.tgz

ENV IN_DOCKER=true
ENV PYTEST_MARK="smoke" 
ENV CHROME_BIN=/usr/bin/chromium
ENV CHROMEDRIVER_PATH=/usr/bin/chromedriver

WORKDIR /app
COPY . /app

CMD ["sh", "-c", "pytest -m \"$PYTEST_MARK\" \
    --html=reports/html-report.html --self-contained-html && \
    allure generate reports/allure-results -o reports/allure-report --clean"]
