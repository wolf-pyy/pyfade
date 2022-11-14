from setuptools import setup, find_packages


setup(
    name='pyfade',
    version='1.0',
    license='MIT',
    author="wolf-pyy",
    author_email='wolfmasterlolsivlet@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/gmyrianthous/example-publish-pypi',
    keywords=['cli', 'fade', 'colors', 'terminal', 'tui'],
)