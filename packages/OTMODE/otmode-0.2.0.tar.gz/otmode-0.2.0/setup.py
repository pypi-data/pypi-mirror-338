from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="OTMODE",  
    version="0.2.0",  
    author="Lanks Huidong Su",  
    author_email="u3010549@conect.hku.hk",  
    description="OTMODE is a computational framework built on Optimal Transport (OT) theory for improving cell-type annotation accuracy and for identifying differential features across conditions in single-cell multi-omics data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Eggong/OTMODE",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # Minimum Python version supported
    install_requires=["POT==0.9.5",
                      "anndata>=0.10.9"],
    include_package_data=True,  # Important to include files listed in MANIFEST.in
    license="MIT",
    zip_safe=False,
)
