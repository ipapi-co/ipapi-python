
from setuptools import setup

setup(
  name = 'ipapi',
  packages = ['ipapi'], 
  version = '0.4.2',
  description = 'Python bindings for ipapi (IP address geolocation API - https://ipapi.com)',
  author = 'ipapi',
  license="MIT License",
  author_email = 'pweb@ipapi.co',
  url = 'https://github.com/ipapi-co/ipapi-python', 
  download_url = 'https://github.com/ipapi-co/ipapi-python/archive/0.4.2.tar.gz', 
  keywords = ['geolocation', 'location', 'ipapi', 'ipapi.co', 'ip address to location', 'ipaddress', 'ipv4', 'ipv6', 'ip address', 'ip checker', 'ip lookup'], 
  classifiers = [],
  install_requires = [
  'requests[security]',
  ],
)
