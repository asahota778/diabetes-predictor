# setup.py
from setuptools import setup, find_packages

setup(
    name='diabetes_predictor',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'scikit-learn',
        'numpy'
    ],
    entry_points={
        'console_scripts': [
            'diabetes-predictor=diabetes_predictor:main',
        ],
    },
)
