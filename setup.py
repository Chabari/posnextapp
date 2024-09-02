from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in posnextapp/__init__.py
from posnextapp import __version__ as version

setup(
	name="posnextapp",
	version=version,
	description="Mobile app API",
	author="George Mukundi",
	author_email="geetabtechnologiesltd@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
