# Image-to-Text Tool

---

## Project Description

This tool processes images and generates textual descriptions using advanced machine learning models. 

It supports multiple models such as BLIP and UForm, allowing users to choose the model that best fits their needs.

---

## Setup and Installation

To set up the environment for this project, please follow the instructions according to your operating system.

---

### For Unix-based Systems (Linux, macOS)

1. Open a terminal.
2. Navigate to the project's root directory.
3. Run the following command to execute the installation script:

```bash
./install.sh
```

This script will create a Python virtual environment, activate it, install the necessary dependencies, and set up the PyTorch library with GPU support.

---

### For Windows Systems

1. Open Command Prompt.
2. Navigate to the project's root directory.
3. Run the following command to execute the installation script:

```bash
install.bat
```

_Note: It's also possible to execute the script by double-clicking the `install.bat` file in Windows Explorer._

Similar to the Unix script, this will set up the Python virtual environment and install all necessary dependencies, including PyTorch with GPU support.

---

### Docker Setup

Alternatively, you can use Docker to set up the environment:

1. Ensure Docker is installed on your system.
2. Build the Docker image:

```bash
docker build -t image-to-text-tool .
```

3. To run the Docker container with the project's root directory mapped as a volume, use the following command. This allows you to have the input folder and other necessary files within the container.

- For Unix-based Systems:

```bash
docker run -it --gpus all -v $(pwd):/usr/src/app image-to-text-tool
```

- For Windows Systems (Command Prompt):

```bash
docker run -it --gpus all -v %cd%:/usr/src/app image-to-text-tool
```

- For Windows Systems (PowerShell):

```bash
docker run -it --gpus all -v ${PWD}:/usr/src/app image-to-text-tool
```

This approach uses the NVIDIA CUDA base image and sets up the environment with GPU support, while also allowing you to work directly with your project files.

---

## Usage

After installing the dependencies and setting up the environment, you can use the tool as follows:

Place the images you want to process in the `input` folder.

Run the `run.py` script with the desired model flags. 

For example:

```bash
python run.py --blip --uform
```

To process the images using all available models, simply run the script without any flags:

```bash
python run.py
```

This will process the images using the specified models and generate textual descriptions.

---

## Output

The output will be saved in `JSON` format in designated files for each model. Check the output files in the project directory to view the descriptions generated for each image.
