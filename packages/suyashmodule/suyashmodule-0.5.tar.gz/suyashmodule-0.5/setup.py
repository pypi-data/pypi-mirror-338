from setuptools import setup

setup(
    name="suyashmodule",  # Make sure this is the new name
    version="0.5",
    py_modules=["mymodule"],
    author="Suyash Guliani",
    author_email="gulianisuyash@gmail.com",
    description="A simple greeting module",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
