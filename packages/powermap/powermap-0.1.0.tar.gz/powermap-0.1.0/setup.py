from setuptools import setup, find_packages
import os

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

version = "0.1.0"
with open(os.path.join("powermap", "__init__.py"), "r", encoding="utf-8") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip("\"'")
            break

setup(
    name="powermap",
    version=version,
    description="Client for PowerMap geospatial API services",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="PowerMap",
    author_email="",
    url="",
    packages=find_packages(exclude=["tests", "tests.*"]),
    install_requires=[
        "requests>=2.25.0",
        "shapely>=2.0.0",
        "openlocationcode>=1.0.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    keywords="powermap, grid"
)
