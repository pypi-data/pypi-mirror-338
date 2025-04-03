from setuptools import setup, find_packages

setup(
    name="boruta-surv",  # Package name
    version="0.1.0",  # Initial version
    description="Feature Selection for Survival Analysis using Boruta",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Alexandre Calado",
    author_email="alexandreluiscalado@gmail.com",
    url="https://github.com/alterreal/boruta-surv",
    packages=find_packages(),  # Automatically finds the package
    install_requires=[
        "numpy",                
        "pandas",               
        "scipy",                
        "scikit-learn",         
        "scikit-survival",               
        "seaborn",              
        "matplotlib",           
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)