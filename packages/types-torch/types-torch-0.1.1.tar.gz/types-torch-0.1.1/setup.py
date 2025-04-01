from setuptools import setup, find_packages

setup(
    name="types-torch",
    version="0.1.1",
    package_dir={"": "src"},
    packages=["torch-stubs"],
    package_data={"torch-stubs": ["*.pyi", "*/*.pyi"]},
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
)
