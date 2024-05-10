#!/usr/bin/env bash
# ---
# A script to manage docker services for the djazz project.
# ---

PWD=$(dirname "$0")
MANAGE_PATH=$(realpath "$PWD/../manage.py")
DOCKER_COMPOSE_PATH=$(realpath "$PWD/../docker/compose.dev.yaml")

# Check if the manage.py file exists
if [ ! -f "$MANAGE_PATH" ]; then
    echo "The manage.py file does not exist, are you in the right directory?"
    exit 1
fi

# Check if the compose.yml file exists
if [ ! -f "$DOCKER_COMPOSE_PATH" ]; then
    echo "The compose.yml file does not exist, are you in the right directory?"
    exit 1
fi

# Usage
usage() {
    echo "Usage: $0 [start|stop|restart|status]"
    echo "This script is used to manage the docker services for the djazz project in development ONLY."
    exit 1
}

# Start the services
start() {
    echo "Starting the services from ${DOCKER_COMPOSE_PATH}..."
    docker compose -f "$DOCKER_COMPOSE_PATH" --profile debug up -d
}

# Stop the services
stop() {
    docker compose -f "$DOCKER_COMPOSE_PATH" down
}

# Restart the services
restart() {
    stop
    start
}

# Get the status of the services
status() {
    docker compose -f "$DOCKER_COMPOSE_PATH" ps
}

# Check the number of arguments
if [ "$#" -ne 1 ]; then
    usage
fi

# Check the argument
case "$1" in
    start)
        start
        ;;
    stop)
        stop
        ;;
    restart)
        restart
        ;;
    status)
        status
        ;;
    *)
        usage
        ;;
esac