from setuptools import setup, find_packages

setup(
    name="v2root",
    version="1.0.0",
    author="Sepehr0Day",
    author_email="sphrz2324@gmail.com",
    description="Simplify v2ray control with this Python package and native extensions",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/V2RayRoot/V2Root",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "v2root": ["lib/*"],  
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
        "Topic :: Internet :: Proxy Servers",
    ],
    python_requires=">=3.6",
    license="MIT",
    install_requires=[
        "colorama>=0.4.6",  
    ],
)