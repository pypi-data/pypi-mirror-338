from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="mlsimplified",
    version="0.1.0",
    author="Ethan Zhang",
    author_email="ethan.zhang@example.com",
    description="A production-ready machine learning library for quick model training and prediction",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ethanzhang/mlsimplified",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.3.0",
        "numpy>=1.21.0",
        "scikit-learn>=1.0.0",
        "matplotlib>=3.4.0",
        "seaborn>=0.11.0",
        "joblib>=1.0.0",
        "setuptools>=65.5.1",
    ],
    keywords="machine learning, data science, scikit-learn, pandas, numpy",
    project_urls={
        "Bug Reports": "https://github.com/ethanzhang/mlsimplified/issues",
        "Source": "https://github.com/ethanzhang/mlsimplified",
    },
) 