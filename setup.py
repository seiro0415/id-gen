from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="id-gen",
    version="0.1.0",
    author="X",
    author_email="x@x",
    description="A simple ID generator with various options",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://x/id-gen",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "id-gen=id_gen.cli:main",
        ],
    },
)
