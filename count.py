from bs4 import BeautifulSoup
import requests, re

headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:79.0) Gecko/20100101 Firefox/79.0'}
url = 'http://change.org/p/35472781'

soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
temp = soup.find_all('script', text = re.compile('signatureCount":{"displayed'))
sig_count = re.search(r'signatureCount":{"displayed":([0-9]*),', str(temp)).group(1)

print(sig_count)

