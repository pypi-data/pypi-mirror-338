from setuptools import setup, find_packages

setup(
    name='bactovision',
    version='0.1.0',
    description='A package for bacterial image processing',
    author='Vladimir Starostin',
    author_email='vladimir.starostin@uni-tuebingen.de',
    url='https://github.com/StarostinV/bactovision',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'numpy',
        'scipy',
        'scikit-image',
        'Pillow',
        'opencv-python',
        'anywidget',
        'traitlets',
        'matplotlib',
        'jupyterlab',
    ],
)
