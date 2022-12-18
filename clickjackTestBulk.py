import sys
import re

if len(sys.argv) < 2:
    print("Error: No text file provided. Please provide a text file with a list of URLs as an argument.\n Usage: clickjackTestBulk.py urls.txt \n urls.txt should contain valid URLs in textfile.")
    sys.exit()


with open(sys.argv[1], 'r') as file:
    urls = file.readlines()
    urls = [url.strip() for url in urls]
    print(urls)

if len(urls) == 0:
    print("Error: No URLs provided in the text file.")
    sys.exit()

for url in urls:
    # Check if the URL is valid
    if not re.match(r'^https?://', url):
        print(f"Error: Invalid URL provided: {url}")
        continue
    # Create the HTML snippet
    html = f"<iframe src='{url}'></iframe>"
    # Output the HTML snippet to a separate file
    url = re.sub(r'[^\w\s]', '', url)
    with open(f"{url}.html", 'w') as file:
        file.write(html)
