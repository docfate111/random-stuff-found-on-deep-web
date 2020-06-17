#!/usr/bin/python3
import socket
import socks
import requests

def main():
	ans = ""
	session = requests.session()
	# each time this site is visited a different letter is made yellow and this program
	# goes to the site 150 times and gets the yellow characters
	for i in range(150):
		session.proxies = {'http':  'socks5h://localhost:9050','https': 'socks5h://localhost:9050'}
		s = session.get('http://n5j7fvzjlfp5fr3sna4ra3c6plkavkrohhza5wnyfgoo3xos33pbc6yd.onion/').text
		a = s.find('<font color="yellow">')+len('<font color="yellow">')
		b = s.find('</font>')
		ans += s[a:b]
		print(i)
	print(ans)
if __name__=='__main__':
	main()
