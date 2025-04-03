from setuptools import setup, find_packages

setup(
        name='risk_package_grf', # Como se descargará el paquete, i.e. el nombre.
        version='0.0.2',
        author='Mateo Rodriguez',
        author_email='mateoalejandrorr641@gmail.com',
        description='Simple test package',
        long_description=open("README.md").read(),
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=['networkx'],
        license_files=["LICENSE.txt"],
)