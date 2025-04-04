# setup.py
from setuptools import setup, find_packages

setup(
    # name="mymath",  # 包名
    name="dtmymath",  # 包名
    version="0.1.0",  # 版本号
    author="Your Name",  # 作者名
    author_email="your.email@example.com",  # 作者邮箱
    description="A simple math toolkit",  # 简短描述
    long_description=open("README.md").read(),  # 读取 README 作为详细描述
    long_description_content_type="text/markdown",  # README 文件格式
    url="https://github.com/yourusername/mymath",  # 项目主页（可选）
    packages=find_packages(),  # 自动找到所有包
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # 支持的 Python 版本
)