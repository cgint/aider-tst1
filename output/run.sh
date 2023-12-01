#!/bin/bash
docker run --rm -v "$(pwd)/input/task1":/usr/src/app/input/task1 -v "$(pwd)/output":/usr/src/app/output merge-csv
