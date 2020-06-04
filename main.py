import cv2
import sys
import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument('input_image', help='Path to input image')
parser.add_argument('-width', help='Width dim of output [DEFAULT = 100]', default=100)
parser.add_argument('-height', help='Height dim of output [DEFAULT = 100]', default=100)
parser.add_argument('--biliniear', help='Supply this parameter to use biliniear interpolation [DEFAULT]', action='store_true')
parser.add_argument('--nearest_neighbour', help='Supply this parameter to use nearest_neighbour interpolation', action='store_true')
parser.add_argument('--c8bit', help='Supply this parameter to use 8-bit colour set [REQUIRED ON TERMINALS THAT DONT SUPPORT TRUECOLOR]', action='store_true')

args = parser.parse_args()

pic = cv2.imread(args.input_image)
pic = cv2.resize(pic, dsize=(int(args.width), int(args.height)), interpolation=(cv2.INTER_NEAREST if args.nearest_neighbour else cv2.INTER_LINEAR))

nl = u'\u001b[0m'

def write_pixel(r, g=None, b=None):
	if not g or not b:
		b, g, r = list(map(lambda x: str(x), r))
	else:
		b, g, r = list(map(lambda x: str(x), [r, g, b]))
	if (args.c8bit):
		c8bit = lambda x: int(int(x) // 42.51)
		r, g, b = c8bit(r), c8bit(g), c8bit(b)
		to8BitCode = lambda r, g, b: str(16 + 36 * r + 6 * g + b)
		sys.stdout.write(u'\u001b[48;5;' + to8BitCode(r, g, b) + 'm  ')
	else:
		sys.stdout.write(u'\x1b[48;2;' + r + ';' + g + ';' + b + 'm  ')

for row in range(pic.shape[0]):
	for col in range(pic.shape[1]):
		write_pixel(pic[row][col])
	print (nl)