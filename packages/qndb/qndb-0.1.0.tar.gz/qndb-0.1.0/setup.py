from setuptools import setup, find_packages

setup(
    name="qndb",
    version="0.1.0",
    author="Abhishek Panthee",
    author_email="contact@abhishekpanthee.com.np",
    description="A quantum database implementation",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/abhishekpanthee/quantum-database",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Database",
        "Topic :: Scientific/Engineering :: Physics",
    ],
    python_requires=">=3.6",
    install_requires=[
        "cirq",
        "numpy",
        "pandas",
        "matplotlib",
        "memory_profiler",
        "pytest",   # For testing
    ],
    include_package_data=True,
    package_data={
        "": ["examples/*.py"],
    },
)