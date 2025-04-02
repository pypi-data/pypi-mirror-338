from setuptools import setup, find_packages

setup(
    name="mypackage_nayana",  # Make sure this is updated
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    author="Your Name",
    description="A sample Python package",
    license="MIT",
)
