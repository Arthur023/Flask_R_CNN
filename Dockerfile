
# Use an official Python runtime as a parent image
#FROM python:3
FROM tensorflow/tensorflow:latest
#FROM python:alpine
# Set the working directory to /app
WORKDIR /flask_arthur3
# Copy the current directory contents into the container at /app
COPY . /flask_arthur3
#  Install any needed packages specified in requirements.txt
#RUN apk update
RUN ["apt-get", "install", "-y", "libsm6", "libxext6", "libxrender-dev"]
RUN pip install -r requirements.txt
# Make port 8000 available to the world outside this container
EXPOSE 5000
# Run app.py when the container launches
#CMD ["python", "app.py"]
CMD flask run --host 172.17.0.2
#CMD flask run --host 172.0.0.1