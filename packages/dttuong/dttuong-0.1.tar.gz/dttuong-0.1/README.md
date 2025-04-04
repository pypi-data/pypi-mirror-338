# dttuong

The `dttuong` library is a Python library that helps process images with linear transformations, which can be applied to grayscale and color images.

## Installation

To install this library, you can use pip:

pip install dttuong

## Usage

```python
import dttuong

Where:

input_path: input image path

output_path: output image path

auto_mode: is the linear transformation mode, with values ​​such as: auto_mode = "histogram" or auto_mode = "kmeans"
## How it works

- **`histogram` mode**: Segment the image based on the pixel distribution from the histogram.

- **`kmeans` mode**: Use the K-Means algorithm to cluster pixel values.

In addition, auto_mode = None, you can enter the value of breakpoints as you want

How to use dttuong library
Suppose you have an input.jpg image, you want to transform linearly each piece with automatic breakpoints using K-Means, you can run:

Here is a simple way to use

Gray image processing
import cv2
import matplotlib.pyplot as plt
from dttuong import process_gray_image

# Process gray image with automatic mode using K-Means
output_image = process_gray_image("input.jpg", auto_mode="kmeans")

# Display the result
plt.imshow(output_image, cmap="gray")
plt.title("Image After Transformation")
plt.show()

# Save the image
cv2.imwrite("output_gray.jpg", output_image)

Color Image Processing
import cv2
import matplotlib.pyplot as plt
from dttuong import process_color_image

# Color Image Processing with Auto Mode using Histogram
output_image = process_color_image("input.jpg", auto_mode="histogram")

# Display the result
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.title("Image After Transformation")
plt.show()

# Save the image
cv2.imwrite("output_color.jpg", output_image)

If you want to enter transformation points manually
from dttuong import process_gray_image

# Define the linear transformation points piecewise
breakpoints = [(0, 0), (100, 50), (150, 200), (255, 255)]

# Process grayscale image with custom transform points

output_image = process_gray_image("input.jpg", breakpoints=breakpoints)

# Save image
cv2.imwrite("output_manual.jpg", output_image)

Run the program from Terminal
If you want to write a separate script (main.py) to run it quickly:
from dttuong import process_gray_image

input_path = "input.jpg"
output_path = "output_gray.jpg"
auto_mode = "histogram" # Or "kmeans"

output_image = process_gray_image(input_path, auto_mode=auto_mode)
cv2.imwrite(output_path, output_image)

print(f"Image processed! The result is saved at: {output_path}")

Then run:
python main.py

Summary:
You just need to import process_gray_image or process_color_image from dttuong and call them with the appropriate parameters. 🚀

HHow to manually enter breakpoints
You just need to pass a list of breakpoints to the process_gray_image or process_color_image function.

Example: Processing grayscale images with manually entered breakpoints
import cv2
import matplotlib.pyplot as plt
from dttuong import process_gray_image

# Define the points of the piecewise linear transformation (x, y)
breakpoints = [(0, 0), (50, 30), (100, 120), (200, 220), (255, 255)]

# Image processing
output_image = process_gray_image("input.jpg", breakpoints=breakpoints)

# Display the result
plt.imshow(output_image, cmap="gray")
plt.title("Image After Transformation")
plt.show()

# Save the image
cv2.imwrite("output_gray_manual.jpg", output_image)
print("✅ Image saved successfully!")

Example: Process color images with manually entered breakpoints
import cv2
import matplotlib.pyplot as plt
from dttuong import process_color_image

# Define breakpoints
breakpoints = [(0, 0), (50, 30), (100, 120), (200, 220), (255, 255)]

# Process color images
output_image = process_color_image("input.jpg", breakpoints=breakpoints)

# Display the result
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.title("Image After Transformation")
plt.show()

# Save the image
cv2.imwrite("output_color_manual.jpg", output_image)
print(" Color image saved successfully!")
Summary
Define the list of breakpoints in the format:
breakpoints = [(0, 0), (50, 30), (100, 120), (200, 220), (255, 255)]

Call the process_gray_image() or process_color_image() function and pass in the breakpoints.

Save the image using cv2.imwrite("output.jpg", output_image).

Now you can manually input breakpoints and process photos as you like!