from setuptools import setup, find_packages

def read_requirements():
     with open("requirements.txt", "r") as f:
         return f.read().splitlines()


setup(
    name="AbhiMusicPlug",
    version="1.1.0",
    author="AbhiShek",
    author_email="abhishekbanshiwal2005@gmail.com",
    description="A Telegram Music Plugin System",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/NotRealAbhi/Plugins",
    packages=find_packages(),
    install_requires=[
    "pyrofork",
    "py-tgcalls",
    "youtube-search-python",
    "yt-dlp",
    "tgcrypto",
    "httpx",
    "speedtest-cli",
    "ffprobe",
],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.9",
)
