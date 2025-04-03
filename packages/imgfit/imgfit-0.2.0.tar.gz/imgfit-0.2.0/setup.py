from setuptools import setup, find_packages
import sys

data_files = []
if sys.platform == "win32":
    data_files = [("scripts","scripts/img.exe")]

setup(
    name = "imgfit",
    version = "0.2.0",
    packages = find_packages(),
    install_requires = ["pillow"],
    python_requires = ">=3",
    author = "xystudio",
    author_email = "173288240@qq.com",
    description = "Change your images.",
    long_description = open("README.md",encoding="utf-8").read(),
    license = "MIT",
    url = "https://github.com/xystudio889/imgfit",
    data_files = data_files,
    include_package_data = True
)
