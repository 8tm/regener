import datetime

import setuptools

version = datetime.datetime.now().strftime('%y.%m.%d')
setuptools.setup(
    name='ResumeGenerator',
    version=version,
    author='Tadeusz Miszczyk',
    author_email='tadeusz.miszczyk@gmail.com',
    description=('Create resume using json and images',),
    url='https://github.com/8tm/resume_generator',
    package_dir={'': 'src'},
    packages=setuptools.find_namespace_packages(where='src'),
    include_package_data=True,
    install_requires=[
        'reportlab==3.6.5',
    ],
    extras_require={
        'test': [
            'flake8==3.8.3',
            'flake8-commas==2.0.0',
            'flake8-import-order==0.18.1',
            'flake8-quotes==3.2.0',
            'pytest==6.0.1',
            'pytest-cov==2.10.0',
            'pytest-mock==3.2.0',
            'pytest-random-order==1.0.4',
            'pytest-xdist==1.29.0',
            'pytest-parallel',
            'mypy==0.812',
        ],
        'tools': [
            'pip-search==0.0.7',
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: Unix',
    ],
    python_requires='>=3.9.0',
    entry_points={
        'console_scripts': [
            'resume_generator = rg.resume_generator:main',
        ],
    },
)
