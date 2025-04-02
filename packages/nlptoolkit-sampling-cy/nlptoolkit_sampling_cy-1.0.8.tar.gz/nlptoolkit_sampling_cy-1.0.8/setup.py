from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["Sampling/*.pyx", "Sampling/*.pxd"],
                          compiler_directives={'language_level': "3"}),
    name='nlptoolkit-sampling-cy',
    version='1.0.8',
    packages=['Sampling'],
    package_data={'Sampling': ['*.pxd', '*.pyx', '*.c']},
    url='https://github.com/StarlangSoftware/Sampling-Cy',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Data sampling library',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
