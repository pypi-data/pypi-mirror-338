from setuptools import setup, find_packages
import wangsu

try:
    from setuptools import setup
except ImportError as err:
    print("To install this package, please install setuptools first.")
    print("You can install it using:")
    print()
    print("pip install setuptools")
    exit()

setup(
    name='wangsu-sdk-python',
    version=wangsu.__version__,
    author='wangsu-api',
    packages=find_packages(exclude=["tests*"]),
    url='https://github.com/wangsu-api/wangsu-sdk-python',
    description='Wangsu SDK for Python',
    long_description=open('README.rst').read(),
    python_requires=">=3.6",
    platforms='any',
    install_requires=[
        "requests>=2.10.0",
        "alibabacloud_tea>=0.3.3, <1.0.0",
        "alibabacloud_tea_openapi>=0.3.6, <1.0.0",
        "alibabacloud_tea_console>=0.0.1, <1.0.0",
        "alibabacloud_tea_util>=0.3.8, <1.0.0"
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Information Technology',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)
