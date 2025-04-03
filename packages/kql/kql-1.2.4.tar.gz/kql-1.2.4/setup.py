from setuptools import setup, find_packages

setup(
    name="kql",  # ✅ Unique package name
    version="1.2.4",  # Start with version 0.1.0
    packages=find_packages(),
    install_requires=["requests"],  # List dependencies
    author="STEIN",
    author_email="devilsteinshorts@gmail.com",
    description="A Python package for user info, username generation, Instagram checking, and email validation.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/steinlurks",  # Change this to your actual GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
