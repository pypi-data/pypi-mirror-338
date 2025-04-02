from setuptools import setup, find_packages

setup(
    name="cnmpdk",        # Replace with your package name
    version="0.2.0",              # Replace with your package version
    packages=find_packages(),
    package_data={'cnmpdk': ['ip_blocks/*', 'pcells/*', 'klayout/*', '*.yaml']},
    install_requires=[
        "gdsfactory>9.0.0",
    ],
    author="Mario Mejias",
    author_email="mario.mejias@vlcphotonics.com",
    description="CNM PDK for gdsfactory",
    long_description="",
    long_description_content_type="text/markdown",
    url="https://github.com/mario26z/cnm.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
)
