from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="aminpy",
    version="1.0.3",
    author="Amin Ebrahimi",
    author_email="sinyoramin@gmail.com",
    description="A Python library - rubino",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://t.me/MeAminCoder/3",
    packages=["aminpy"],
    install_requires=[
        "aiohttp>=3.11.15",
        "aiofiles>=24.1.0",
        "tqdm>=4.67.1"
    ],
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    keywords=["rubika", "api", "bot", "aminpy"],
)