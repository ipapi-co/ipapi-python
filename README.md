

# ipapi Python Library ~ [ipapi.co](https://ipapi.co/) by Kloudend, Inc.
## IP Address Location | IP Lookup | IP Geolocation API

The ipapi Python library provides convenient access to the IP address location service from applications written in the Python language. It makes it easy to harness the potential of the IP geolocation API. 

Details on [free IP lookup](https://ipapi.co/free/) and [ipapi pricing plans](https://ipapi.co/pricing/)

## Documentation
See the [ipapi API docs](https://ipapi.co/api/?python#location-of-clients-ip)

## Installation

```
pip install --upgrade ipapi
```
or
Install from source with:
```
python setup.py install
```
### Requirements

Python 2.7+ or Python 3.4+ (PyPy supported)

## QuickStart
```python
>>> import ipapi

>>> ipapi.location()
{
  "ip": "8.8.8.8",
  "city": "Mountain View",
  "country": "US",
  "timezone": "America/Los_Angeles",
  ...
}
```

## Usage : As an IP Location library

```python
import ipapi

ipapi.location(ip, key, output)
```
### [Options](#options)
|Argument|Description  |
|--|--|
|`ip`| IP Address (IPv4 or IPv6) that you wish to locate.<br>If omitted, it defaults to the your machine's IP  |
|`key`| API key (for paid plans).<br>Omit it or set key=`None` for usage under [free IP Location]([https://ipapi.co/free/](https://ipapi.co/free/)) tier.  |
|`output`| The desired output from the API. <br>For complete IP location object, valid values are `json`, `csv`, `xml`, `yaml`.<br>To retrieve a specific field (e.g. city, country etc. as text), valid values are [1].<br>If omitted or `None`, gets the entire location data as `json` |

[1] Fields supported by the API : `ip`, `city`, `region`, `region_code`, `country`, `country_code`, `country_code_iso3`, `country_capital`, `country_tld`, `country_name`, `continent_code`, `in_eu`, `postal`, `latitude`, `longitude`, `timezone`, `utc_offset`, `country_calling_code`, `currency`, `currency_name`, `languages`, `country_area`, `country_population`, `latlong`, `asn`, `org`

#### Examples

1. Find the **location of your IP address**
```python
>>> ipapi.location()
```
The output would be a `JSON` object like this (assuming your IP is '50.1.2.3') : 
```json
{
    "ip": "50.1.2.3",
    "city": "Sacramento",
    "region": "California",
    "region_code": "CA",
    "country": "US",
    "country_code": "US",
    "country_code_iso3": "USA",
    "country_capital": "Washington",
    "country_tld": ".us",
    "country_name": "United States",
    "continent_code": "NA",
    "in_eu": false,
    "postal": "95817",
    "latitude": 38.548,
    "longitude": -121.4597,
    "timezone": "America/Los_Angeles",
    "utc_offset": "-0700",
    "country_calling_code": "+1",
    "currency": "USD",
    "currency_name": "Dollar",
    "languages": "en-US,es-US,haw,fr",
    "country_area": 9629091.0,
    "country_population": 310232863.0,
    "asn": "AS7065",
    "org": "SONOMA"
}
```

2. Find the **location of an IP address**
```python
>>> ipapi.location(ip='8.8.8.8')
```
```json
{
    "ip": "8.8.8.8",
    "city": "Mountain View",
    "region": "California",
    ...
}
```
You can also use an IPv6 address e.g.
```python
>>> ipapi.location(ip='2001:4860:1::1')
```

3. Find the **location of an IP address** in `xml`format (other formats :`json`, `csv`,`yaml`)
```python
>>> ipapi.location(ip='8.8.8.8', output='xml')
```
```xml
'<?xml version="1.0" encoding="utf-8"?>
  <root>
    <ip>8.8.8.8</ip>
    <city>Mountain View</city>
    ...
  </root>'
```

4. Find **your external IP address**
```python
>>> ipapi.location(output='ip')
```
```
'50.1.2.3'
```

5. Find the **city from an IP address**
```python
>>> ipapi.location(ip='8.8.8.8', output='city')
```
```
'Mountain View'
```
6. Find the **country code from an IP address**
```python
>>> ipapi.location(ip='8.8.8.8', output='country_code')
```
```
'US'
```
7. Find the **region of an IP address**
```python
>>> ipapi.location(ip='8.8.8.8', output='region_code')
```
```
'CA'
```
8. Find if an **IP address is located in the European Union**
```python
>>> ipapi.location(ip='8.8.8.8', output='in_eu')
```
```
'False'
```
9. Find the **latitude and longitude of an IP address**
```python
>>> ipapi.location(ip='1.2.3.4', output='latlong')
```
```
'-27.473101,153.014046'
```
10. Find the **postal code of an IP address**
```python
>>> ipapi.location(ip='1.2.3.4', output='postal')
```
```
'4101'
```
11. Find the **timezone of an IP address**
```python
>>> ipapi.location(ip='1.2.3.4', output='timezone')
```
```
'Australia/Brisbane'
```
12. Find the **currency of an IP address**
```python
>>> ipapi.location(ip='1.2.3.4', output='currency')
```
```
'AUD'
```
13. Find the **ASN of an IP address**
```python
>>> ipapi.location(ip='1.1.1.1', output='asn')
```
```
'AS13335'
```
14. Find the **Organization of an IP address**
```python
>>> ipapi.location(ip='8.8.8.8', output='org')
```
```
'GOOGLE'
```



## Usage : As an IP Location command line utility

```bash
$ python ipapi -i <IP Address> -k <API KEY> -o <Output Format>
$ python ipapi --ip <IP Address> --key <API KEY> --output <Output Format>
```
where the [options](#options) ip, key, output are defined above.

#### Examples

1. Get your IP Geolocation
```bash
$ python ipapi

```
The output would be a `JSON` object like this (assuming your IP is `50.1.2.3`) : 
```json
{
    "ip": "50.1.2.3",
    "city": "Sacramento",
    "region": "California",
    "region_code": "CA",
    "country": "US",
    "country_code": "US",
    "country_code_iso3": "USA",
    "country_capital": "Washington",
    "country_tld": ".us",
    "country_name": "United States",
    "continent_code": "NA",
    "in_eu": false,
    "postal": "95817",
    "latitude": 38.548,
    "longitude": -121.4597,
    "timezone": "America/Los_Angeles",
    "utc_offset": "-0700",
    "country_calling_code": "+1",
    "currency": "USD",
    "currency_name": "Dollar",
    "languages": "en-US,es-US,haw,fr",
    "country_area": 9629091.0,
    "country_population": 310232863.0,
    "asn": "AS7065",
    "org": "SONOMA"
}
```
2. Get the geolocation of an IP address
```bash
$ python ipapi -i '8.8.8.8'
```
```json
{
    "ip": "8.8.8.8",
    "city": "Mountain View",
    "region": "California",
    ...
}
```

3. Get the location of an IP in `xml` format (other formats : `json`, `csv`, `yaml`)
```bash
$ python ipapi -i '8.8.8.8' -o xml
```

```xml
'<?xml version="1.0" encoding="utf-8"?>
  <root>
    <ip>8.8.8.8</ip>
    <city>Mountain View</city>
    ...
  </root>'
```

4. Get your external IP address
```bash
$ python ipapi -o ip
```
```
'50.1.2.3'
```

5. Get the city of an IP address
```bash
$ python ipapi -i '8.8.8.8' -o city
```
```
'Mountain View'
```





