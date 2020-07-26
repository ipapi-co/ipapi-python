
import sys
import argparse
import pprint

import ipapi 



def main(argv=None):    
    argv = argv or sys.argv[1:]
    
    parser = argparse.ArgumentParser(description='IP Address Location & Geolocation API : https://ipapi.co/ by Kloudend, Inc.')
    
    parser.add_argument('-i', '--ip', dest='ip', help='IP Address (IPv4 or IPv6) that you wish to locate.'\
                                                      ' If omitted, it defaults to the your machine\'s IP') 
    parser.add_argument('-k', '--key', dest='key', help='API key (for paid plans). Omit it for free plan') 
    parser.add_argument('-o', '--output', dest='output', help='Output format i.e. either json|csv|xml|yaml or '\
                        'Specific location field i.e. city|region|country etc. '\
                        'See https://ipapi.co/api for field details') 
    
    args = parser.parse_args(argv)

    pprint.pprint(ipapi.location(args.ip, args.key, args.output), indent=4)


if __name__ == "__main__":       
    sys.exit(main())   

