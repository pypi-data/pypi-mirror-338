from setuptools import setup, find_packages

import merhaba_dunya

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="merhaba-dunya",
    version=merhaba_dunya.__version__,
    author="Arı Bilgi Ogr",
    author_email="aribilgiogr@gmail.com",
    description="Basit bir merhaba dünya paketi",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aribilgiogr/merhaba-dunya",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7",
    install_requires=[
        # Zorunlu bağımlılıkları buraya ekliyoruz,
        # "requests>=2.0",
    ]
)
