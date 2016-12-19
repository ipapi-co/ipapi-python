
# Python bindings for ipapi (IP address location API)

## Installation

```
pip install ipapi
```
or
```
python setup.py install
```

## Usage

### From your Python code

```
import ipapi

ipapi.location()
# Gets complete location for your IP address
{u'city': u'Wilton', u'ip': u'50.1.2.3', u'region': u'California', u'longitude': -121.2429, u'country': u'US', u'latitude': 38.3926, u'timezone': u'America/Los_Angeles', u'postal': u'95693'}

ipapi.field('ip')
# Gets my external IP address
u'50.1.2.3'

ipapi.field('city')
# Gets your city name
u'Wilton'

ipapi.field('country')
# Gets your country
u'US'

ipapi.location('8.8.8.8')
# Gets complete location for IP address 8.8.8.8
{u'city': u'Mountain View', u'ip': u'8.8.8.8', u'region': u'California', u'longitude': -122.0838, u'country': u'US', u'latitude': 37.386, u'timezone': u'America/Los_Angeles', u'postal': u'94035'}

ipapi.field('city', '8.8.8.8')
# Gets city name for IP address 8.8.8.8
u'Mountain View'

ipapi.field('country', '8.8.8.8')
# Gets country for IP address 8.8.8.8
u'US'
```


### From command line
```
$ python ipapi.py 
{u'city': u'Wilton', u'ip': u'50.1.2.3', u'region': u'California', u'longitude': -121.2429, u'country': u'US', u'latitude': 38.3926, u'timezone': u'America/Los_Angeles', u'postal': u'95693'}

$ python ipapi.py  -f ip
50.1.2.3

$ python ipapi.py  -f city
Wilton

$ python ipapi.py -i 8.8.8.8
{u'city': u'Mountain View', u'ip': u'8.8.8.8', u'region': u'California', u'longitude': -122.0838, u'country': u'US', u'latitude': 37.386, u'timezone': u'America/Los_Angeles', u'postal': u'94035'}

$ python ipapi.py -i 8.8.8.8 -f city
Mountain View

$ python ipapi.py -i 8.8.8.8 -f country
US
```

### With API Key

API key can be specified in the following ways : 

1. Inside `ipapi.py` by setting `API_KEY` variable
2. Via command line with the `-k` option
3. As a function argument e.g. `ipapi.field(field='country', ip='8.8.8.8', key='xyz')` or `ipapi.location(ip='8.8.8.8', key='xyz')`
