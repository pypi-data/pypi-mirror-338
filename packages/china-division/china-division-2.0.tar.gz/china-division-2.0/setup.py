from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="china-division",
    version="2.0",
    author="wangxueming",
    author_email="zgxdxf@hotmail.com",
    description="中国行政区划查询工具",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zgxdxf/china-division",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    keywords="china administrative division",

)

project_urls={
    "旧版项目": "https://pypi.org/project/chinese_administrative_divisions/",
}