import requests
import xml.etree.ElementTree as ET

# URL of the news RSS feed
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"

def loadRSS():
    '''Utility function to load RSS feed'''
    # Create HTTP request response object
    resp = requests.get(RSS_FEED_URL)
    # Return response content
    return resp.content

def parseXML(rss):
    '''Utility function to parse XML format RSS feed'''
    # Create element tree root object
    root = ET.fromstring(rss)
    # Create empty list for news items
    newsitems = []
    # Iterate news items
    for item in root.findall('./channel/item'):
        news = {}
        # Iterate child elements of item
        for child in item:
            # Special checking for namespace object content:media
            if child.tag == '{http://search.yahoo.com/mrss/}content':
                news['media'] = child.attrib['url']
            news[child.tag] = child.text.encode('utf8')
        newsitems.append(news)
    # Return news items list
    return newsitems

def topStories():
    '''Main function to generate and return news items'''
    # Load RSS feed
    rss = loadRSS()
    # Parse XML
    newsitems = parseXML(rss)
    return newsitems

#second file


import time
import notify2
from topnews import topStories

# Path to notification window icon
ICON_PATH = "/path/to/your/icon.png"  # Update this with the full path to your icon image

# Fetch news items
newsitems = topStories()

# Initialize the D-Bus connection
notify2.init("News Notifier")

# Create Notification object
n = notify2.Notification(None, icon=ICON_PATH)

# Set urgency level
n.set_urgency(notify2.URGENCY_NORMAL)

# Set timeout for a notification
n.set_timeout(10000)

for newsitem in newsitems:
    # Update notification data for Notification object
    n.update(newsitem['title'], newsitem['description'])
    # Show notification on screen
    n.show()
    # Short delay between notifications
    time.sleep(15)
