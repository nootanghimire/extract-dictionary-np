#!/usr/bin/python

import sys
import os
import requests
import lxml.html as lh
from lxml.cssselect import CSSSelector
from decimal import Decimal

def getData(text):
    url = 'http://dictionary.com.np/index.php'
    form_data = {
        'search2nep': text,
        'submit1': 'Search',
    }
    print("Requested: " + url+ " with search2nep: " +text,end="")
    response = requests.post(url, data=form_data)
    tree = lh.document_fromstring(response.content)
    #return lh.tostring(tree.cssselect("font.nepfont")[0])
    hold = tree.cssselect("font.nepfont")
    if(len(hold)<1):
        print (" Not Found :( ")
        return ""
    print(" Found :) ")
    return (tree.cssselect("font.nepfont")[0]).text_content()
    #return lh.tostring(tree)
    #return tree.text_content()
    #return tree[0].tail.strip()
    #return tree;
    #tree.cssselect(".nepfont")
    #return tree.cssselect
    #return tree.html.tostring()
    #return tree.xpath("//b[text()=$caption]", caption=caption)[0].tail.strip()

def readFile(filename, filename_new, resume=False):
    filenew = open(filename_new, "a+")
    pos = 0
    if(resume == True):
        #Calculate LineNumber
        print("Calculating Resume Position...")
        pos =  os.popen("wc -l "+filename_new).read()
        pos = pos.strip()
        pos = pos.split(" ")
        pos = pos[0]
        pos = int(pos)
        print("Calculated Resume Position! Now Resuming from line", pos, "...")
    with open(filename) as f:
        if resume:
            for i in range(pos):
                next(f)
        for line in f:
            text = line.strip()
            utf = os.popen("echo \"" + getData(text).strip() + "\" | ./2utf8/main.sh").read()
            utf = utf.strip()
            print(text + "\t" +  utf , file=filenew)

if __name__ == '__main__':
    #print(len(sys.argv))
    if(len(sys.argv) < 3):
        print("  Usage: ./main.py eng_wordlist_file  new_file_to_write_nep_wordlist [--resume]")
        print("  \tNepali List will be appended to the file specified. Or created if file do not exist.")
        print("  \tOutput  Format: <eng_name>     <nep_word1>, <nep_word2>, ... , <nep_word_n>")
        print("  \tUse --resume if you want to resume the crawl")
    else:
        if(len(sys.argv) == 4):
            if(sys.argv[3] != "--resume"):
                print("  [!!] Expected \"--resume\" but got " + sys.argv[3])
                print("  Usage: ./main.py eng_wordlist_file  new_file_to_write_nep_wordlist [--resume]")
                print("  \tNepali List will be appended to the file specified. Or created if file do not exist.")
                print("  \tOutput  Format: <eng_name>     <nep_word1>, <nep_word2>, ... , <nep_word_n>")
                print("  \tUse --resume if you want to resume the crawl")
            else:
                readFile(sys.argv[1], sys.argv[2], True)
        else:
            readFile(sys.argv[1], sys.argv[2])
