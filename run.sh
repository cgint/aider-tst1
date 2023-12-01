#!/bin/bash

# Build the Docker image
docker build -t solution-image .

# Run the Docker container
docker run --rm --name solution-container solution-image
