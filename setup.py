from setuptools import setup, find_packages

setup(
    name='MHDA',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Flask>=0.12.2',
        'psycopg2>=2.7.3.2',
    ]
)




