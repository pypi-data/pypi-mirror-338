from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="postman-to-pytest",
    version="1.0.0",
    author="Barun Yadav",
    author_email="benz3k3@gmail.com",
    description="A tool to convert Postman collections to pytest test files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/benz1k1/postman-to-pytest",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "postman-to-pytest=postman_to_pytest:main",
        ],
    },
) 