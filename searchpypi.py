import requests, bs4, webbrowser, sys, logging, re

'''
This is an example project from Automate the boring stuff with Python book

This program scraps pypi.org/help for any keyword user inputs from command line and find all the links that contains that keyword

'''
# logging setup
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s: [%(levelname)s] - %(message)s')

# parameter setup
URL='https://pypi.org/help'
try:
    KEYWORD=sys.argv[1]
    logging.info(f"Now searching for {KEYWORD}...")
except IndexError:
    raise('Please input keyword to search!')

# scraps the webpage and find all <section class="faq-group faq-group--list"> -> <li> -> <a>

# cook soup
soup=bs4.BeautifulSoup(requests.get(URL).text,'lxml')

# find all elements with keyword
found_link=[]
for a in soup.select('.faq-group.faq-group--list ul li a'):
    if re.search(KEYWORD,a.get_text(),re.IGNORECASE):
        link=f"{URL}/{a['href']}"
        found_link.append(link)
        logging.info(f"{a.get_text()}: {link}")

# ask if user would like to open all found link
open_or_not=input('Do you wish to open up all links? y/n\n')

while open_or_not.lower() not in ['yes','y','no','n']:
    open_or_not=input('Do you wish to open up all links? y/n\n')

# open links
if open_or_not.lower() in ['yes','y']:
    for linkk in found_link:
        webbrowser.open_new_tab(linkk)
else:
    logging.info('Program exits without opening found pages')
