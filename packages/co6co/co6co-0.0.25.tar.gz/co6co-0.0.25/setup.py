# -*- coding:utf-8 -*-
from setuptools import setup, find_packages
from co6co import setupUtils

long_description = setupUtils.readme_content(__file__)
version = setupUtils.get_version(__file__)
packagesName, packages = setupUtils.package_name(__file__, exclude=["tests"])
p = find_packages(exclude=())
print("test", p)
setup(
    name=packagesName,
    version=version,
    description="基础模块",
    packages=p,
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    include_package_data=True, zip_safe=True,
    exclude_package_data={
        '': ['tests/*']
    },
    # 依赖哪些模块
    install_requires=[],
    # package_dir= {'utils':'src/log','main_package':'main'},#告诉Distutils哪些目录下的文件被映射到哪个源码
    author='co6co',
    author_email='co6co@qq.com',
    url="http://git.hub.com/co6co",
    data_file={
        ('', "*.txt"),
        ('', "*.md"),
    },
    package_data={
        '': ['*.txt', '*.md'],
        'bandwidth_reporter': ['*.txt']
    }
)
