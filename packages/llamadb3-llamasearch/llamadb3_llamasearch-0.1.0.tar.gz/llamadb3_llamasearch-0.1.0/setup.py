from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="llamadb3-llamasearch",
    version="0.1.0",
    author="LlamaSearch AI",
    author_email="nikjois@llamasearch.ai",
    description="Database management and query optimization library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://llamasearch.ai",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "typing_extensions; python_version < '3.8'",
    ],
    extras_require={
        "sqlite": [],  # No additional dependencies for SQLite
        "mysql": ["pymysql>=1.0.2"],
        "postgresql": ["psycopg2>=2.9.3"],
        "all": ["pymysql>=1.0.2", "psycopg2>=2.9.3"],
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=3.0.0",
            "black>=22.1.0",
            "isort>=5.10.1",
            "flake8>=4.0.1",
            "mypy>=0.940",
        ],
    },
) 