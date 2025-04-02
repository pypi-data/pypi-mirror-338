from setuptools import setup, find_packages

setup(
    name="pismikroplib",  # Paket ismi
    version="0.1.0",  # Versiyon numarası
    author="h4t1ce",
    author_email="h4t1c3@pismikrops.com",
    description="Pismikroplar.",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),  # Paketleri otomatik bul
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
