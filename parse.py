#!/usr/bin/env python

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
            word = ret[i+3]
            i = i+4
            #print word
            while check_next(ret[i], ret[i+1]):
                word = word + " " + ret[i]
                i = i + 1
            print word
            #print ret[i+11]
        else:
            i = i+1

