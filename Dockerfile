# Use an official Python runtime as a parent image
FROM python:3.8

# Set environment variables for Django
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any required packages
RUN pip install -r requirements.txt

# Expose the port your application will run on
EXPOSE 8000

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/

# Make the entrypoint script executable
RUN chmod +x /app/entrypoint.sh

# Set the entrypoint to the script
ENTRYPOINT ["/app/entrypoint.sh"]
