from setuptools import setup, find_packages

setup(
    name="sonucv",  # Package name is 'sonucv'
    version="1.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "resumeviewer=sonucv.resume:show_resume",  # Command to run the resume
        ],
    },
    author="Sonu kr Sahani",
    author_email="sahanix7@gmail.com",
    description="A Python package that displays my resume in the terminal",
    url="https://github.com/yourusername/sonucv",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
