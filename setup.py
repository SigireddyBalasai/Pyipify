from setuptools import setup
import pathlib
import os

dir_path = os.path.dirname(os.path.realpath(__file__))


def readme() -> str:
    """This will read the readme file"""
    with open(r"README.md") as f:
        readme_data = f.read()
    return readme_data


def reqs():
    """THis will read the requirements file"""
    print(dir_path)
    with open(str(pathlib.Path(dir_path) / "requirements.txt"), "r") as f:
        requirements = [line.strip() for line in f]
        return requirements


setup(
    name="PyIpify",
    packages=['PyIpify', 'PyIpify.synchronous', 'PyIpify.asynchronous'],
    version="0.0.1",
    setup_requires=['setuptools_scm'],
    license="MIT",
    description="A simple python library to find the public ip address of the system.",
    author="SigireddyBalasai",
    author_email="sigireddybalasai@gmail.com",
    url="https://github.com/SigireddyBalasai/ipify",
    download_url="https://github.com/SigireddyBalasai/AsyncPywhatKit/archive/refs/tags/1.0.tar.gz",
    keywords=["ipify", "ip", "ip address", "ipify.org", "ipify api", "ipify python", "ipify python library",
              "ipify python api", "ipify python library", "ipify python api", "ipify python package", "ipify",
              "ipify cli", "ipify asynchronous", 'ipify synchronous'],
    install_requires=reqs(),
    include_package_data=True,
    long_description=readme(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
