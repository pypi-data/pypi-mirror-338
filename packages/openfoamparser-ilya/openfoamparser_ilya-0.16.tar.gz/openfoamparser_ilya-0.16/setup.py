from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='openfoamparser_ilya',
    version='0.16',
    description='Lightweight library to parse OpenFOAM files using Numpy (Ofpp Fork)',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://www.ccs-labs.org/',
    author='CCS-Labs',
    author_email='ilyarozhkov010@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='openfoam cfd parser',
    packages=['openfoamparser'],
    python_requires='>=3.7',
    install_requires=['numpy'],
    project_urls={
        'Parent Project Description': 'https://www.forschung-it-sicherheit-kommunikationssysteme.de/projekte/mamoko',
        'Source': 'https://github.com/resi2311/openfoamparser.git',
        'Forked from': 'https://github.com/ApolloLV/openfoamparser',
    },
)
