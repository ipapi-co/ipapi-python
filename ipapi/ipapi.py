
# ipapi Python bindings (https://ipapi.co)
# API docs at https://ipapi.co/api

import sys
import argparse
from requests import get


API_KEY = ''

headers    = {'user-agent': 'ipapi/ipapi-python/0.5.1'}

field_list = ['ip', 'city', 'region', 'country', 'postal',
              'latitude', 'longitude', 'timezone', 'latlong']



def location(ip=None, key=None, field=None):
    ''' Get geolocation data for a given IP address
        If field is specified, get specific field as text 
        Else get complete location data as JSON 
    '''

    if field and (field not in field_list):
        return 'Invalid field'

    if field:
        if ip:
            url = 'https://ipapi.co/{}/{}/'.format(ip, field)
        else:
            url = 'https://ipapi.co/{}/'.format(field)
    else:
        if ip:
            url = 'https://ipapi.co/{}/json/'.format(ip)
        else:
            url = 'https://ipapi.co/json/'

    if key or API_KEY:
        url = '{}?key={}'.format(url, (key or API_KEY))

    response = get(url, headers=headers)

    if field:
        return response.text
    else:
        return response.json()



def main(argv=None):    
    argv = argv or sys.argv[1:]
    parser = argparse.ArgumentParser(description='IP address location API : https://ipapi.co')
    parser.add_argument('-i', '--ip', dest='ip', help='IP address', default=None) 
    parser.add_argument('-f', '--field', dest='field', help='specific field e.g. {}'.format(', '.join(field_list))) 
    parser.add_argument('-k', '--key', dest='key', help='API key', default=None) 
    args = parser.parse_args(argv)

    print location(args.ip, args.key, args.field)


if __name__ == "__main__":       
    sys.exit(main())   

