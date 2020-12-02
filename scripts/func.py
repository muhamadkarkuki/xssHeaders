#!/usr/bin/env python
# By Abdulrahman-Kamel
# This file related xssHeaders tool contains on functions which used in tool.

import requests
import json
from os import path
from concurrent.futures import ThreadPoolExecutor


class letter():

	# Function to convert [list] to {dict}.
	def list_to_dict(self, _list):
	    it = iter(_list) 
	    res_dct = dict(zip(it, it)) 
	    return res_dct 

	# Function to write in config.json
	def config(self, value):
		with open("conf/config.json", "w") as outfile: 
			outfile.write(json.dumps(value, indent = 4)) 


# Mini function to write in file.
def writee(path , status , msg):
	filee = open(str(path) , str(status))
	filee.writelines(msg)
	filee.close()


# Function to get urls from web-archive site.
def waybackurls(domain):
	global w_path
	w_path = 'logs/waybackurls.txt'
	
	try:
		r = requests.get('https://web.archive.org/cdx/search/cdx?url=*.'+ domain +'&output=text&fl=original&collapse=urlkey' , timeout=30)
		writee(w_path ,'a+' , r.text)

	except Exception as er:
		error = 'Error occured when get urls ('+domain+') from [web-archive] site: \t'+str(er)
		writee('logs/error.txt' ,'a+' , error)


# Function: to filter data entered (anyway convert to list)
def filter(value):
    if value is not None:

        if path.isfile(value) == True:
            with open(value) as _file:
                value = [line.rstrip() for line in _file]

        elif type(value) == str and ',' not in value:
            value = value.split(' ')

        elif ',' in value:
            value = value.split(',')
        
        else:
            value = None
    return value


# Function: to calculator lines from file
def calc_lines_file(_file):
	global count
	count = 0
	for line in open(_file,'r'):
		count += 1
	return count
	open(_file,'r').close()


# Function: to read lines file as rstrip
def lines(_file):
	with open(str(_file), 'r') as f:
		urlsss = [line.rstrip() for line in f]
	return urlsss

# Function: to execute script with threads using map func
def mapThreads(_threads, _function, _file):
	with ThreadPoolExecutor(max_workers = _threads) as executor:
		for _ in executor.map(_function, _file):
			pass


# Function: check config/proxies-raw.txt, if not found download it
def check_proxiesFile():
	proxies_raw = path.isfile('conf/proxies-raw.txt')
	if proxies_raw == False:
		try:
			response = requests.get('https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt', allow_redirects=True)
			if str(response.status_code)[0] == '2' or '3':
				open('conf/proxies-raw.txt', 'wb').write(response.content)
		except Exception as er:
			print('\nMissing configs/proxies-raw.txt, can`t download it\nplease download from this repo: https://github.com/clarketm/proxy-list\nThen move here by the same name configs/proxies-raw.txt\n')

# Function to print alerts
def alert(arg):

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
	
	# Determined alerts
	if arg == 'alert_1':
		print(c.r+c.n+c.B+'\nAlert: '+c.e+' Please enter one from this arguments {-d, --domain} {-ds, --domains} {-u, --urls}\n') ; exit(1)

	if arg == 'alert_2':
		print(c.r+c.n+c.B+'\nAlert: '+c.e+'Please seperator between domains via [,] when use -ds, --domains\n') ; exit(1)
