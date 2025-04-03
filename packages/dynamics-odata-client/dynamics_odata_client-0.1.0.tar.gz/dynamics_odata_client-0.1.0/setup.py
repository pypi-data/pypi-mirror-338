from setuptools import setup, find_packages

# Leer contenido del README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dynamics_odata_client",
    version="0.1.0",
    author="AlbertoDR",
    description="Cliente OData para Dynamics 365 con autenticación y exportación a DataFrame",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AlbertoDuranR/dynamics_odata_client",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "python-dotenv"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)