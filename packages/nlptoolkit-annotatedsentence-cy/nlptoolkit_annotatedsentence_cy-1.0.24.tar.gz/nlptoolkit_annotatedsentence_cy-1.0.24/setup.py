from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")
from Cython.Build import cythonize

setup(
    ext_modules=cythonize(["AnnotatedSentence/*.pyx"],
                          compiler_directives={'language_level': "3"}),
    name='nlptoolkit-annotatedsentence-cy',
    version='1.0.24',
    packages=['AnnotatedSentence'],
    package_data={'AnnotatedSentence': ['*.pxd', '*.pyx', '*.c', '*.py']},
    url='https://github.com/StarlangSoftware/AnnotatedSentence-Cy',
    license='',
    author='olcaytaner',
    author_email='olcay.yildiz@ozyegin.edu.tr',
    description='Annotated Sentence Processing Library',
    install_requires=['NlpToolkit-WordNet-Cy', 'NlpToolkit-NamedEntityRecognition-Cy', 'NlpToolkit-PropBank-Cy',
                      'NlpToolkit-DependencyParser-Cy', 'NlpToolkit-SentiNet-Cy', 'NlpToolkit-FrameNet-Cy'],
    long_description=long_description,
    long_description_content_type='text/markdown'
)
