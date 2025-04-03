from setuptools import setup

requires = [
    "aiohttp>=3.0.0",
    "aiofiles>=0.7.0",
    "tqdm>=4.0.0",
]

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="rbino",
    version="1.0.2",
    author="AminEbrahimi",
    author_email="SinyorAmin@gmail.com",
    description="Rubino Library for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    keywords=[
        "rubika",
        "bot",
        "rubino",
        "robot",
        "library",
        "rubikalib",
        "rbino",
        "Rubika",
    ],
    url="https://t.me/MeAminCoder",
    packages=["rbino"],
    install_requires=requires,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)