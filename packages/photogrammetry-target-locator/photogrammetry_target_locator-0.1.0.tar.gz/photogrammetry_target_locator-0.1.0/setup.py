from setuptools import setup, find_packages

setup(
    name="photogrammetry-target-locator",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Calculate real-world coordinates from camera images",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/photogrammetry-target-locator",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "numpy",
        "pyproj",
        "requests",
    ],
    entry_points={
        "console_scripts": [
            "phototarget=photogrammetry_target_locator.cli:cli",
        ],
    },
) 