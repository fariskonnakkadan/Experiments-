import requests

def scan_xss(url, param):
  payloads = []
  with open('payloads.txt', 'r') as f:
    payloads = f.readlines()
  for payload in payloads:
    r = requests.get(url, params={param: payload})
    if payload in r.text:
        print("XSS vulnerability found "+r.url)
        return True
    return False

url = input('Enter the URL to scan: ')
param = input('Enter the parameter to inject payloads into: ')
scan_xss(url, param)
