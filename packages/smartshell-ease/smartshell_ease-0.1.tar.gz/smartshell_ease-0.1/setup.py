from setuptools import setup, find_packages

setup(
    name="smartshell-ease",  # Package name
    version="0.1",
    packages=find_packages(),
    include_package_data=True,  # Include non-Python files
    package_data={
        "smartshell_ease": ["commands.json"],  # Ensure commands.json is inside the package
    },
    install_requires=[
        "click",
        "colorama",
        "rich",
        "requests",
        "rapidfuzz",
        "openai",
        "ollama",
        "pyreadline3",
    ],
    entry_points={
        "console_scripts": [
            "smartshell=smartshell_ease.smartshell:cli",  # Link CLI command
        ],
    },
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",  # Specify markdown for README.md
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
