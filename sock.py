# import socks
# import socket
# from urllib import request

# socks.set_default_proxy(socks.SOCKS5, "localhost", 9050)
# socket.socket = socks.socksocket
# r = request.urlopen('http://icanhazip.com')
# print(r.read()) # check ips

import socket
import socks
 # you need to install pysocks (see above)

# Configuration
SOCKS5_PROXY_HOST = '47.52.133.18'
SOCKS5_PROXY_PORT = 1080

# Remove this if you don't plan to "deactivate" the proxy later
default_socket = socket.socket

# Set up a proxy
socks.set_default_proxy(socks.SOCKS5, SOCKS5_PROXY_HOST, SOCKS5_PROXY_PORT)
socket.socket = socks.socksocket

# - If you use urllib2:
# import urllib2
# print urllib2.urlopen('http://icanhazip.com/', timeout=24).read() # outputs proxy IP

# - If you use requests (pip install requests):
import requests
print (requests.get('http://icanhazip.com/', timeout=24).text) # outputs proxy IP

# # Use this only if you plan to make requests without any proxies later
# socket.socket = default_socket

# # Make a request normally without a proxy; this will output your own public IP
# # print urllib2.urlopen('http://icanhazip.com/', timeout=24).read()