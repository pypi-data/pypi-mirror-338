
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="neuronmix",
    version="0.1.3",  # Bump version!
    author="Muhammad Adeel Javaid",
    author_email="ajavaid@ieee.org",
    description="Neuron-level mixed activation layer for PyTorch",
    long_description=long_description,
    long_description_content_type="text/markdown",  # ✅ Required for README.md
    url="https://github.com/ajaviaad/neuronmix",
    project_urls={
        "Documentation": "https://github.com/ajaviaad/neuronmix",
        "Source": "https://github.com/ajaviaad/neuronmix",
        "Tracker": "https://github.com/ajaviaad/neuronmix/issues",
    },
    license="MIT",
    packages=find_packages(),
    install_requires=["torch"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
