from setuptools import setup, find_packages

setup(
    name="hotpod-cli",
    version="1.2.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A CLI tool for managing GCS instances",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/hotpod",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    package_data={
        "hotpod_cli": ["*.json","tasks/.gitkeep"],  # 包含 hotpod_cli 包下的所有 json 文件和tasks目录
    },
    include_package_data=True,     # 确保包含包数据
    install_requires=[
        "click",
        "click-help-colors",
        "click-spinner",
        "paramiko",
        "python-dotenv",
        "jdcloud-sdk",
        "requests",
        "paramiko",
        "litellm"
    ],
    entry_points={
        "console_scripts": [
            "hotpod=hotpod_cli.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.6",
)
