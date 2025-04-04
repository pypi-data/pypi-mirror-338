from setuptools import setup, find_packages

"""
:author: abuztrade
:license: MIT License, see LICENSE file.
:copyright: (c) 2025 by abuztrade.
"""


version = '0.0.2'

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="fkassa",
    version=version,

    author="abuztrade",
    author_email="abuztrade.work@gmail.com",

    url="https://github.com/makarworld/fkassa.git",
    download_url=f"https://github.com/makarworld/fkassa/archive/refs/tags/v{version}.zip",

    description="FreeKassa Python SDK",

    packages=['fkassa'],
    install_requires=['requests', 'pydantic'],

    license='MIT License',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Topic :: Communications :: Email",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",

        "Intended Audience :: Developers",
        "Intended Audience :: Customer Service",
        "Intended Audience :: Financial and Insurance Industry",
    ],
    include_package_data=True, # for MANIFEST.in
    python_requires='>=3.6.0',
    package_data={
        package: [
            "py.typed",
            "*.pyi",
            "**/*.pyi",
            "web/*",
            "_async/*"
        ] for package in find_packages()
    },
    zip_safe=False,

    project_urls={
        "Bug Reports": "https://github.com/makarworld/fkassa/issues",
        "Source": "https://github.com/makarworld/fkassa",
    },

    keywords=['freekassa', 'freekassa api', 'freekassa ru', 'freekassa com', 'freekassa net', 'freekassa ru'],
    
)