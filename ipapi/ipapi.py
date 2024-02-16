
''' 

IP Address Location & Geolocation API 

(c) ipapi by Kloudend, Inc. | https://ipapi.co/

API Docs : https://ipapi.co/api/

'''

from requests import get

try:
    from .exceptions import RateLimited, PageNotFound, AuthorizationFailed
except (SystemError, ImportError):  
    from exceptions import RateLimited, PageNotFound, AuthorizationFailed


field_list = ['ip', 'city', 'region', 'region_code', 'country', 'country_code', 'country_code_iso3', 
              'country_capital', 'country_tld', 'country_name', 'continent_code', 'in_eu', 'postal', 
              'latitude', 'longitude', 'timezone', 'utc_offset', 'country_calling_code', 'currency', 
              'currency_name', 'languages', 'country_area', 'country_population', 'latlong', 
              'asn', 'org']


def build_url(ip, key, output):
    url = 'https://ipapi.co/'

    if ip:
        url = '{}{}/'.format(url, ip)

    url = '{}{}/'.format(url, output)

    if key:
        url = '{}?key={}'.format(url, key)

    return url


def parse_response(resp):
    if resp.headers['Content-Type'] == 'application/json':
        return resp.json()
    else:
        return resp.text


def location(ip=None, key=None, output=None, options=None):
    ''' 
    Get Geolocation data and related information for an IP address 

    - ip      : IP Address (IPv4 or IPv6) that you wish to locate.
                If omitted, it defaults to the your machine's IP
    - key     : API key (for paid plans).
                Omit it or set key=None for usage under free IP Location tier.
    - output  : The desired output from the API.
                For complete IP location object, valid values are json, csv, xml, yaml.
                To retrieve a specific field (e.g. city, country etc. as text), valid values are [1].
                If omitted or None, gets the entire location data as json
    - options : request options supported by python requests library
    
    '''
    
    if output is None:
        output = 'json'

    if options is None:
        options = {}

    url = build_url(ip, key, output)
    
    headers = {
      'user-agent': 'ipapi.co/#ipapi-python-v1.1.2'
    }
    
    resp = get(url, headers=headers, **options)
    
    data = parse_response(resp)

    if resp.status_code == 200:
        return data
    elif resp.status_code == 403:
        raise AuthorizationFailed(data)
    elif resp.status_code == 404:
        raise PageNotFound(data)
    elif resp.status_code == 429:
        raise RateLimited(data)
    else:
        raise Exception(data)

