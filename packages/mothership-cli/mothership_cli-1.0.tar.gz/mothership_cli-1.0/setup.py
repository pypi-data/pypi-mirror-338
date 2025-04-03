from setuptools import setup, find_packages

setup(
    name="mothership_cli",
    version="1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mothership=mothership_cli.cli:main',
            'startup=mothership_cli.cli:main',
        ],
    },
    author="Your Name",
    description="Modular Python project CLI scaffolding tool",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
