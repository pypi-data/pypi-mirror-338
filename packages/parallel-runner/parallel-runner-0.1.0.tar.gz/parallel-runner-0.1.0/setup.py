from setuptools import setup, find_packages

setup(
    name="parallel-runner",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python utility for running functions in parallel using multiprocessing.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/parallel-runner",
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
