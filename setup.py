from setuptools import setup, find_packages

setup(
    name="olivia_dataset",
    version="1.0.0",
    description="Olivia Dataset: Multi-Domain COVID-19 Region-based Features",
    url="https://github.com/shayanfazeli/olivia_dataset",
    author="Shayan Fazeli",
    author_email="shayan@cs.ucla.edu",
    license="Apache",
    classifiers=[
        'Intended Audience :: Science/Research',
        #'Development Status :: 1 - Beta',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering :: Artificial Intelligence'
    ],
    keywords="machine learning,coronavirus,deep learning,inference",
    packages=find_packages(),
    python_requires='>3.6.0',
    scripts=[
        'olivia_dataset/bin/olivia_dataset_config',
        'olivia_dataset/bin/olivia_dataset_refresh'
    ],
    install_requires=[
    ],
    zip_safe=False
)
