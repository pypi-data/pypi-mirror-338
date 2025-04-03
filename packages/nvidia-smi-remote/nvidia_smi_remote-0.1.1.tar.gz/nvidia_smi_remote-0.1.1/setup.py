from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nvidia-smi-remote",
    version="0.1.1",
    description="CLI tool to query GPU status remotely (based on nvidia-smi)",
    long_description=long_description,
    long_description_content_type="text/markdown", 
    author="HEEWON KIM",  
    author_email="ive2go@naver.com", 
    packages=["nvidia_smi_remote"],
    python_requires=">=3.8",
    license="MIT",
    install_requires=[
        "paramiko",
        "blessed",
    ],
    entry_points={
        "console_scripts": [
            "nvidia-smi-remote=nvidia_smi_remote.main:main",
        ],
    },
)