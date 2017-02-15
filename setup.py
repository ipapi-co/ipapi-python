
from setuptools import setup
import sys

if sys.version_info >= (3,2):
    install_requires = ['requests']
else:
    install_requires = ['requests[security]']

setup(
  name = 'ipapi',
  packages = ['ipapi'], 
  version = '0.5.2',
  description = 'Python bindings for ipapi (IP address to location mapping service. Free & paid API for a secure, fast & reliable IP lookup (city, country, latitude, longitude, timezone) - https://ipapi.co)',
  author = 'ipapi',
  license="MIT License",
  author_email = 'pweb@ipapi.co',
  url = 'https://github.com/ipapi-co/ipapi-python', 
  download_url = 'https://github.com/ipapi-co/ipapi-python/archive/0.5.2.tar.gz', 
  keywords = ['geolocation', 'ip address', 'ip address geolocation', 'ip address lookup', 'ip address to location', 'ip address tracer', 'ip address tracker', 'ip checker', 'ip lookup', 'ip tracker', 'ip-address', 'ipapi', 'ipapi.co', 'ipv4', 'ipv6', 'location', 'lookup ip address', 'trace ip address'], 
  classifiers = [],
  install_requires = install_requires,
)
