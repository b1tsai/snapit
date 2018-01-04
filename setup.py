from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='snapit',
      version='0.101',
      description='Spliced Neoantigen Pipeline for Immunotherapy',
      long_description=readme(),
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Programming Language :: Python :: 3.4',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'License :: Free To Use But Restricted'
      ],
      keywords='alternative splicing neoantigen neoepitope immunotherapy',
      url='http://github.com/b1tsai/snapit',
      author='Brandon Liang Tsai',
      author_email='b1tsai@ucla.com',
      packages=['snapit'],
      install_requires=[
          'markdown',
      ],
      test_suite='nose.collector',
      tests_require=['nose', 'nose-cover3'],
      entry_points={
          'console_scripts': ['snapit-talk=snapit.command_line:main'],
      },
      include_package_data=True,
      zip_safe=False)