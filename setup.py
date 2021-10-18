import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='modules',
    version='0.0.1',    
    description='Testing the package',
    url='C:\Users\Raidon\Documents\Python code projects\Package 1 for pip\modules',
    author='GhostUponAvon',
    author_email='n/a',
    license='MIT',
    packages=['module1'],
    install_requires=['os',                     
                      ],
    long_description=long_description,
    long_description_content_type="text/markdown",
)
