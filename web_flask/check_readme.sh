#!/bin/bash

if [ -s README.md ]; then
    echo "README.md exists and is not empty."
else
    echo "README.md is missing or empty."
fi
