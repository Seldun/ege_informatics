from setuptools import setup, find_packages

setup(
    name='ege_informatics',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.26.0',
        'pandas>=2.0.3'
    ],
    entry_points={
        'console_scripts': [
            'run-task=ege.type_01.solutions.task_01:main'
        ]
    }
)
