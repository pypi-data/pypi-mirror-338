from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["Dictionary/*.pyx", "Dictionary/Trie/*.pyx", "Language/*.pyx", "Syllibification/*.pyx"],
                          compiler_directives={'language_level': "3"}),
    name='nlptoolkit-dictionary-cy',
    version='1.0.33',
    packages=['Language', 'Dictionary', 'Dictionary.data', 'Dictionary.Trie', 'Syllibification'],
    package_data={'Language': ['*.pxd', '*.pyx', '*.c'],
                  'Dictionary': ['*.pxd', '*.pyx', '*.c', '*.py'],
                  'Dictionary.Trie': ['*.pxd', '*.pyx', '*.c'],
                  'Syllibification': ['*.pxd', '*.pyx', '*.c'],
                  'Dictionary.data': ['*.txt']},
    url='https://github.com/StarlangSoftware/Dictionary-Cy',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Simple Dictionary Processing',
    install_requires=['NlpToolkit-Math-Cy', 'NlpToolkit-Util-Cy'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
