from setuptools import setup, find_packages

setup(
    name='morse_python',
    version='1.0',
    description='Library for coding in Python with morse code',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Mattia Capuano AKA: Ametisto',
    author_email='mattia.capuano1508@gmail.com',
    url='https://github.com/ame-tisto/morse_python',
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
