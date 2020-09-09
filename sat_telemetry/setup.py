from setuptools import setup, find_packages

setup(
    name='sat_telemetry',
    version='0.5',
    packages=['polls', 'polls.scripts', 'polls.management', 'polls.migrations', 'sat_telemetry'],
    url='',
    license='',
    author='marco',
    author_email='marconardes@gmail.com',
    description='',
    install_requires=['django','django_extensions','django-cors-headers'],
    scripts=['manage.py']
)
