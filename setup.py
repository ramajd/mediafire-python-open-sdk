from setuptools import setup
import uuid

with open('requirements.txt') as f:
    install_requires = f.read().strip().split('\n')

setup(
    name='mediafire',
    version='0.6.0',
    author='Roman Yepishev',
    author_email='rye@keypressure.com',
    packages=['mediafire', 'mediafire.media'],
    url='https://github.com/MediaFire/mediafire-python-open-sdk',
    license='BSD',
    description='Python MediaFire client library',
    long_description=open('README.rst').read(),
    install_requires=install_requires,
    keywords="mediafire cloud files sdk storage api upload",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'License :: OSI Approved :: BSD License'
    ]
)
