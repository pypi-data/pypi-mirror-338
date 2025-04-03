from setuptools import setup, find_packages


def readme():
    with open('README.md', 'r') as f:
        return f.read()


setup(
    name='dm-aiomysql',
    version='v0.1.5',
    author='dimka4621',
    author_email='mismartconfig@gmail.com',
    description='This is my custom aiomysql client',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://pypi.org/project/dm-aiomysql',
    packages=find_packages(),
    install_requires=[
        'dm-logger~=0.6.2',
        'python-dotenv>=1.0.0',
        'mysql-connector-python>=9.0.0, <10.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ],
    keywords='dm aiomysql',
    project_urls={
        'GitHub': 'https://github.com/MykhLibs/dm-aiomysql'
    },
    python_requires='>=3.8'
)
