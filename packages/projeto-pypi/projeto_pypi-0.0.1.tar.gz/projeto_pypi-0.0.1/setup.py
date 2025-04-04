from setuptools import setup, find_packages

setup(
    name="projeto-pypi", 
    version="0.0.1",
    author="Seu Nome",
    author_email="seuemail@example.com",
    description="Um pacote simples para testes no PyPI",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/LeonardoCigarra/projeto_pypi", 
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
