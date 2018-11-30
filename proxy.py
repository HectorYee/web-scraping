# import requests
# url = 'https://httpbin.org/ip'
# proxies = {
#     # "socks": '59.115.32.43:1080',
#     "socks": '47.244.19.238:1080',
#     "socks": '212.237.21.114:1080',
#     "socks": '47.52.133.18:1080', 
#     "socks": '61.228.174.67:1080', 
#     "socks": '103.78.88.103:1080', 
#     "socks": '175.208.142.34:1080'
#     # "https": 'http://209.50.52.162:9050'
# }
# response = requests.get(url,proxies=proxies)
# print(response.json())


import requests
url = 'https://ipecho.net/plain'
proxies = {
    "https": 'https://196.32.103.155:43380',
    "https": 'https://59.127.55.215:52127',
    "https": 'https://213.74.123.108:33672',
    "https": 'https://185.188.116.223:54406',
    "https": 'https://65.126.127.202:37005',
    "https": 'https://212.42.113.240:43472'
}
response = requests.get(url,proxies=proxies)
print(response.text)

# import random
# import requests
# proxy_choices = ['140.82.62.45:3128', '196.32.103.155:43380', '213.74.123.108:33672', '59.127.55.215:52127']
# proxy = random.choice(proxy_choices)
# proxies = {'http': 'http://%s' % proxy, 'https': 'http://%s' % proxy}
# response = requests.get('http://ipecho.net/plain', proxies=proxies)
# print(response.text)