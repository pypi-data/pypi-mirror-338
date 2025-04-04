from setuptools import setup, find_packages

setup(
    name="synthra",  # Replace with your desired package name
    version="0.1.2",
    packages=find_packages(include=["synthra", "synthra.*"]),  # Explicitly include the synthra package
    install_requires=[
        "colorama>=0.4.6",
    ],
    description="A simple logging module for Python",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author="x2sadddDM",
    author_email="x2saddddm@gmail.com",
    url="https://github.com/x2saddDM/synthra-logger",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)
