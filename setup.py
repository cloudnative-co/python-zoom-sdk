from setuptools import setup, find_packages

setup(
    name="ZoomSDK",
    version="0.0.1",
    description="Python SDK for Python 3.6",
    author="sebastian",
    author_email="seba@cloudnative.co.jp",
    packages=find_packages(),
    install_requires=[
        "jsonschema"
    ],
    entry_points={
        "console_scripts": [
        ]
    },
)
