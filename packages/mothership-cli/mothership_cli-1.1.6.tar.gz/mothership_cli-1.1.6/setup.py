from setuptools import setup, find_packages

setup(
    name="mothership-cli",
    version="1.1.6",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mothership=mothership_cli.cli:main',
            'startup=mothership_cli.cli:main',
        ],
    },
    author="Nikolai Janiszewsky",
    description="Modular Python project scaffolding CLI for rapid startup and deployment",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
