# Adicione isto no início do arquivo
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages  # Adicione find_packages aqui
import pathlib

HERE = pathlib.Path(__file__).parent

# Substitua a leitura do README por:
try:
    with open(HERE / "README.md", encoding='utf-8') as f:
        README = f.read()
except Exception:
    README = "Calculadora Científica Avançada"  # Descrição fallback

setup(
    name="calculadora-cientifica",
    version="3.0.0",
    author="Leonardo Medeiros - LeoMedeiros72",
    author_email="xorao.lsm@gmail.com",
    description="Calculadora científica com operações avançadas",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/LeoMedeiros72/Calculadora-3.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "numpy>=1.26.0",
        "matplotlib>=3.8.0",
        "scipy>=1.11.0",
        "sympy>=1.12"
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Education",
    ],
    python_requires=">=3.12",
    keywords="calculadora matemática científica educação",
    project_urls={
        "Source": "https://github.com/LeoMedeiros72/Calculadora-3.0",
        "Bug Reports": "https://github.com/LeoMedeiros72/Calculadora-3.0/issues",
    },
)
