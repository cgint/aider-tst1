#!/bin/bash

# Build the Docker image
docker build -t solution-image .

# Run the Docker container with volume mounts
docker run --rm --name solution-container -v "$(pwd)/input:/usr/src/app/input" -v "$(pwd)/output:/usr/src/app/output" solution-image
