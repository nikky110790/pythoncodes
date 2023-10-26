
# from urllib.parse import urlparse
# import requests

# from bs4 import BeautifulSoup

# url = 'https://www.google.co.in/'

# response = requests.get(url)

# soup = BeautifulSoup(response.text, "html.parser")

# links = soup.find_all("a")

# for link in links:
#     print(link)





import requests
from bs4 import BeautifulSoup

# search for SQL training
#target_url ="https://www.pylonofthemonth.org/"
target_url ="https://www.google.com/"

# get the HTML page for this
html_page = requests.get(target_url).text

# get the HTML soup for this using default parser
soup = BeautifulSoup(html_page,"html.parser")

# get all the hyperlinks
links = soup.find_all("a")

# external links
external_links = []

# list them out
for link in links:
    
    # get this link's URL
    url = str(link.get("href"))

    # if external link, add it to list
    if not url.startswith("/"):
        if url.startswith("http"):
            external_links.append(url)  

# get list of unique links
unique_links = set(external_links)
final_list = list(unique_links)

if final_list == None:
    print("No links found")
else:
    # list final links out
    for final_link in final_list:
        print(final_link)

