from setuptools import setup, find_packages


def load_readme():
    with open('README.md') as readme:
        return readme.read()


def load_requirements():
    return (
        'colorama>=0.4.4, <0.5',
    )


def load_extras_require():
    requires = {
        'dev': (
            'pytest>=6.2, <6.3',
            'flake8>=3.9, <3.10'
        ),
        'yaml': (
            'pyyaml>=5.4, <5.5',
        ),
    }

    # Add all required packages to 'dev'
    requires['dev'] = tuple(
        package
        for group in requires.values()
        for package in group
    )

    return requires


setup(
    name='configTemplate',
    description='Easily define and check configuration file structures',
    version='0.0.1',
    author='RealA10N',
    author_email='downtown2u@gmail.com',
    long_description=load_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/RealA10N/configTemplate',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=load_requirements(),
    extras_require=load_extras_require(),
)
