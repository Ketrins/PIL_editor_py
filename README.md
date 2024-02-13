# Simple Image Editor

This is a simple image editor that allows you to open, modify, and save images.

## Requirements

To use this image editor, you need to have the PIL library (or Pillow) installed, which can be installed via pip:
`pip install Pillow`


## Usage

1. Run the `pil.py` file.
2. Enter the name of the image file you want to open.
3. Choose the operation you want to perform (e.g., convert the image to black and white).

## Example

```python
from PIL import Image

# Creating an instance of the image editor
my_image = ImageEditor('cat.jpg')

# Opening the image
my_image.open()

# Performing black and white operation
my_image.do_bw()
