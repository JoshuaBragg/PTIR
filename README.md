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
- `ptir.render(image_path, width=100, height=100, interp_method='bilinear', only8Bit=False, only24Bit=False)`
  - `image_path` : Path to the image that will be rendered
  - `width` : The width of the output (will be 2 * `width` characters wide)
  - `height` : The height of the output (will be `height` characters tall)
  - `interp_method` : Rescale interpolation method (Either 'bilinear' or 'nearest_neighbour')
  - `only8Bit` : If True the image will be rendered without any 24-bit colour 
  - `only24Bit` : If True the image will be rendered without any 8-bit colour. This mode is recommended to be used only if you are confident that the terminal will support 24-bit colour but are unsure if unicode characters are supported by the terminal font
- Not all terminal windows support 24-bit colour (Visit [this website](https://gist.github.com/XVilka/8346728) for more information on TrueColour support)
- **The macOS default Terminal.app DOES NOT support 24-bit colour!**
- By default the image will be rendered with two layers, 24-bit foreground to display properly on supporting terminals, and a 8-bit background to display if 24-bit colour is not available
  
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
