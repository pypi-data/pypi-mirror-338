from setuptools import setup, find_packages

setup(
    name="vhub",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    entry_points={
        'console_scripts': [
            'vh=vhub.cli:main',
        ],
    },
    author="Pavel",
    author_email="asuraspru@gmail.com",
    description="vHub - A Git-like version control system",
    keywords="version control, git",
    python_requires=">=3.6",
)