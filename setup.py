import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='dirmaker',
    version='0.2.2',    
    description='Testing the package',
    url='https://github.com/GhostUponAvon/pip_packages',
    author='GhostUponAvon',
    author_email='n/a',
    license='MIT',
    packages=['dirmaker'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_data={'': ['*.cmd', '*.ico']}    
)
