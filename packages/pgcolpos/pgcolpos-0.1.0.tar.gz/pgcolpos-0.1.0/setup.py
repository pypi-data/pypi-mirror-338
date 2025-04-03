from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pgcolpos",
    version="0.1.0",
    author="Latiful Mousom",
    author_email="latifulmousom@gmail.com",
    description="A tool to add or move columns to specific positions in PostgreSQL tables",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lmousom/pgcolpos",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
    install_requires=[
        "psycopg2-binary>=2.8.0",
    ],
    entry_points={
        "console_scripts": [
            "pgcolpos=pgcolpos.main:main",
        ],
    },
)