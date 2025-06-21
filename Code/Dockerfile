FROM python:3.11

RUN apt-get update && apt-get install -y \
    wget \
    libnss3 \
    libatk-bridge2.0-0 \
    libx11-xcb1 \
    libxcomposite1 \
    libxcursor1 \
    libxdamage1 \
    libxi6 \
    libxtst6 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libgtk-3-0 \
    libdrm2 \
    libxshmfence1 \
    libxss1 \
    libxfixes3 \
    libxext6 \
    libxrender1 \
    libfontconfig1 \
    libfreetype6 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libcairo2 \
    libcairo-gobject2 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt


RUN pip install playwright && \
    for i in 1 2 3; do playwright install --with-deps && break || sleep 5; done


COPY . /scripts
WORKDIR /scripts

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
