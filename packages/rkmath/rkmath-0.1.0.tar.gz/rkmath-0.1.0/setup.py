from setuptools import find_packages, setup

setup(
    name='rkmath',
    packages=find_packages(include=['rmath']),
    version='0.1.0',
    description='Math library for easy math operations',
    author='Swifterhtmler',
    install_requires=["numpy==2.20.0"],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)