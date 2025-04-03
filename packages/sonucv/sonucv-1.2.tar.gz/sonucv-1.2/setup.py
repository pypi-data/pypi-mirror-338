from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="sonucv",
    version="1.2",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "resumeviewer=sonucv.resume:interactive",  # Entry point
        ],
    },
    author="Sonu Kr Sahani",
    author_email="sahanix7@gmail.com",
    description="A Python package that displays my resume in the terminal",
    long_description=long_description,  # Adding long description
    long_description_content_type="text/markdown",  # Specifies markdown format
    url="https://github.com/sonusahani/sonucv",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
