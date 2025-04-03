from setuptools import setup, find_packages

setup(
    name="aisec-sdk",
    version="0.1.0",
    description="AI应用安全SDK，用于检测会话中的prompt注入等恶意攻击行为",
    author="安全团队",
    author_email="anquan@ly.com",
    packages=find_packages(),
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.1",
) 