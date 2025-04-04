from setuptools import setup, find_packages

setup(
    name="my_package_hello_db",  # Your package name (should be unique on PyPI)
    version="0.1.0",  # Versioning (increase when updating)
    author="darshil",
    author_email="darshilbabariya444@gmail.com",
    description="A simple Python package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    # url="https://github.com/yourusername/my_package",  # GitHub repo (optional)
    packages=find_packages(),
    install_requires=[
        "flask"  # List dependencies here
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum Python version
)
