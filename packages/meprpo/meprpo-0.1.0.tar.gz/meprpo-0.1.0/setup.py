from setuptools import setup, find_packages

setup(
    name="meprpo",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "matplotlib",
        "scipy",
        "requests"
    ],
    author="Jozef Lauko",
    author_email="laukojozef1@gmail.com",
    description="Measuring predictive potential in graph databases",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jozef-Lauko/Measuring-predictive-potential-in-graph-databases",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
