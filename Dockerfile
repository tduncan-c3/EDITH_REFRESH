FROM fnproject/python:3.11-dev

# Install required packages for building dlib
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    cmake \
    g++ \
    make

# Set the working directory
WORKDIR /function

# Copy the current directory contents into the container at /function
COPY . /function

# Install Python dependencies if needed
RUN pip install -r requirements.txt

# Set the entrypoint to use the fdk
ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]
