import setuptools

setuptools.setup(
    name='django-remark42',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
