from setuptools import setup, find_packages

setup(
    name="zipsar",
    version="0.1.0",
    author="pk",
    author_email="",
    description="A Python package for Zipsar.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
