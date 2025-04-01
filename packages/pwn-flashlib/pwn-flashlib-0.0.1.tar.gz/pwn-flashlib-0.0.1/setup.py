from setuptools import setup, find_packages

setup(
    name="pwn-flashlib",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],  # Add dependencies here
    author="TheFlash2k",
    author_email="alitaqi2000@gmail.com",
    description="A wrapper around pwntools for more abstraction and stuff that I really use",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/theflash2k/flashlib",  # Update this if you have a GitHub repo
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
