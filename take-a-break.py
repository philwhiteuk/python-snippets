import time
import http.client
import xml.etree.ElementTree as ET
import random
import webbrowser

while (True):
    # after 2h interval has passed
    time.sleep(60*60*2)

    # get news feed
    conn = http.client.HTTPSConnection("www.goodnewsnetwork.org")
    conn.request("GET", "/category/news/inspiring/feed/")
    r1 = conn.getresponse()

    # parse rss
    root = ET.fromstring(r1.read())
    links = root.findall('./channel/item/link')

    # select news at random
    link = links[random.randint(0, len(links))]

    # launch interruption
    webbrowser.open(link.text)
