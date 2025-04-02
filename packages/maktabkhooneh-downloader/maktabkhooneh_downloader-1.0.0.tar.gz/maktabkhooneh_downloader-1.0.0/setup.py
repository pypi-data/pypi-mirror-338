from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="maktabkhooneh-downloader",
    version="1.0.0",
    author="Aghil Padash",
    author_email="aghilpadash73@gmail.com",
    description="A command-line tool to download courses from Maktabkhooneh",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/aghilpadash/maktabkhooneh-downloader",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "httpx>=0.23.0",
        "pydantic>=1.10.2",
        "tqdm>=4.64.1",
        "lxml>=4.9.1",
        "python-dotenv>=0.21.0",
    ],
    entry_points={
        "console_scripts": [
            "maktabkhooneh-downloader=maktabkhooneh_downloader.cli:main",
        ],
    },
)
