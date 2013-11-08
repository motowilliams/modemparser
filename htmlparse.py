from bs4 import BeautifulSoup
import re
import requests
import json

r = requests.get('http://192.168.100.1/cgi-bin/status_cgi')

soup = BeautifulSoup(r.text)
downstreamtable = soup.find_all('table')[1].find_all('tr')

downstreams = []
for n in range(1, 5):
    row = downstreamtable[n].find_all('td')
    data = dict([
            ('label', row[0].string),
            ('DCID', row[1].string.split( )[0]),
            ('Freq', row[2].string.split( )[0]),
            ('Power', row[3].string.split( )[0]),
            ('SNR',   row[4].string.split( )[0]),
            ('Modulation', row[5].string.split( )[0]),
            ('Octets',     row[6].string.split( )[0]),
            ('Correcteds', row[7].string.split( )[0]),
            ('Uncorrectables', row[8].string.split( )[0])
          ])
    downstreams.append(data)

print downstreams
