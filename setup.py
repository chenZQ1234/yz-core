#!/usr/bin/python3.7+
# -*- coding:utf-8 -*-
import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yz-core",  # Replace with your own username
    version="0.2.1",
    author="lxm",
    author_email="luoyuren13@gmail.com",
    description="An ID generator for distributed microservices",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lixuemin13/yz-core.git",
    packages=setuptools.find_packages(),
    package_data={'yzcore': [
        'templates/project_template/*',
        'templates/project_template/docs/*',
        'templates/project_template/migrations/*',
        'templates/project_template/src/*',
        'templates/project_template/src/apps/*',
        'templates/project_template/src/conf/*',
        'templates/project_template/src/const/*',
        'templates/project_template/src/tests/*',
        'templates/project_template/src/utils/*',
        'templates/project_template/.gitignore',
    ]},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6.8',
    install_requires=[
        "fastapi>=0.68.1",
        "uvicorn>0.13",
        "yzrpc>=0.1",
        "nacos-sdk-python==0.1.6"
    ],
    entry_points={
        'console_scripts': [
            'yzcore=yzcore.__main__:main'
        ],
    },
    extras_require={
        'rpc': ['yzrpc>=0.1'],
        'oss-aliyun': ['oss2>=2.13.0, !=3.0.0'],
        'oss-huawei': ['esdk-obs-python==3.20.11'],
        'oss-aws': ['boto3==1.17.27'],
    }
)
