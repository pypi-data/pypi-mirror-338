from setuptools import setup, find_packages

setup(
    name="cgraaaj-discord-notifier",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    author="cgraaaj",
    author_email="cgraaaj@example.com",
    description="A simple Python library for sending Discord notifications.",
    url="https://github.com/cgraaaj/python-discord-notifier",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
