from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='password_leak_verifier',
    version='0.1.1',
    packages=find_packages(),
    install_requires=[
        'requests>=2.32.0'  # Add requests, remove standard library modules
    ],
    author='Danilo De Castro',
    author_email='danilocastro81@gmail.com',
    description='Library for password checking. It checks the number of time the password has been leaked based on pwnedpasswords records.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    url='https://github.com/rapzodo/password_checker',
    classifiers=['Programming Language :: Python :: 3',
                 'License :: OSI Approved :: MIT License',
                 'Operating System :: OS Independent'],
    python_requires='>=3.6',
)

#python setup.py sdist bdist_wheel -- command to generate the lib
#twine upload dist/*  -- command to upload the lib
