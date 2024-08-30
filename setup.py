from setuptools import setup

setup(
    name='NumLex',
    version='2.0.0',
    package_dir={'': 'src'},  # Tell setuptools to look for packages in the src directory
    packages=['NumLex'],  # Specify the package to include
    author='Jenil Desai',
    author_email='jenildev91@gmail.com',
    description='A blend of "Numerical" and "Lexical," indicating the dual focus on numbers and language.',
    url='https://github.com/Jenil-Desai/NumLex',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)