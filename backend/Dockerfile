# GET python and Alphine Linux OS from dockerHub
FROM python:3.9-alpine3.13
LABEL maintainer="TyW-98"

ENV PYTHONUNBUFFERED 1

# Copy local file to container directory
COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./app /app

# Change working directory
WORKDIR /app

# Port to be exposed when running container
EXPOSE 8000

# Set build argument DEV false
ARG DEV=false

# Create new virtual environment
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    # Install postgresql adapter (psycopg2)
    apk add --update --no-cache postgresql-client && \
    # Group installation necessary packages togehter
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev && \
    # Install dependencies from requirements.txt
    /py/bin/pip install -r /tmp/requirements.txt && \
    # Only install dev dependencies if DEV is True
    if [ $DEV = "true" ]; then \
        /py/bin/pip install -r /tmp/requirements.dev.txt ; \
    fi && \
    # remove temporary directory (Since this is not needed after packages are installed)
    rm -rf /tmp && \
    # Remove packages grouped in the directory (Excess packages)
    apk del .tmp-build-deps && \
    # Add new user inside docker image
    adduser \
        --disabled-password \
        --no-create-home \
        project-user

# Will add "/py/bin" to the system path therefore it will run command in the path everytime.
ENV PATH="/py/bin:$PATH"

# Switch away from root user
USER project-user