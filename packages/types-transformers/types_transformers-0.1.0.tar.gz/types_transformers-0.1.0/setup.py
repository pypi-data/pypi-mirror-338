from setuptools import setup, find_packages

setup(
    name="types-transformers",
    version="0.1.0",
    package_dir={"": "src"},
    packages=["transformers-stubs"],
    package_data={"transformers-stubs": ["*.pyi", "*/*.pyi"]},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
)