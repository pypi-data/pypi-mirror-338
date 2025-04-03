"""Setup script for BactoVision package."""

import pathlib

from setuptools import find_packages, setup

# Get the long description from the README file
root_dir = pathlib.Path(__file__).parent.resolve()
long_description = (root_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="bactovision",
    version="0.1.1",
    description="A package for bacterial image processing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Vladimir Starostin",
    author_email="vladimir.starostin@uni-tuebingen.de",
    url="https://github.com/StarostinV/bactovision",
    packages=find_packages(exclude=["tests", "tests.*"]),
    include_package_data=True,
    install_requires=[
        "numpy>=1.20.0,<2.0.0",
        "scipy>=1.8.0,<1.15.0",
        "scikit-image>=0.18.0",
        "Pillow>=9.0.0",
        "opencv-python>=4.5.0",
        "anywidget>=0.1.0",
        "traitlets>=5.0.0",
        "matplotlib>=3.5.0",
        "jupyterlab>=3.0.0",
    ],
    python_requires=">=3.8",
)
