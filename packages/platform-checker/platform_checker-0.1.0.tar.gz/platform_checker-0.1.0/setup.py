from setuptools import setup, find_packages

setup(
    name="platform-checker",
    version="0.1.0",
    packages=find_packages(),
    author="Aditya Sriram",
    author_email="adisriram7777@gmail.com",
    description="A simple package for checking the platform type.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/platform_checker",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
