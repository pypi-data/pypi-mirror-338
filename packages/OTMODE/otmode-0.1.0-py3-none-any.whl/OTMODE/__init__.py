from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirement.txt", "r", encoding="utf-8") as fh:
    requirements = fh.read()

setup(
    name="OTMODE",  # Replace with your package name
    version="0.1.0",  # Start with a version number like 0.1.0
    author="Lanks Huidong Su",  # Replace with your name
    author_email="u3010549@conect.hku.hk",  # Replace with your email
    description="OTMODE is a computational framework built on Optimal Transport (OT) theory for improving cell-type annotation accuracy and for identifying differential features across conditions in single-cell multi-omics data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eggong/OTMODE",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # Replace with your license
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # Minimum Python version supported
    install_requires=requirements,
)