from setuptools import setup, find_packages

setup(
    name="mle_nl2query",
    version="0.1.3",
    packages=find_packages(),
    author="Palistha Deshar",
    author_email="palisthadeshar@gamil.com",
    description="A short description of your project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/RamailoTech/mle_nl2query",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
