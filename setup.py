from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in sales_monitoring/__init__.py
from sales_monitoring import __version__ as version

setup(
	name="sales_monitoring",
	version=version,
	description="Monitor SO, DN, SI, Customer",
	author="Yohannes",
	author_email="yohanneswoo10@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
