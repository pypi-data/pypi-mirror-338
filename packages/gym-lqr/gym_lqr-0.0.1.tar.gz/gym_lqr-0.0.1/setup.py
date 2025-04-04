import os
import setuptools


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setuptools.setup(
    name='gym-lqr',
    version='0.0.1',
    author='Nick Korbit',
    description='Gym(nasium) Interface for LQR-Family Problems',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    classifiers=[
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    packages=setuptools.find_packages(exclude=[
        'artifacts',
        'examples',
        'benchmarks',
        'tests',
    ]),
    platforms='any',
    # python_requires='>=3.10',
    install_requires=[
        'numpy',
        'scipy',
        'gymnasium>=0.26.1',
        # 'pettingzoo>=1.22',
    ],
    tests_require=[
        'numpy',
        'scipy',
        'gymnasium>=0.26.1',
        # 'pettingzoo>=1.22',
        'pytest',
    ],
)
