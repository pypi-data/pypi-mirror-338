from setuptools import setup, find_packages

setup(
    name='ai2soft.automation',
    version='0.0.5',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    description='用于完与一些自动化的操作',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='',
    author='ai2soft.cn',
    author_email='goldli@live.cn',
    license='MIT',
    install_requires=[
    ],
    classifiers=[
        'Programming Language :: Python :: 3.10',
    ]
)
