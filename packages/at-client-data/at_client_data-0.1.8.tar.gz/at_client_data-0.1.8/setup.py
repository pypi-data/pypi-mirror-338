from setuptools import setup, find_packages

setup(
    name="at-client-data",
    version="0.1.8",
    description="AT Data Client API",
    author="AT",
    author_email="info@at.com",
    package_dir={"at_client_data": "app"},
    packages=["at_client_data", "at_client_data.client"],
    python_requires=">=3.8",
    install_requires=[
        "aiohttp>=3.11.0,<4.0.0",
        "tenacity>=9.0.0,<10.0.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)