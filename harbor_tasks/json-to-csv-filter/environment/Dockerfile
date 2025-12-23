FROM python:3.11-slim

WORKDIR /app

# Copy only the input data
COPY input.json /app/input.json

# Ensure the container stays alive or is ready to run commands
CMD ["tail", "-f", "/dev/null"]
