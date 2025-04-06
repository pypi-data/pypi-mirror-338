from setuptools import setup, find_packages

setup(
    name="retroPySim",
    version="0.0.1",
    packages=find_packages(),
    install_requires=[],
    author="---",
    author_email="retropy@respawnin.com",
    description="retroPySim - a Python simulator for retroPy, a micro-python retro game engine for the RP2350 micro-controller. ",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://www.retropy.io/",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)