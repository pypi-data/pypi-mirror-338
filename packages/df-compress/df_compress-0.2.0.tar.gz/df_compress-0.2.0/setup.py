from setuptools import setup

setup(
    name='df-compress',
    version='0.2.0',    
    description="A python package to compress pandas DataFrames akin to Stata's `compress` command",
    url='https://github.com/phchavesmaia/df-compress',
    author='Pedro H. Chaves Maia',
    author_email='pedro.maia@imdsbrasil.org',
    license='MIT',
    packages=['df_compress'],
    install_requires=['pandas',
                      'numpy',                     
                      ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3.13',
    ],
)
