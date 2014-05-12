#!/usr/bin/env python

import peewee
from peewee import *

db = MySQLDatabase('wordpress', user='root',passwd='root')

def getPostId(title):
    post = Wp_posts.get(Wp_posts.post_title == title)
    return post.id

def getPostName(title):
    l = title.split(" ")
    ret = ""
    for w in l:
        if ret != "":
            ret = ret + "-"
        ret = ret + w
    return ret

def insertPost(pt, pp=0):
    pm = ""
    pty =""
    ps = ""
    pn = getPostName(pt)
    if pp != 0:
        pm = "image/jpeg"
        pty = "attachment"
        ps = "inherit"
    else:
        pty = "product"
        ps = "publish"
    post = Wp_posts(post_title=pt, post_name=pn, post_type=pty, post_parent=pp, post_mime_type = pm, post_content="", post_excerpt="", to_ping="", pinged="", post_content_filtered="", post_status=ps)
    post.save()

def insertMeta(pid, key, val):
    post = Wp_postmeta(post_id=pid, meta_key=key, meta_value=val)
    post.save()

class Wp_posts(peewee.Model):
    post_title = peewee.TextField()
    post_name = peewee.TextField()
    post_type = peewee.TextField()
    post_parent = peewee.IntegerField()
    post_mime_type = peewee.TextField()
    post_content = peewee.TextField()
    post_excerpt= peewee.TextField()
    to_ping = peewee.TextField()
    pinged = peewee.TextField()
    post_content_filtered = peewee.TextField()
    post_status = peewee.TextField()

    class Meta:
        database = db

class Wp_postmeta(peewee.Model):
    post_id = peewee.IntegerField()
    meta_key = peewee.TextField()
    meta_value = peewee.TextField()

    class Meta:
        database = db

def insertDatabase(title, img, price):
    insertPost(title, 0)
    ppid = getPostId(title)
    insertMeta(ppid, "_price", price)
    insertMeta(ppid, "_visibility", "visible")

    insertPost(title+"image", ppid)
    pmid = getPostId(title+"image")
    insertMeta(pmid, "_wp_attached_file", img)

insertDatabase("my fav jaljeera", "bhawani/jaljeera.jpeg", 30)










