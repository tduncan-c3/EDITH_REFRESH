FROM fnproject/python:3.11-dev

# Install required packages for building dlib using yum
RUN yum install -y \
    epel-release && \
    yum install -y \
    mesa-libGL \
    glib2 \
    cmake \
    gcc-c++ \
    make

# Set the working directory
WORKDIR /function

# Copy the current directory contents into the container at /function
COPY . /function

# Install Python dependencies if needed
RUN pip install -r requirements.txt

# Set the entrypoint to use the fdk
ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]