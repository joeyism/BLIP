from setuptools import find_packages, setup

setup(
    name="blip-model", 
    version="v1.0.0",
    packages=find_packages(exclude=["tests"]),
    install_requires=[line.replace("\n", "") for line in open("requirements.txt", "r").readlines()],
    entry_points={
    },
    package_data={
    },
)
