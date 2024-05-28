#!/usr/bin/env bash
# ---
# A script to manage docker services for the djazz project.
# ---
# Usage: services [command]

# Set the current directory
PWD=$(dirname "$0")

# If no command provided, show help

if [ $# -eq 0 ]; then
    cat <<-'EOF'
    Usage: services [command]

    Commands:
    - `start` start the services
    - `stop` stop the services
    - `status` show the status of the services
EOF
    exit 1;
fi

# First argument is the command
COMMAND=$1

# case statement to handle the command

case $COMMAND in
    start)
        echo "Starting the services..."
        # Check if the services are already running
        if [ "$(docker ps -q -f name=djazz-services)" ]; then
            docker restart djazz-services
            exit 1
        fi
        docker run -d \
            --name djazz-services \
            -v postgres-data:/var/lib/postgresql/data \
            -p 1025:1025 \
            -p 5432:5432 \
            -p 5672:5672 \
            -p 6379:6379 \
            -p 8025:8025 \
            -p 9000:9000 \
            -p 9001:9001 \
            -p 15672:15672 \
        azataiot/djazz-services:latest
        ;;
    stop)
        echo "Stopping the services... (to remove, use the remove command)"
        docker stop djazz-services
        ;;
    restart)
        echo "Restarting the services..."
        docker restart djazz-services
        ;;
    remove)
        echo "Removing the services..."
        docker rm djazz-services
        ;;
    status)
        echo "Showing the status of the services..."
        docker ps -f name=djazz-services
        ;;
    *)
        echo "Invalid command: $COMMAND"
        exit 1
        ;;
esac