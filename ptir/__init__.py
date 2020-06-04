import cv2
import os

is8Bit = False

def _print_error(e):
	print (u'\u001b[31mERROR: \u001b[33m' + str(e) + u'\u001b[0m')
	exit()

def _write_pixel(r, g=None, b=None):
	if not g or not b:
		b, g, r = list(map(lambda x: str(x), r))
	else:
		b, g, r = list(map(lambda x: str(x), [r, g, b]))
	if (is8Bit):
		to8bit = lambda x: int(int(x) // 42.51)
		r, g, b = to8bit(r), to8bit(g), to8bit(b)
		to8BitCode = lambda r, g, b: str(16 + 36 * r + 6 * g + b)
		print (u'\u001b[48;5;' + to8BitCode(r, g, b) + 'm  ', end='')
	else:
		print (u'\x1b[48;2;' + r + ';' + g + ';' + b + 'm  ', end='')

def render(image_path, width=100, height=100, interp_method='bilinear', c8bit=False):
	if (width <= 0 or height <= 0 or (width // 1 != width) or (height // 1 != height)):
		_print_error('WIDTH and HEIGHT parameters must be positive integers')

	pic = cv2.imread(image_path)
	
	if (pic is None):
		_print_error(f'Could not find image at location {image_path}')
	
	pic = cv2.resize(pic, dsize=(width, height), interpolation=(cv2.INTER_NEAREST if interp_method == 'nearest_neighbour' else cv2.INTER_LINEAR))

	is8Bit = c8bit

	for row in range(pic.shape[0]):
		for col in range(pic.shape[1]):
			_write_pixel(pic[row][col])
		print (u'\u001b[0m')

def view8BitPalette():
	for i in range(16):
		for j in range(16):
			ind = i * 16 + j
			code = str(ind)
			if ((ind + 8) % 6 == 0 and 232 > ind > 15) or ind == 16 or ind == 232:
				print(u'\u001b[0m')
			print (u'\u001b[48;5;' + code + 'm  ', end='')
	print (u'\u001b[0m')

def view24bitPalette(*, ARE=False, YOU=False, SURE=False):
	if ARE and YOU and SURE:
		for r in range(255):
			for g in range(255):
				for b in range(255):
					print (u'\x1b[48;2;' + str(r) + ';' + str(g) + ';' + str(b) + 'm ', end='')
				print (u'\u001b[0m')
		print (u'\u001b[0m')
	else:
		print (u'\u001b[36m=====================================================================================================================\u001b[0m')
		print ('There are 16,777,216 colours in the RGB 24-bit colour space')
		print ('I do not recommend looking at the screen while this is running to avoid headaches and DO NOT RUN IF YOU HAVE EPILEPSY')
		print ('To see the colour space you must run \'ptir.view24bitPalette(ARE=True, YOU=True, SURE=True)\'')
		print ('Run at your own risk!')
		print (u'\u001b[36m=====================================================================================================================\u001b[0m')