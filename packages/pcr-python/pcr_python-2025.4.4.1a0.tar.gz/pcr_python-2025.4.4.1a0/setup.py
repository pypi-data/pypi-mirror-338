from setuptools import setup, find_packages

setup(
    name="pcr_python",
    version="2025.04.04.1-alpha",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
)
