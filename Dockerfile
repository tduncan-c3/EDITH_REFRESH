FROM oraclelinux:8-slim

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

# Install Python and necessary Python packages
RUN yum install -y python3 && \
    pip3 install -r requirements.txt

# Set the entrypoint to use the fdk
ENTRYPOINT ["/usr/local/bin/fdk", "/function/func.py", "handler"]
