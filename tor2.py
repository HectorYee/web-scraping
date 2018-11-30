from torrequest import TorRequest

with TorRequest(proxy_port=9050, ctrl_port=9051, password='thread') as tr:
	response = tr.get('http://ipecho.net/plain')
	print(response.text)