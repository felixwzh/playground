#-*- coding: utf-8 -*-
import urllib2
import re
#------------------------------------------------------------------------------

def get_ID_list(file_path):
    fi=open(file_path,"r")
    a=[]
    for line in fi:
        line=line.strip('\n')
        a.append(line)
    fi.close()
    return a

def get_names(ID_list):
    lenth=len(ID_list)
    for i in range(0,lenth):
        userMainUrl = "http://z.seiee.com/scores/search?student_no="+ID_list[i]
        req = urllib2.Request(userMainUrl)
        resp = urllib2.urlopen(req)
        respHtml = resp.read()
        foundH1user = re.search('<p>\d*(?P<h1user>.+?)同学</p>', respHtml)
        if(foundH1user):
            h1user = foundH1user.group("h1user")
            op.write(h1user)
            op.write("\n")
        if i%20==0:
            print i


ID_list=get_ID_list(file_path='./ID.txt')
op=open("./names.txt","w")
name_list=get_names(ID_list=ID_list)
op.close()
