from setuptools import setup, find_packages

setup(
    name="ukaddress",
    version="0.1.0",
    author="Syed Ali Hamza Shah",
    author_email="sahamzashah19@gmail.com",
    description="Generate and parse realistic UK addresses.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["faker"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
