# Use an official Python runtime as a parent image
FROM python:3.10.9


# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the trained Rasa model from the models directory
COPY ./models /app/models

# Make port 5005 available to the world outside this container
EXPOSE 5005

# Define environment variables
ENV RASA_HOME=/app

# Command to run your Rasa chatbot
CMD ["rasa", "run", "-m", "models", "--endpoints", "endpoints.yml"]

