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
    install_requires=(
        # "tf-nightly-cpu>=2.5.0.dev20201122",
        # "tensorflow-cpu>=2.4.0rc", # for windows
        "tensorflow-cpu>=2.3.0", # for linux
        "numpy",
        "pypinyin",
        # "g2pM",
        "dataclasses"
    ),
    classifiers=(
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    )
)
