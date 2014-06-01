
from distutils.core import setup

required = ['pillow', 'requests', 'vari>=0.0.2']

with open('README.txt') as f:
    readme = f.read()

setup(
    name='lores',
    version='0.0.5',
    author='Phil Adams',
    author_email='phil@philadams.net',
    url='https://github.com/philadams/lores',
    license='LICENSE.txt',
    description='Render image files in the terminal',
    long_description=readme,
    install_requires=required,
    packages=['lores'],
    scripts=['bin/lores'],
)
