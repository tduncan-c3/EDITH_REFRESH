# Use an official Python runtime as a parent image
FROM fnproject/python:3.8

# Set the working directory in the container
WORKDIR /function

# Copy the current directory contents into the container at /function
COPY . /function

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install the necessary OpenGL and GLib libraries
RUN apt-get update && apt-get install -y libgl1-mesa-glx libglib2.0-0

# Command to run the function
CMD ["python", "func.py"]