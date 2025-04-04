from setuptools import setup, find_packages
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setup(
   name='AV_investimentos',
   version='0.5',
   packages=find_packages(),
   install_requires=[],
   author='Antonio Victor M Fonseca',
   author_email='anvimefo0123@gmail.com',
   description='Uma biblioteca para cálculos de investimentos.',
   url='https://github.com/Antonio-AV/AV_investimentos',
   classifiers=[
       'Programming Language :: Python :: 3',
       'License :: OSI Approved :: MIT License',
       'Operating System :: OS Independent',
   ],
   python_requires='>=3.7',
   long_description=long_description,
   long_description_content_type='text/markdown'
)