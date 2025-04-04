from setuptools import setup, find_packages

setup(
    name='euler-swarm',
    version='0.2.1',
    author='Atharv Patawar',
    description='A tool for building dependency graphs and generating code documentation using muliple agents.',
    packages=find_packages(),
    install_requires=[
         'networkx',
         'matplotlib',
         'openai',
         'python-dotenv'
    ],
    entry_points={
         'console_scripts': [
             'euler-swarm=euler_swarm.main:main'
         ]
    },
    classifiers=[
         'Programming Language :: Python :: 3',
         'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)