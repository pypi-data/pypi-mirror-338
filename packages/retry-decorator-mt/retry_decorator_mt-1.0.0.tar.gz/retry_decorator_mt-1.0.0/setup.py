from pathlib import Path

from setuptools import setup, find_packages


# read the contents of your README file

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()


setup(
    name="Retry Decorator",
    description="Decorator to retry a callable if a given error is catched",
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    setuptools_git_versioning={"enabled": True},
    setup_requires=[
        "flake8",
        'setuptools',
        'setuptools-git-versioning',
        'wheel',
    ],
)
