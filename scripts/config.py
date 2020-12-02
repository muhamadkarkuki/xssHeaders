#!/usr/bin/env python
# By Abdulrahman-Kamel
# This file related xssHeaders tool contains on configrations tool.

import requests
from os import path
import json
from sys import exit
from scripts import func

letter = func.letter()

# class to colors
class colors:
    h = '\035[90m'	 # Header
    b = '\033[96m'   # Blue
    g = '\033[92m'	 # Green
    y = '\033[93m'	 # Yellow
    r = '\033[91m'	 # Red
    e = '\033[0m'	 # End
    B = '\033[1m' 	 # Bold
    u = '\033[4m' 	 # underLine
    n = '\033[5;91m' # notic

c = colors

# Function: print simple message
def alert(msg):
	return c.r + msg + c.e 

# Variable display banner message in terminal
msg1 = c.g+'Welcome to the xss-headers Tool. \n This tool attack the site from blind xss in headers via append xss-hunter in every header and send request \n  if the site save any header value ex.. [user-agent], will execute js code and send you update in xss-hunter site \n  now you enter the configration to save configration files tool \n\n'+c.r+' Developer By: '+c.n+ 'Abdulrahman Kamel\n\n'+c.e

msg2 = c.n+c.B+c.g+ '\t\t *~ Happy Hunting ~* \n' +c.e

# Default variables config
d_xsshunter = '-'
d_threads 	= 200
d_timeout 	= 30
d_headers = [
	'User-Agent',
	'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/12.0', 
	'Referer', 
	'https://www.google.com/', 
	'Client-IP',
	'127.0.0.1',
	'True-Client-IP',
	'127.0.0.1',
	'Cluster-Client-IP',
	'127.0.0.1',
	'X-Forwarded-For',
	'127.0.0.1',
	'Cache-Control',
	'max-age=3600',
	'From',
	'user@google.com',
	'Date',
	'Tue, 15 Nov 2020 08:12:31 GMT',
	'X-Att-Deviceid',
	'GT-P7320/P7320XXLPG',
	'Proxy-Connection',
	'keep-alive',
	'X-Do-Not-Track',
	'1',
	'X-Request-ID',
	'f058ebd6-02f7-4d3f-942e-904344e8cde5',
	'X-UIDH',
	'31337DEADBEEFCAFE',
	'X-Wap-Profile',
	'http://wap.samsungmobile.com/uaprof/SGH-I777.xml',
]

# default config in one list
default_config = ["Write XSS-Hunter next line..",
[d_xsshunter],
"Write headers start from next line..",
d_headers,
"write threads number next line..",
[d_threads],
"write timeout number next line..",
[d_timeout]
]

# open-read [config.json] file
with open('conf/config.json', 'r') as openfile: 
    json_file = json.load(openfile)

# read from [config.json] file
json_xsshunter = json_file[1][0]
json_headers   = json_file[3]
json_threads   = json_file[5][0]
json_timeout   = json_file[7][0]

# to skip error: variable is not defined 
xsshunter = ''
headers   = ''
threads   = ''
timeout   = ''

# Function: update [config.json] file, set default, editor
def update(value=None):
	XSS_HUNTER = xsshunter if xsshunter else json_xsshunter
	HEADERS    = d_headers if value == 'default_headers' else json_headers and headers if headers else json_headers
	THREADS    = d_threads if value == 'default_threads' else json_threads and threads if threads else json_threads
	TIMEOUT    = d_timeout if value == 'default_timeout' else json_timeout and timeout if timeout else json_timeout

	D_json = ['Write xsshunter here ..' , [XSS_HUNTER] , 'Write headers here ..' , HEADERS, 'write threads number next line..', [int(THREADS)], 'write timeout number next line..', [int(TIMEOUT)]]

	# Artibitally update
	with open("conf/config.json", "w") as outfile: 
	    outfile.write(json.dumps(D_json, indent = 4)) 


#==================================== Display in terminal ====================================
def runing():
	# primary
	_1 = input('\n' + msg1 + '\n 1) xssHunter \n 2) Headers \n 3) Threads \n 4) Timeout \n\n 5) default config \n 6) Exit \n\n' + c.b + 'config> ' + c.e)

	# xsshunter
	if int(_1) == 1:
		_1_1 = input('\n' + msg1 + '\n 1) display the current xss-hunter \n 2) set new xss-hunter \n\n 3) Exit \n\n' + c.b + 'config:xsshunter> ' + c.e)
		
		# dsiplay the current xss-hunter 
		if int(_1_1) == 1:
			print('\n https://' + alert(json_xsshunter) + '.xsshunter.com\n')

		# set new xss-hunter 
		if int(_1_1) == 2:
			global xsshunter
			xsshunter = input('\n'+ c.b + 'config:xsshunter:set> '+ c.e)
			update()
			print('\n xss-hunter is: https://' + alert(xsshunter) + '.xsshunter.com\n')

		# exit 
		if int(_1_1) == 3:
			print('\n[!]+ Stopped \t\t '+msg2)
			exit(1)


	'''
	# proxy
	if int(_1) == 2:
		_1_2 = input('\n' + msg1 +'\n 1) display the current proxy \n 2) set new proxy \n 3) delete proxy \n\n 4) Exit \n\n' + c.b + 'config:proxy> ' + c.e)
		

		# dsiplay the current proxy 
		if int(_1_2) == 1:
			print('\n' + alert(json_proxy) + '\n')

		# set new proxy 
		if int(_1_2) == 2:
			global proxy
			proxy = input('\n' + c.b + 'config:proxy:set> ' + c.e)
			update()
			print('\n Proxy is: ' + alert(proxy) + '\n')

		# delete proxy 
		if int(_1_2) == 3:
			update('default')
			print('\n' + alert('Proxy is none') + '\n')

		# exit 
		if int(_1_1) == 4:
			print('\n[!]+ Stopped \t\t '+msg2)
			exit(1)
	'''

	# headers
	if int(_1) == 2:
		_1_2 = input('\n' + msg1 +'\n 1) display the current headers \n 2) delete all and set default \n 3) delete all and set new \n 4) plus new headers \n\n 5) Exit \n\n' + c.b + 'config:headers> ' + c.e)
		


		# dsiplay the current headers 
		if int(_1_2) == 1:
			print('\n')

			for i in json_headers:
				print(i + ' - ',end='')
			print('\n')

		# delete all and set default 
		if int(_1_2) == 2:

			print('\n' + alert('Deleted and set default') + '\n')
			update('default_headers')

		# delete all and set new 
		if int(_1_2) == 3:

			print('\n\n' + alert('How count headers you need ?') + '\n')
			global headers
			count_headers = input('\n' + c.b +'config:headers:set>'+ c.e+' Enter count: ')

			headers = []
			
			for i in range(int(count_headers)):
				header_name  = input('\n' + c.b +'config:headers:set>'+ c.e+' Enter new header name: ')
				header_value = input('\n' + c.b +'config:headers:set>'+ c.e+' Enter value header => ' +header_name+ ' ')
				
				headers.append(header_name)
				headers.append(header_value)

			update()


			print('\n' + alert('The headers which saved..'))
			for i in headers:
				print(i + ' - ',end='')

			print('\n')

			update()

		# plus new headers 
		if int(_1_2) == 4:

			print('\n' + alert('How count headers you need ?'))
			count_headers = input('\n' + c.b + 'config:headers:set> ' + c.e + 'Enter count: ')
			
			headers = json_headers
			
			for i in range(int(count_headers)):
				header_name  = input('\n' + c.b +'config:headers:set>'+ c.e+' Enter new header name: ')
				header_value = input('\n' + c.b +'config:headers:set>'+ c.e+' Enter value header => ' +header_name+ ' ')
				
				headers.append(header_name)
				headers.append(header_value)


			print('\n' + alert('All headers which saved..'))
			for i in headers:
				print(i + ' - ',end='')

			print('\n')
			update()


		if int(_1_2) == 6:
			print('\n[!]+ Stopped \t\t '+msg2)
			exit(1)



	# threads
	if int(_1) == 3:
		_1_3 = input('\n' + msg1 +'\n 1) display the current threads \n 2) edit threads number \n 3) set default threads number(100) \n 4) Exit \n\n' + c.b + 'config:threads> ' + c.e)
	
		# dsiplay the current threads 
		if int(_1_3) == 1:

			print('\n' + alert(str(json_threads)) + '\n')

		# edit threads 
		if int(_1_3) == 2:

			global threads
			threads = input('\n' + c.b + 'config:threads:set> ' + c.e)
			update()
			print('\n Threads is: ' + alert(threads) + '\n')


		# set default threads
		if int(_1_3) == 3:

			print('\n' + alert('set default') + '\n')
			threads = 100
			update()

		# exit threads
		if int(_1_3) == 4:
			print('\n[!]+ Stopped \t\t '+msg2)
			exit(1)


	# timeout
	if int(_1) == 4:
		_1_4 = input('\n' + msg1 +'\n 1) display the current timeout \n 2) edit timeout number \n 3) set default timeout number(30) \n 4) Exit \n\n' + c.b + 'config:timeout> ' + c.e)
	
		# dsiplay the current timeout 
		if int(_1_4) == 1:

			print('\n' + alert(str(json_timeout)) + '\n')

		# edit timeout 
		if int(_1_4) == 2:

			global timeout
			timeout = input('\n' + c.b + 'config:timeout:set> ' + c.e)
			update()
			print('\n Timeout is: ' + alert(timeout) + '\n')


		# set default 
		if int(_1_4) == 3:

			print('\n' + alert('set default') + '\n')
			timeout = 30
			update()

		# exit
		if int(_1_4) == 4:
			print('\n[!]+ Stopped \t\t '+msg2)
			exit(1)



	# set default config
	if int(_1) == 5:
		letter.config(default_config)
		print('\n Default config  is set \t\t '+msg2)
		exit(1)

	# exit config
	if int(_1) == 6:
		print('\n[!]+ Stopped \t\t '+msg2)
		exit(1)