import setuptools

with open('README.md', 'r') as fh:
	long_description = fh.read()

setuptools.setup(
	name='ptir',
	version='1.2.0',
	author='Joshua Bragg',
	author_email='joshua.bragg@outlook.com',
	description='Python Terminal Image Renderer',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/JoshuaBragg/PTIR',
	packages=setuptools.find_packages(),
	license='MIT',
	install_requires=[
		'numpy',
		'Pillow'
	],
	classifiers=[
		'Programming Language :: Python :: 3',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	]
)