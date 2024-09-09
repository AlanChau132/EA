ARG VARIANT=3.16
FROM mcr.microsoft

ENV PYTHONUNBUFFERED 1

# Install Docker CLI
RUN apt-get update && \
    apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg-agent \
    software-properties-common && \
    curl -fsSL https://download.docker.com/linux/debian/gpg | apt-key add - && \
    add-apt-repository \
    "deb [arch=amd64] https://download.docker.com/linux/debian \
    $(lsb_release -cs) \
    stable" && \
    apt-get update && \
    apt-get install -y docker-ce-cli

# Copy requirements.txt to a temporary location
COPY requirements.txt /tmp/pip-tmp/

# Install dependencies with increased timeout and retry mechanism
RUN for i in 1 2 3; do \
      pip3 --disable-pip-version-check --no-cache-dir install --default-timeout=1000 -r /tmp/pip-tmp/requirements.txt \
      && break || sleep 5; \
    done \
    && rm -rf /tmp/pip-tmp