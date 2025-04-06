from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="image_processing",
    version="0.0.1",
    author="Matheus",
    description="Image processing  Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MatheusPRodrigues/image-processing-package",
    packages=find_packages(),
    install_requires=[
        "matplotlib",
        "numpy",
        "scikit-image >= 0.16.1"
    ],
    python_requires='>=3.5',
)