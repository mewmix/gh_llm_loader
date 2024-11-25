from setuptools import setup, find_packages

setup(
    name="gh_llm_loader",
    version="0.1.2",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'gh-llm-loader=gh_llm_loader.cli:main',
        ],
    },
)
