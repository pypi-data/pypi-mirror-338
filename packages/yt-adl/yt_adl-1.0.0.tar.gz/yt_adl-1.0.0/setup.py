from setuptools import setup, find_packages

setup(
    name="yt-adl",
    version="1.0.0",
    author="Avinion",
    author_email="shizofrin@gmail.com",
    description="YouTube Audio and Video Downloader with advanced features",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://x.com/Lanaev0li",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        'yt-dlp',
        'colorama',
        'tqdm',
        'mutagen',
        'pydub'
    ],
    entry_points={
        'console_scripts': [
            'yt-adl=yt_adl.cli:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)