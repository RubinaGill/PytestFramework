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
    --no-install-recommends

RUN pip3 install --upgrade pip
RUN pip3 install selenium pytest pytest-bdd pytest-html

WORKDIR /app
COPY . /app

CMD ["sh", "-c", "pytest -m \"$PYTEST_MARK\""]
# Set the environment variable for pytest marker
ENV PYTEST_MARK="smoke" 
