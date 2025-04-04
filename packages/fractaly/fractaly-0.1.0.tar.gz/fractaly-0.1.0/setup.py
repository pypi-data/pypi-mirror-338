from setuptools import setup, find_packages

setup(
    name="fractaly-package",
    version="1.0.0",  # Should match __version__
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "fractaly": ["py.typed", 'lib/*.dll', 'lib/*.so'],  # Include type information
    },
    python_requires=">=3.7",
    install_requires=[
        # List your dependencies here
        # "numpy>=1.20.0",
        # "pandas>=1.3.0",
    ],
    author="Masoud NAJAFI",
    author_email="name.surname@gmail.com",
    description="A package for fractal creation and display",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/masoud-najafi/fractaly-project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Typing :: Typed",
    ],
)