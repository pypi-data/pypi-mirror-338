from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

setup(
    name="TrainSense",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[
        "GPUtil",
        "psutil",
        "torch"
    ],
    description="A package to analyze architecture and optimize model training",
    author="RDTvlokip",
    author_email="rdtvlokip@gmail.com",
    url="https://github.com/RDTvlokip/TrainSense",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    long_description=description,
    long_description_content_type="text/markdown",
)