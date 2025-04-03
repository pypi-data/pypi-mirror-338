from setuptools import setup, find_packages

setup(
    name="okrequest",
    version="0.0.1",
    packages=find_packages(),
    package_data={
        'okrequest': ['*.dll', '*.so', '*.h', 'libs/*'],
    },
    description="一个类似 requests 的 HTTP 客户端库，基于 Go 实现",
    author="",
    author_email="",
    url="",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        # 在这里添加你的依赖
    ]
)