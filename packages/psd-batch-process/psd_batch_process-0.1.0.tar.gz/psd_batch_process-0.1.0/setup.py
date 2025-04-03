from setuptools import setup, find_packages

setup(
    name="psd_batch_process",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "pywin32>=306",
        "pandas>=2.1.1",
    ],
    author="Ocarina",
    author_email="Ocarina1024@gmail.com",
    description="A tool for batch updating text layers in PSD files using CSV data",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/psd_batch_process",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "psd-batch-process=psd_batch_process.cli:main",
        ],
    },
)
