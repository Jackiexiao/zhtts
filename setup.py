from setuptools import setup, find_packages


setup(
    name='zhtts',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/jackiexiao/zhtts',
    license='MIT',
    author='jackiexiao',
    author_email='707610215@qq.com',
    description="A demo of zh/Chinese Text to Speech system run on CPU",
    long_description=open("README.md", 'r', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=(
        "tensorflow-cpu>=2.4.0",
        "numpy",
        "scipy",
        "pypinyin",
        "dataclasses"
    ),
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    )
)
