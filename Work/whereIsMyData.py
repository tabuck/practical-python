import urllib
import urllib.request

u = urllib.request.urlopen('https://data.usgs.gov/datacatalog/metadata/USGS.db4fb1b6-1282-4e5b-9866-87a68912c5d1.xml')
from xml.etree.ElementTree import parse
doc = parse(u)
for title in doc.findall('.//title'):
    print(title.text)

