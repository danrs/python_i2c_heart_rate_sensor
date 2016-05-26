from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='python_i2c_heart_rate_sensor',
    version='0.1',
    description='Library for reading heart rate sensor',
    long_description=readme(),
    url='https://github.com/modular-CAT/python_i2c_heart_rate_sensor',
    author='Daniel Smith',
    author_email='modular-CAT@users.noreply.github.com',
    license='MIT',
    packages=['python_i2c_heart_rate_sensor'],
    install_requires=[
    ],
    zip_safe=False)
