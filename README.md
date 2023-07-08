# Specific RGB Color identification Project

This project uses computer vision techniques to detect and identify specific RGB colours in an image. It converts the image into black and white, where the selected colour appears white, and the rest of the image appears black.

## Features

- Detect and recognize specific RGB colors in an image.
- Convert the image to black and white, highlighting the selected color in white.
- Allow users to specify the RGB color to detect.
- Provide visual feedback by displaying the processed image with the selected color highlighted.

## Requirements

- Python 3.7 or above
- PIL (Python Imaging Library) module

## Installation

1. Clone the project repository:

   ```bash
   git clone https://github.com/SenChirag/Specific_RGB_color_identification.git
   ```

2. Navigate to the project directory:

   ```bash
   cd Specific_RGB_color_identification
   ```

3. Install the required dependencies:

   ```bash
   pip install pillow
   ```

## Usage

1. Prepare the image file on which you want to perform RGB color detection.

2. Modify the configuration settings in the `config.py` file, if needed. Specify the RGB color values you want to detect.

3. Run the project:

   ```bash
   python Specific_RGB_color_identification.py
   ```

4. The program will process the image and convert it into black and white, with the selected color appearing white.

5. The processed image will be displayed, highlighting the selected color in white.

6. Close the image window to exit the program.

## Contributing

Contributions are welcome! If you have any ideas, improvements, or bug fixes, please submit a pull request. Make sure to follow the existing code style and provide clear documentation for your changes.


## Acknowledgements

- [PIL (Python Imaging Library)](https://pillow.readthedocs.io/) - Python library for image processing


