import requests
from bs4 import BeautifulSoup
 
file = "url.txt"
readfile = open(file)
url = readfile.read()

reqs = requests.get(url)
soup = BeautifulSoup(reqs.text, 'html.parser')
 
urls = []
for link in soup.find_all('a'):
    print(link.get('href'))
