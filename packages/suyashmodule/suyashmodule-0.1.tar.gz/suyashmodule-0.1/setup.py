from setuptools import setup

setup(
    name="suyashmodule",
    version="0.1",
    py_modules=["mymodule"],  # This is important for single-file modules
    author="Suyash Guliani",
    author_email="gulianisuyash@gmail.com",
    description="A simple greeting module",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
