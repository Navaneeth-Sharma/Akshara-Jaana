import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="AksharaJaana", # Replace with your own username
    version="1.0.0.0",
    author="Navaneeth",
    author_email="navaneethsharma2310oct@gmail.com",
    description="A Kannada OCR",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Navaneeth-Sharma/Akshara-Jaana/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
