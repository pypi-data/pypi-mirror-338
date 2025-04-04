from setuptools import setup, find_packages

setup(
    name="parallel-runner",
    version="0.1.2",
    author="Mohammad Reza Soheili",
    author_email="msoheili@gmail.com",
    description="A Python utility for running functions in parallel using multiprocessing.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/msoheili/ParallelRunner",
    packages=find_packages(),
    install_requires=[
        "tqdm"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
