#!/bin/bash

echo "Installing CLIP from OpenAI repository..."
pip install git+https://github.com/openai/CLIP.git

if [ $? -eq 0 ]; then
    echo "CLIP installation successful!"
else
    echo "Error installing CLIP. Please try manually: pip install git+https://github.com/openai/CLIP.git"
    exit 1
fi