from setuptools import find_packages, setup

setup(
    name="id-gen",
    version="0.1.0",
    packages=find_packages(),
    python_requires=">=3.12",
    entry_points={
        "console_scripts": [
            "id-gen=id_gen.cli:main",
        ],
    },
)
