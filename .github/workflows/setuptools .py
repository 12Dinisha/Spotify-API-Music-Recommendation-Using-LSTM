from setuptools import setup, find_packages

setup(
    name="your_project",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask==2.0.2",
        "requests==2.26.0",
        "numpy==1.21.2",
        "pandas==1.3.3",
        "scikit-learn==0.24.2"
    ],
)


