from setuptools import setup, find_namespace_packages

setup(
    name="cognyx-bom-sdk",
    version="0.1.0",
    description="Cognyx BOM SDK",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Cognyx",
    license="MIT",
    python_requires=">=3.8",
    package_dir={"": "src"},
    packages=find_namespace_packages(where="src"),
    install_requires=[
        "pydantic>=2.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url="https://github.com/cognyx/cognyx-bom-sdk",
    project_urls={
        "Bug Tracker": "https://github.com/cognyx/cognyx-bom-sdk/issues",
    },
)
