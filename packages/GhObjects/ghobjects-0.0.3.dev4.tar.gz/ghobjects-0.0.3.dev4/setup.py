from setuptools import setup, find_packages

setup(
    packages=find_packages(),
    exclude_package_data={'': ['__pycache__/*']},
)