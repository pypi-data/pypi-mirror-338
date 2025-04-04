from setuptools import setup, find_packages

setup(
    name="shareithub", 
    version="1.1.2",
    author="SHARE IT HUB",
    author_email="",
    description="Don't forget to subscribe to keep the channel growing",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/shareithub",  
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "shareithub=shareithub.cli:main",  
        ],
    },
)
