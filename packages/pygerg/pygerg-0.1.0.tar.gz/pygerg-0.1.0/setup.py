from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pygerg",
    version="0.1.0",
    author="Tijs van der Velden",
    author_email="tijsvdvelden@hotmail.com", 
    description="Python implementation of the GERG-88 standard for natural gas properties",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/safersephy/pygerg", 
    project_urls={
        "Bug Tracker": "https://github.com/safersephy/pygerg/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    packages=find_packages(),
    python_requires=">=3.7",
)