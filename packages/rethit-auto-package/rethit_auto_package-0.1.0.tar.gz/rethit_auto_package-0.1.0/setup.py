from setuptools import setup, find_packages

setup(
    name="rethit_auto_package",
    version="0.1.0",
    packages=find_packages(),
    install_requires=['packaging==24.2', 'requests==2.32.3', 'setuptools==78.1.0'],
    entry_points={
        'console_scripts': [
            'rethit_auto_package = rethit_auto_package.main:main',
        ],
    },
    python_requires='>=3.6',
    author="gigascake",
    author_email="gigascake@gmail.com",
    description="A CLI tool generated from source based python",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
