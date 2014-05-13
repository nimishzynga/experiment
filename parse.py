#!/usr/bin/env python
from google import findimage
from database import insertDatabase

globaldict = {"MAS":"MASALA", "YD":"YARDLEY", "CRN":"CORN"}
MAINPATH = "/Library/WebServer/Documents/wordpress/wp-content/uploads/"
DIR = "bhawani/"

def check_word(w):
    if w == "GN":
        return False
    return w.isalpha()

def check_next(w, w1):
    if check_word(w):
        return True
    if w.find("GM") != -1  or w.find("KG") != -1 or w.find("L") != -1:
        return True
    if w.isdigit() and (w1.find("GM") != -1  or w1.find("KG") != -1 or w1.isalpha()):
        return True
    return False

def convert(w):
    global globaldict
    if w in globaldict:
        return globaldict[w]
    return w

with open("/Users/nimishgupta/123") as f:
    content = f.readlines()
    ret = content[36].split(" ")
    i = 0
    while i < len(ret):
    #    if check_word(ret[i]):
    #        print ret[i]
    #        i = i + 1
    #        while check_next(ret[i]):
    #            print ret[i]
    #            i = i + 1
    #    else:
    #
    # i = i + 1
        word = ""
        if ret[i] == "1GN" and ret[i+1] == "GN" and ret[i+3].isalpha():
            word = convert(ret[i+3])
            i = i+4
            #print word
            while ".0" not in ret[i]:
            #while check_next(ret[i], ret[i+1]):
                word = word + " " + convert(ret[i])
                i = i + 1
            price = ret[i+11]
            localPath = DIR+"img"+str(i)+"jpg"
            savePath = MAINPATH+localPath
            if findimage(word, savePath):
                insertDatabase(word, localPath, price)
                print "inserted into database", word
            else:
                print "image not found for", word
            #print ret[i+11]
        else:
            i = i+1

