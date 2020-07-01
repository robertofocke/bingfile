import urllib.parse
import re
import requests

bing_url = 'http://www.bing.com/search?q=ip%3a+'

urls_array = []
count = 0
req2 = ''

f=input('file: ')
with open (f, 'r') as ff:
	for linea in ff:
		print (linea[:-1])
		while count < 10:
			url = bing_url+linea[:-1]+'&first='+str(count)
			req = requests.get(url, timeout = 3, stream = True)
			req2 += str(req.content)
			count = count+1

		hrefs = re.findall('href=[\'"]?([^\'" >]+)', req2)

		for href in hrefs:
			if 'http' in href:
				if 'microsoft' not in href:
					parse = urllib.parse.urlparse(href)
					urls_array.append(parse.scheme+'://'+parse.netloc)

print ('\n'.join(set(urls_array)))

