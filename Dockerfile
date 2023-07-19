# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# The environment variable ensures that the python output is set straight
# to the terminal without buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /podcast_app

# Set the working directory to /podcast_app
WORKDIR /podcast_app

# Copy the current directory contents into the container at /podcast_app
ADD . /podcast_app/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the command
CMD ["python", "./backend/app.py"]