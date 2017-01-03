
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

ipapi.location(None, None, 'ip')
# Gets my external IP address
u'50.1.2.3'

ipapi.location(None, None, 'city')
# Gets your city name
u'Wilton'

ipapi.location(None, None, 'country')
# Gets your country
u'US'

ipapi.location('8.8.8.8')
# Gets complete location for IP address 8.8.8.8
{u'city': u'Mountain View', u'ip': u'8.8.8.8', u'region': u'California', u'longitude': -122.0838, u'country': u'US', u'latitude': 37.386, u'timezone': u'America/Los_Angeles', u'postal': u'94035'}

ipapi.location('8.8.8.8', None, 'city')
# Gets city name for IP address 8.8.8.8
u'Mountain View'

ipapi.location('8.8.8.8', None, 'country')
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
3. As a function argument e.g. `ipapi.location(ip='8.8.8.8', key='secret-key')` or `ipapi.location(ip='8.8.8.8', key='secret-key', field='city')`

### Notes
- All function arguments (`ip`, `key`, `field`) are optional . To skip an argument, use `None` or an empty string `''`.
  `ipapi.location(ip='8.8.8.8', key=None, field='city')`
  `ipapi.location(ip='8.8.8.8', key='',   field='city')`    


### Error
- If you are getting `requests.exceptions.SSLError` (see below), then you need to run :

  `pip install requests[security]` 
  
```

    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "ipapi.py", line 45, in field
        response = get(url, headers=headers)
      File "/usr/lib/python2.7/dist-packages/requests/api.py", line 55, in get
        return request('get', url, **kwargs)
      File "/usr/lib/python2.7/dist-packages/requests/api.py", line 44, in request
        return session.request(method=method, url=url, **kwargs)
      File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 455, in request
        resp = self.send(prep, **send_kwargs)
      File "/usr/lib/python2.7/dist-packages/requests/sessions.py", line 558, in send
        r = adapter.send(request, **kwargs)
      File "/usr/lib/python2.7/dist-packages/requests/adapters.py", line 385, in send
        raise SSLError(e)
    requests.exceptions.SSLError: [Errno 1] _ssl.c:510: error:14077438:SSL routines:SSL23_GET_SERVER_HELLO:tlsv1 alert internal error
```

