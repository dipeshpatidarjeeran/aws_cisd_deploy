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
# RUN python manage.py makemigrations
# RUN python manage.py migrate

# Define the command to run your application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]