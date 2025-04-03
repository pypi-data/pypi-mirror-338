from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="quimerax",
    version="0.1.2",
    author="QuimeraX Intelligence",
    author_email="support@quimerax.com",
    description="SDK Python para a API da QuimeraX",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://docs.quimerax.com",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.31.0",
        "python-dotenv>=1.0.0",
    ],
) 