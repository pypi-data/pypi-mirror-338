from setuptools import setup, find_packages

setup(
    name="TrainSense",
    version="0.0.0",
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
    ]
)