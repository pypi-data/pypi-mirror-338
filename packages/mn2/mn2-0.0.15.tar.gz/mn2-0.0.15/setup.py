import setuptools

with open("README.md", "r") as filename:
    readme = filename.read()

setuptools.setup(

    name='mn2', version='0.0.15',
    description='Linear Mixed Models by Feed-Forward Neural Networks.',
    url='https://github.com/orgs/CIMMYT/teams/mixed-models/',
    author='Fernando H Toledo', author_email='f.toledo@cgiar.org',

    long_description=readme,
    long_description_content_type='text/markdown',
    
    include_package_data=True,
    package_data={ 'mn2': ["data/*.csv"], },
    
    license='GPLv2',
    requires_python='>=3.11',
    install_requires=[
        'pandas>=2.2.3',
        'patsy>=1.0.1',
        'pip>=23.0.1',
        'scipy>=1.15.2',
        'setuptools>=66.1.1',
        'torch>=2.6.0'
    ],

    classifiers=[
       'Development Status :: 4 - Beta',
       'Intended Audience :: Education',
       'Topic :: Scientific/Engineering',
       'Programming Language :: Python :: 3',
       'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
       'Operating System :: OS Independent'
       ]
    )
