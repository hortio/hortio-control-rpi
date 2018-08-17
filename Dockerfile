FROM resin/rpi-raspbian:latest
LABEL maintainer="Sergei Silnov <po@kumekay.com>"

RUN apt-get update && apt-get install -y \
    python \
    python-pip \
    python-smbus \
    --no-install-recommends && \
    rm -rf /var/lib/apt/lists/*

COPY control/ /app

# Define default command
CMD ["python", "/app/core.py"] 