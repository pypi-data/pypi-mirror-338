from setuptools import setup, find_packages

setup(
    name="pycloudmesh",
    version="0.1.3",
    author="Nithesh",
    author_email="nitheshkg18@gmail.com",
    description="A package that exposes the cost API data for AWS, Azure, and GCP",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NitheshKG/cloudmesh",
    packages=find_packages(),
    install_requires=[
        "boto3",
        "requests",
        "google",
        "google-cloud-billing"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
