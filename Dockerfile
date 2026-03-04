FROM ghcr.io/astral-sh/uv:python3.14-alpine

COPY src /jumpstart

WORKDIR /jumpstart

CMD ["echo", ":)"]