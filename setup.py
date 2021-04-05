from setuptools import setup

with open("README.md", "r") as f:
	long_description = f.read() 

setup(
	name="turtex",
	version="0.0.1",
	description="Extension to turtle module.",
	py_modules=["turtex"],
	package_dir={"": "src"},
	classifiers=[
		"Development Status :: 2 - Pre-Alpha",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
		"Programming Language :: Python",
		"Programming Language :: Python :: 3",
		"Programming Language :: Python :: 3.0",
		"Programming Language :: Python :: 3.1",
		"Programming Language :: Python :: 3.2",
		"Programming Language :: Python :: 3.3",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3.6",
		"Programming Language :: Python :: 3.7",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Programming Language :: Python :: 3.10",
		"Topic :: Artistic Software",
		"Topic :: Multimedia",
		"Topic :: Multimedia :: Graphics",
		"Topic :: Software Development :: Libraries",
		"Topic :: Software Development :: Libraries :: Python Modules"
	],
	long_description=long_description,
	long_description_content_type="text/markdown",
	url="https://github.com/GimLala/Turtex",
	author="G Lala",
	author_email= "gimpylala@gmail.com"
)
