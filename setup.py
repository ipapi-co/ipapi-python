
from setuptools import setup
import sys

if sys.version_info >= (3,2):
    install_requires = ['requests']
else:
    install_requires = ['requests[security]']

setup(
  name = 'ipapi',
  packages = ['ipapi'], 
  version = '1.0.4',
  description = 'ipapi - Python library. https://ipapi.co - IP Address Location & Geolocation API by Kloudend. A REST API for JSON, CSV, XML, YAML. Supported languages are PHP, JavaScript, Python, Node, Java, Ruby, Go, C# and more. Free & paid API for a secure, fast & reliable IP lookup (city, country, latitude, longitude, region, currency, timezone, and more)',
  author = 'ipapi',
  license="MIT License",
  author_email = 'pweb@ipapi.co',
  url = 'https://github.com/ipapi-co/ipapi-python', 
  download_url = 'https://github.com/ipapi-co/ipapi-python/archive/1.0.4.tar.gz', 
  keywords = ['ip location', 'ip lookup', 'ip geolocation', 'geolocation', 'ip address', 'ip address geolocation', 'ip address lookup', 'ip address to location', 'ip address tracer', 'ip address tracker', 'ip checker', 'ip lookup', 'ip tracker', 'ip-address', 'ipapi', 'ipapi.co', 'ipv4', 'ipv6', 'location', 'lookup ip address', 'trace ip address'], 
  classifiers = [],
  install_requires = install_requires,
)
