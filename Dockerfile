FROM oraclelinux:8-slim

# Install Python 3
RUN yum install -y python3

# Install required packages for building dlib
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

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set the entrypoint to use the fdk
ENTRYPOINT ["/usr/local/bin/fdk", "/function/func.py", "handler"]
