from bs4 import BeautifulSoup
import re
import requests

r = requests.get('http://192.168.100.1/cgi-bin/status_cgi')

soup = BeautifulSoup(r.text)

print soup.text
