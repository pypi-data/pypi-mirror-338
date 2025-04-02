from setuptools import setup, find_packages

setup(
    name="python_to_cpp", 
    version="0.1.7",
    packages=find_packages(where='src'),
    package_dir={"": "src"}, 
    install_requires=[],
    entry_points={
        "console_scripts": [
            "python_to_cpp=python_to_cpp.__main__:main",
        ],
    },
    author="Singhom931",
    description="Convert Python To C++",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Singhom931/python_cpp",
    # python_requires=">=3.6",
)
