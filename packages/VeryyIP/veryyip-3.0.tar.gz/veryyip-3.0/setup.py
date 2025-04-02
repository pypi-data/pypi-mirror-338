from setuptools import setup, find_packages

setup(
    name="VeryyIP",  # Your package name
    version="3.0",  # Package version
    description="A Python library for handling IP addresses (local and public) with OS-specific commands",
    author="Xscripts Inc.",
    author_email="sunnyplaysyt9@gmail.com",
    license="MIT",
    long_description=open('README.md').read(),  # Reads the README file for long description
    long_description_content_type="text/markdown",  # Type of the content in the README
    url="",  # Your project URL if you have one
    packages=find_packages(),  # Automatically find and include all packages
    include_package_data=True,  # Includes other data files
    package_data={
        "veryyip": ["config/*.cfg", "docs/*.md"],  # Example of including non-Python files
    },
    python_requires=">=3.6",  # Minimum Python version required
    extras_require={
        "dev": ["pytest", "sphinx"],  # Development dependencies
    },
)
