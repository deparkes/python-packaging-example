from setuptools import setup
from setuptools import find_packages

setup(name='my_package',
      version='0.1.0',
      description='Simple python packaging example',
      license='GPL', packages=find_packages('src'),
      package_dir={'': 'src'}  # Specifies that the 'root' directory for the build is 'src'
)