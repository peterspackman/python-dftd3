from numpy.distutils.core import Extension

def configuration(parent_package='', top_path=None):

    from numpy.distutils.misc_util import Configuration

    config = Configuration(None, parent_package, top_path)

    config.add_subpackage('dftd3')

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup

    setup(name='python-dftd3',
          version='0.1.0',
          description='D3 dispersion correction calculation with python',
          author='Peter Spackman',
          author_email='peterspackman@fastmail.com',
          entry_points={
              'console_scripts': [
                  'python-dftd3 = dftd3.cli:main',
              ]
          },
          install_requires=['numpy'],
          configuration=configuration)
