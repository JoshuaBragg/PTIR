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
ptir.view24BitPalette()
```
### Documentation
- `ptir.render(image_path, width=100, height=100, interp_method='bilinear', is8Bit=False)`
  - `image_path` : Path to the image that will be rendered
  - `width` : The width of the output (will be 2 * `width` characters wide)
  - `height` : The height of the output (will be 2 * `height` characters tall)
  - `interp_method` : Rescale interpolation method (Either 'bilinear' or 'nearest_neighbour')
  - `is8Bit` : If True the image will be rendered in 8-bit colour, if False the image will be rendered in 24-bit colour. Not all terminal windows support 24-bit colour (Visit [this website](https://gist.github.com/XVilka/8346728) for more information)
  
### Example #1
**Original**:

![mountain original](https://joshbra.gg/mountain.jpeg)

**24-bit**:

![mountain 24-bit](https://joshbra.gg/mountain24.png)

**8-bit**:

![mountain 8-bit](https://joshbra.gg/mountain8.png)

### Example #2
**Original**:

![mario original](https://joshbra.gg/mario.jpg)

**24-bit**:

![mario 24-bit](https://joshbra.gg/mario24.png)

**8-bit**:

![mario 8-bit](https://joshbra.gg/mario8.png)

### Dependencies
- `pillow`
- `numpy`
