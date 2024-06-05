ARG PYTHON_VERSION=3.12-alpine
FROM python:${PYTHON_VERSION} as builder
ARG DEV
ENV DEV=${DEV:-0}
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
RUN set -eux; \
	\
    apk add --no-cache bash && \
    pip install --no-cache-dir --no-deps --upgrade pip && \
    pip install --no-cache-dir pip-tools

COPY requirements/base.in /requirements.in
RUN pip-compile --upgrade --output-file requirements.txt requirements.in && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r requirements.txt

COPY requirements/dev.in /dev-requirements.in
RUN set -eux; \
	\
    if [ $DEV = 1 ]; then \
    pip-compile --upgrade --output-file dev-requirements.txt dev-requirements.in && \
    pip wheel --no-cache-dir --no-deps --wheel-dir /wheels -r dev-requirements.txt ; \
    fi


FROM python:${PYTHON_VERSION} as runner
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
COPY --from=builder /wheels /wheels
COPY --from=builder /bin/bash /bin/bash
RUN apk add --no-cache bash && \
    pip install --no-cache-dir --no-deps /wheels/* && \
    rm -rf /wheels

WORKDIR /djazz
COPY . /djazz

EXPOSE 8000
VOLUME /djazz/data

CMD ["bash", "./scripts/entrypoint.sh"]