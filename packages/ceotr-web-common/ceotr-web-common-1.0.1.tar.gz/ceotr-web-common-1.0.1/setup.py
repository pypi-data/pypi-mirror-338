from setuptools import setup, find_packages

setup(name='ceotr-web-common',
      version='1.0.1',
      description="Common web assets",
      author="CEOTR",
      author_email="support@ceotr.ca",
      url="https://gitlab.oceantrack.org/ofi/web-common.git",
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=True
      )
