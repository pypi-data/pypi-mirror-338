from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["ContextFreeGrammar/*.pyx", "ProbabilisticContextFreeGrammar/*.pyx",
                           "SyntacticParser/*.pyx", "ProbabilisticParser/*.pyx"],
                          compiler_directives={'language_level': "3"}),
    name='nlptoolkit-syntacticparser-cy',
    version='1.0.1',
    packages=['ContextFreeGrammar', 'ProbabilisticContextFreeGrammar',
              'ProbabilisticParser', 'SyntacticParser'],
    package_data={'ContextFreeGrammar': ['*.pxd', '*.pyx', '*.c', '*.py'],
                  'ProbabilisticContextFreeGrammar': ['*.pxd', '*.pyx', '*.c', '*.py'],
                  'ProbabilisticParser': ['*.pxd', '*.pyx', '*.c', '*.py'],
                  'SyntacticParser': ['*.pxd', '*.pyx', '*.c', '*.py']},
    url='https://github.com/StarlangSoftware/SyntacticParser-Cy',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Syntactic Parser',
    install_requires=['NlpToolkit-ParseTree-Cy', 'NlpToolkit-Corpus-Cy', 'NlpToolkit-DataStructure-Cy']
)
