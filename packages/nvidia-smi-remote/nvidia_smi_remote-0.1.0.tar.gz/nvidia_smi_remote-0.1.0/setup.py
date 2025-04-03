from setuptools import setup

setup(
    name="nvidia-smi-remote",
    version="0.1.0",
    description="CLI tool to query GPU status locally and remotely (based on nvidia-smi)",
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
