from setuptools import setup, find_packages

setup(
    name="codemetrica",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add your package dependencies here
    ],
    author="Rafed Muhammad Yasir",
    author_email="rafed123@gmail.com",
    description="A package for calculating metrics and detecting code smells",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/sparklabOrg/codemetrica",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
)
