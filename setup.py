from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='datafit',
    version='0.2023.7',
    description='This is a Python package that automates your data preprocessing',
    long_description=long_description,
    long_description_content_type='text/x-rst',  # Specify the type of content as Markdown
    author='Syed Syab & Hamza Rustam',
    author_email='syab.se@hotmail.com',
    url='https://github.com/SyabAhmad/datafit',
    license='MIT',

    packages=find_packages(),
    install_requires=[
        'numpy>=1.0',
        'pandas>=1.0',
        'scikit-learn',

    ],

    # Entry points for command-line scripts if applicable
    entry_points={
        'console_scripts': [
            'my_script = datafit.datafit:information',
        ],
    },

    # Other optional metadata
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        # Add more classifiers as appropriate
    ],
)