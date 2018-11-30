import urllib.parse
import urllib.request

url = 'https://www.linkedin.com/in/xunweiyee/'
user_agent = 'Mozilla/5.10'
headers = { 'User-Agent' : user_agent }

req = urllib.request.Request(url, None, headers)


# req = urllib.request.Request(url)
# req.add_header('User-agent', 'Mozilla/5.10')

with urllib.request.urlopen(req) as response:
   the_page = response.read()




# import urllib

# urlopener= urllib.build_opener()
# urlopener.addheaders = [('User-agent', 'Mozilla/5.0')]
# html= urlopener.open('https://www.linkedin.com/in/xunweiyee/').read()