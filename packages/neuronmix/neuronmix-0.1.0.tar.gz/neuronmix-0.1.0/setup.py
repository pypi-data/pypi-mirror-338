from setuptools import setup, find_packages

setup(
    name='neuronmix',
    version='0.1.0',
    description='Neuron-level mixed activation for deep learning models',
    author='Muhammad Adeel Javaid',
    author_email='ajavaid@ieee.org',
    license='MIT',
    packages=find_packages(),
    install_requires=['torch'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
