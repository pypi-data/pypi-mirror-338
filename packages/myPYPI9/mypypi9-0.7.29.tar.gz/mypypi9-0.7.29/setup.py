from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="myPYPI9",
    version="0.7.29",  # Increment this for future updates
    author="timenet2300",
    author_email="endersu@outlook.com",
    description="A lightweight Python library for prime number operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/myNKUST/myprimelib9b",
    packages=find_packages(where="src"),  # Better package discovery
    package_dir={"": "src"},  # Standard src layou#t
    license_files=["LICENSE"],  # Explicit license file declaration
    install_requires=[],  # Add dependencies if needed
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires=">=3.6",
    keywords='primes mathematics algorithms',
    project_urls={
        "Documentation": "https://github.com/myNKUST/myprimelib9b/wiki",
        "Source": "https://github.com/myNKUST/myprimelib9b",
    },
)
