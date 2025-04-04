from setuptools import setup, find_packages
from pathlib import Path

# Tratamento seguro de arquivos
def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        print(f"Erro ao ler {filename}: {e}")
        return ""

page_description = read_file("README.md")
requirements = read_file("requirements.txt").splitlines()

setup(
    name="package_imagens",
    version="0.0.1", 
    author="Adrienne Siqueira",
    author_email="adrienne_siqueira97@hotmail.com",
    description="Um pacote para processamento básico de imagens",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DrySiqu3ira/simple-package-template",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
    license="MIT",
    keywords="imagens processamento opencv pil",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)