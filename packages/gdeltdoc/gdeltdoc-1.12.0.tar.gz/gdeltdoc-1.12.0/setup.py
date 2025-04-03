import setuptools

with open("requirements.txt", "r") as f:
    requirements = [line.replace("\n", "") for line in f.readlines()]

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("gdeltdoc/_version.py", "r") as g:
    version = "1.0.0"
    for line in g.readlines():
        if "version" in line:
            version = (
                line.split("=")[1].replace("\n", "").replace('"', "").replace(" ", "")
            )

setuptools.setup(
    name="gdeltdoc",
    version=version,
    author="Alex Whitehead-Smith",
    author_email="alex.me.smith@gmail.com",
    description="A client for the GDELT 2.0 Doc API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/alex9smith/gdelt-doc-api",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
)
