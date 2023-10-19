FROM python:3.11-slim-bullseye

# Update package list and install essential dependencies
RUN apt-get update -y \
    && apt-get install -y --no-install-recommends wget unzip apt-utils make curl gnupg jq \
    && rm -rf /var/lib/apt/lists/*

# Setting the working directory
WORKDIR /app

# Copy only the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Set permission on script
RUN chmod +x wait-for-grid.sh

# Run tests
ENTRYPOINT ["make"]
CMD ["test"]
