
# ipapi Python bindings (https://ipapi.co)
# API docs at https://ipapi.co/api

import sys
import argparse
from requests import get

headers = {'user-agent': 'ipapi/ipapi-python/0.4'}
API_KEY = ''


def location(ip=None, key=None):
    ''' Get complete geolocation data (as JSON) for given IP address '''
    if ip:
        url = 'https://ipapi.co/{}/json/'.format(ip)
    else:
        url = 'https://ipapi.co/json/'
    if key or API_KEY:
        url = '{}?key={}'.format(url, (key or API_KEY))

    response = get(url, headers=headers)
    return response.json()


def field(field, ip=None, key=None):
    ''' Get specific geolocation field (as text) for given IP address '''
    if ip:
        url = 'https://ipapi.co/{}/{}/'.format(ip, field)
    else:
        url = 'https://ipapi.co/{}/'.format(field)
    if key or API_KEY:
        url = '{}?key={}'.format(url, (key or API_KEY))

    response = get(url, headers=headers)
    return response.text


def main(argv=None):
    field_list = ['ip', 'city', 'region', 'country', 'postal', 'latitude', 'longitude', 'timezone', 'latlong']
    
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser(description='IP address location API : https://ipapi.co')
    parser.add_argument('-i', '--ip', dest='ip', help='IP address') 
    parser.add_argument('-f', '--field', dest='field', help='specific field e.g. {}'.format(', '.join(field_list)), default=None) 
    parser.add_argument('-k', '--key', dest='key', help='API key', default=None) 
    args = parser.parse_args(argv)

    if args.field and (args.field not in field_list):
        print 'Invalid field : {}'.format(args.field)
        return

    if args.field:
        print field(args.field, args.ip, args.key)
    else:
        print location(args.ip, args.key)


if __name__ == "__main__":       
    sys.exit(main())   
