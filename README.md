## About script
This tool test blind xss using xsshunter via many headers [user-agent , referer , etc..] <br> 
Give urls or to work or only domain and the tool will get urls from web-archive site  <br>
The tool will request all urls with headers plus xsshunter payloads , if site store user-agent or Client-IP value or any header your entered the vulnerability will append and alert in your xsshunter profile<br>
you can test domain or multiple domains but seperator via [,] sign <br>

## Installation
pip3 install -r requments.txt <br> OR <br>
```bash
pip3 install requests
pip3 install argparse
pip3 install urllib3
pip3 install random
pip3 install time
pip3 install json
pip3 install os
pip3 install sys
pip3 install concurrent.futures
```
## Usage
short arg     | long arg      | Description
------------- | ------------- |-------------
-c            | --config      | set configs tool
-p            | --proxies     | specific one or multiple proxies 
-u            | --urls    	  | file contains urls 
-d            | --domain      | specific domain 
-ds           | --domains     | specific multiple domain , seperator via [,] sign
-t            | --threads     | Threads number to multiProccess [Default = 100]
-T            | --timeout     | Time out waiting if delay request , [Default 3]
-s            | --sleep       | sleep after every each request
-v            | --view     	  | view status code when send a request
-h            | --help        | show the help message and exit

if you want use multiple domains usage -ds, --domains twitter.com,google.com,facebook.com  ==> seperator via [,]
if you want use multiple proxies usage -p, --proxies "127.0.0.1:8080" OR "default" OR file.txt
NOTIC: if use -p, --proxies "default" will use conf/proxies-raw.txt this is file contains many proxies

## Examples
- Default usage
```python
python3 xssHeaders.py --urls urls_file.txt
```
- Put multiple domain  
```python
python3 xssHeaders.py -ds twitter.com,google.com
```
- Determine default proxies file [conf/proxies-raw.txt]
```python
python3 xssHeaders.py -d google.com -p "default"
```
- Determine threads & timeout & sleep & multiple domain & view status_code
```python
python3 xssHeaders.py -ds nokia.com,twitter.com --threads 200 --timeout 10 --sleep 1 --view
```
- set configs tool
```python
python3 xssHeaders.py --config
```
