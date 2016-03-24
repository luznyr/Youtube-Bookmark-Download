#!/usr/bin/env python

"""
Save All Bookmarked Youtube Videos
=================================
Modified by Ricky Luzny, 2016
Usage:
---------
./ python bookmarksave.py bookmarks.html

Based on:
"Extract all links from web page" by Laszlo Szathmary, 2011 (jabba.laci@gmail.com)
Website: https://pythonadventures.wordpress.com/2011/03/10/extract-all-links-from-a-web-page/
GitHub:  https://github.com/jabbalaci/Bash-Utils
Given a webpage, extract all links.

and 

Youtube-dl

"""

from __future__ import unicode_literals
from BeautifulSoup import BeautifulSoup

import sys
import urllib
import urlparse
import youtube_dl

class MyOpener(urllib.FancyURLopener):
    version = 'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15'

f = open("links.txt", "w")
d = open("downloaded.txt", "a+")

def process(url):
    myopener = MyOpener()
    #page = urllib.urlopen(url)
    page = myopener.open(url)

    text = page.read()
    page.close()

    soup = BeautifulSoup(text)

    for tag in soup.findAll('a', href=True):
    	tag['href'] = urlparse.urljoin(url, tag['href'])
        if "/watch?v" in tag['href']:
        	f.write(tag['href']+'\n')

# process(url)


def main():
    if len(sys.argv) == 1:
        print "Jabba's Link Extractor v0.1"
        print "Usage: %s URL [URL]..." % sys.argv[0]
        sys.exit(1)
    # else, if at least one parameter was passed
    for url in sys.argv[1:]:
        process(url)
# main()

#############################################################################

if __name__ == "__main__":
    main()

f.close()
f = open("links.txt", "r")

ydl_opts = {}
for line in f:
	if line not in d:
		with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    			ydl.download([line])
    	d.write(line+'\n')
    	
f.close()
d.close()


