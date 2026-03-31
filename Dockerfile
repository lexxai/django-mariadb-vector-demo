ARG PYTHON_VERSION=3.13

FROM python:${PYTHON_VERSION} AS builder

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY "pyproject.toml" "uv.lock" ./
COPY ./dist/ ./dist/
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --link-mode=copy --locked --no-dev --no-install-project

FROM python:${PYTHON_VERSION}-slim

ARG _USER=appuser
ARG _GROUP=appgroup

WORKDIR /app

ENV DEBIAN_FRONTEND=noninteractive
RUN groupadd ${_GROUP} && useradd --no-log-init -r --no-create-home -G ${_GROUP} ${_USER} \
    && apt-get update -y && apt-get install -y \
    curl \
    procps \
    default-libmysqlclient-dev \
    default-mysql-client \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY --from=builder /app/.venv /app/.venv
COPY --from=builder /app/pyproject.toml ./
# COPY --chown=${_USER}:${_GROUP} ./src ./src/
COPY --chmod=+x  *.sh ./


ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PATH=/app/.venv/bin/:$PATH \
    VIRTUAL_ENV=/app/.venv \
    PYTHONPATH=/app/src

USER ${_USER}

ENTRYPOINT ["/app/entrypoint.sh"]
