#!/usr/bin/env python
import urllib2, json, re

def urlencoder(item):
    val = item.split(" ")
    ret = ""
    for it in val:
        if ret != "":
            ret = ret + "+"
        ret = ret + it
    return ret

url = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1430&bih=483&q="

def getImage(path, name):
    request = urllib2.Request(path)
    response = urllib2.urlopen(request)
    if response.info().getheader('Content-Type') == "image/jpeg":
        local_file = open(name, "w")
        local_file.write(response.read())
        local_file.close()
        return True
    return False

def findimage(name, filename):
    toturl = url + urlencoder(name)
    req = urllib2.Request(toturl)
    req.add_header('user-agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36')
    val = urllib2.urlopen(req)
    data = val.read()
    it = re.finditer('(?<=imgurl=)[\w\\\\\\.-\\:]*jpg', data)
    try:
        while True:
            val = it.next()
            if getImage(val.group(0), filename) == True:
                return True
    except StopIteration:
        print("Iteration done.")
        return False

#findimage("aachi garam masala", "testfile.jpg")
