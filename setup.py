from setuptools import find_packages, setup


setup(
    version='0.1.0',
    name='django-declaration-middleware',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],
    description='Django application to force users to accept a declaration before accessing a set of urls',
    author='Incuna Ltd',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/django-declaration-middleware',
    classifiers=[
        'Development Status :: 2',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
