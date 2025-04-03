from setuptools import setup, find_packages

setup(
    name='ai2soft_automation',
    version='0.0.7',
    packages=['src', 'src.models', 'src.internals'],
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
