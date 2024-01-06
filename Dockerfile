# Use an official NVIDIA runtime as a parent image
FROM nvidia/cuda:12.1.1-runtime-ubuntu22.04

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Change permissions to ensure read and write access
RUN chmod -R 777 /usr/src/app

# Install Python and pip
RUN apt-get update && apt-get install -y python3-pip python3-dev

# Install any needed packages specified in requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

# Install the PyTorch version with CUDA support
RUN pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu121

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME ImageToTextTool

# Set a default command for the container (can be overridden)
CMD ["bash"]
