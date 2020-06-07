from PIL import Image
import numpy as np
import os

def _print_error(e):
	print (u'\u001b[31mERROR: \u001b[33m' + str(e) + u'\u001b[0m')

def render(image_path, width=100, height=100, interp_method='bilinear', only8Bit=False, only24Bit=False):
	if (width <= 0 or height <= 0 or (width // 1 != width) or (height // 1 != height)):
		_print_error('WIDTH and HEIGHT parameters must be positive integers')
		return

	if (only8Bit and only24Bit):
		_print_error('Cannot have both only8Bit and only24Bit parameters true. They are mutually exclusive modes')
		return

	pic = Image.open(image_path)
	
	if (pic is None):
		_print_error(f'Could not find image at location {image_path}')
		return
	
	pic = np.array(pic.resize((width, height), resample=(Image.NEAREST if interp_method == 'nearest_neighbour' else Image.BILINEAR)))
	
	to8Bit = lambda x: int(int(x) // 42.51)
	to8BitCode = lambda r, g, b: str(16 + 36 * to8Bit(r) + 6 * to8Bit(g) + to8Bit(b))

	def _write_pixel(rgb):
		r, g, b = list(map(lambda x: str(x), rgb))

		if (only8Bit):
			print (u'\u001b[48;5;' + to8BitCode(r, g, b) + 'm  ', end='')
		elif (only24Bit):
			print (u'\x1b[48;2;' + r + ';' + g + ';' + b + u'm  ', end='')
		else:
			# 8-bit background and 24-bit foreground
			print (u'\u001b[48;5;' + to8BitCode(r, g, b) + 'm', end='')
			print (u'\x1b[38;2;' + r + ';' + g + ';' + b + u'm\u2588\u2588', end='')

	for row in range(pic.shape[0]):
		for col in range(pic.shape[1]):
			_write_pixel(pic[row][col][:3])
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

def view24BitPalette(*, ARE=False, YOU=False, SURE=False):
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