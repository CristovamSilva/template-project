# syntax=docker/dockerfile:1
FROM python:3.10 as base

# ARG CONFIG_DIR=config

RUN --mount=type=cache,target=/var/cache/apt,sharing=locked \
    --mount=type=cache,target=/var/lib/apt,sharing=locked \
    <<eot bash
set -euo pipefail
export DEBIAN_FRONTEND=noninteractive
apt-get update
apt-get -y upgrade
apt-get -y install --no-install-recommends build-essential gcc
apt-get clean
mkdir -p -m 0600 /root/.ssh &&
ssh-keyscan -H github.com >> /root/.ssh/known_hosts
rm -rf /var/lib/apt/lists/*
eot

# COPY ${CONFIG_DIR} /root/
# RUN sed 's|/home/runner|/root|g' -i.bak /root/.ssh/config

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

WORKDIR /build
COPY . .
RUN --mount=type=cache,target=/root/.cache/pip pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r ./requirements.txt

FROM python:3.10-slim

COPY --from=base /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY ./API/app app

CMD [ "python", "-m", "app" ]
