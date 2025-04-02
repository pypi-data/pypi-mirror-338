from setuptools import setup, find_packages

setup(
   name='meu_investimento_lib_arraes',
   version='0.1',
   packages=find_packages(),
   install_requires=[],
   author='Pedro Arraes',
   author_email='pedroarraes@gmail.com',
   description='Uma biblioteca para cálculos de investimentos.',
   url='https://github.com/parraes/postech',
   classifiers=[
       'Programming Language :: Python :: 3',
       'License :: OSI Approved :: MIT License',
       'Operating System :: OS Independent',
   ],
   python_requires='>=3.6',
)