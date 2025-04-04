from setuptools import setup

setup(
    name="PyAutoPilot",  # Module name for pip install
    version="0.1.0",
    author="Aryan gupta",
    author_email="ludmj99@gmail.com",
    description="A module to automatically check and install missing imports",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/AryanGupta-234/PyAutoPilot",
    py_modules=["PyAutoPilot"],  # <-- Defines it as a single module
    install_requires=[],  # List dependencies if needed
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
