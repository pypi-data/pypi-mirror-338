"""
Setup configuration for kalX package.
"""

from setuptools import setup, find_packages

setup(
    name="kalx",
    version="1.0.0",
    packages=find_packages("src"),
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "kalx=kalx.__main__:main",
        ],
    },
    install_requires=[
        "firebase-admin>=5.0.0",
        "rich>=10.0.0",
        "prompt_toolkit>=3.0.0", 
        "cryptography>=3.4.0",
        "python-dotenv>=0.19.0",
        "requests>=2.25.0",
        "pynput>=1.8.1"
    ]
)
