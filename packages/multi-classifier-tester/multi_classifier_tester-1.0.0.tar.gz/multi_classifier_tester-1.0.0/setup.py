from setuptools import setup, find_packages

import multi_classifier_tester

with open('README.md','r',encoding='utf-8') as f:
    long_desc = f.read()

setup(
    name="multi-classifier-tester",
    version=multi_classifier_tester.__version__,
    author='Arı Bilgi Ogr',
    author_email='aribilgiogr@gmail.com',
    description='Multi-Classifier Tester for your classification data',
    long_description=long_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/aribilgiogr/multi-classifier-tester',
    packages=find_packages(),
    install_requires =[
        "lightgbm==4.6.0",
        "numpy==2.2.4",
        "pandas==2.2.3",
        "scikit-learn==1.6.1",
        "xgboost==3.0.0"
    ],
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.7",
)