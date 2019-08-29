import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gatherup-sdk",
    version="1.0.0",
    author="GatherUp",
    author_email="lucas@gatherup.com",
    description="GatherUp SDK",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://app.gatherup.com/api/doc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 
