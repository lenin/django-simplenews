from setuptools import setup, find_packages

version = '0.1'

LONG_DESCRIPTION = """
Simple news
--------------------------
"""

setup(
    name='django-simplenews',
    version=version,
    description="django-simplenews",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='news,django',
    author='Lenin Yee',
    author_email='lenin.ayr@gmail.com',
    url='http://github.com/lenin/django-simplenews',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)
