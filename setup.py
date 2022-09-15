from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='clia',
    description='CLIA - Command Line Intelligent Assistant',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.1.1',
    license='MIT',
    author="Gautam Rajeev Singh",
    author_email='gautamsingh1997@gmail.com',
    url='https://github.com/singhgautam7/CLIA---Command-Line-Intelligent-Assistant',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    py_modules=["cli", "constants", "regex"],
    keywords='pyton cli assistant',
    python_requires=">=3.6",
    install_requires=["colorama", "rich", "shellingham", "typer"],
)
