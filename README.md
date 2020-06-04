# PTIR (Python Terminal Image Renderer)

### Installation
`pip install ptir`

### Usage
```python
import ptir

image_path = ...

# Render the given image
ptir.render(image_path)

# Display entire 8-bit colour space
ptir.view8BitPalette()

# Display entire 24-bit colour space
ptir.view24bitPalette()
```
### Documentation
- `ptir.render(image_path, width=100, height=100, interp_method='bilinear', c8bit=False)`
  - `image_path` : Path to the image that will be rendered
  - `width` : The width of the output (will be 2 * `width` characters wide)
  - `height` : The height of the output (will be 2 * `height` characters tall)
  - `interp_method` : Rescale interpolation method (Either 'bilinear' or 'nearest_neighbour')
  - `c8bit` : If True the image will be rendered in 8-bit colour, if False the image will be rendered in 24-bit colour. Not all terminal windows support 24-bit colour (Visit [this website](https://gist.github.com/XVilka/8346728) for more information)

### Dependencies
- `opencv-python`