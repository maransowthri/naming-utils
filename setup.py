from setuptools import setup, find_packages


setup(
    name='naming_utils',
    version='0.1',
    license='MIT',
    author="Maran Sowthri Kalailingam",
    author_email='contact@maransowthri.dev',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/maransowthri/naming-utils.git',
)