from setuptools import setup

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
   name             =   'hijacked_log',
   version          =   '0.1',
   description      =   "Hijacked Node's NG text generation logging module",
   license          =   "0BSD",
   long_description =   long_description,
   author           =   'Luxter77',
   author_email     =   'Luxter77@eggg.tk',
   url              =   "https://eggg.tk/",
   packages         =   ['hijacked_log'],
   install_requires =   ['colorama~=0.4.4', 'tqdm~=4.64.0'],
)
