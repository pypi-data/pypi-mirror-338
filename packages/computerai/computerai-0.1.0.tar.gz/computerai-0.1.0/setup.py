from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="computerai",
    version="0.1.0",
    author="Lawrence Chen",
    author_email="your.email@example.com",
    description="Framework for creating computer use agents",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/computerai",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
