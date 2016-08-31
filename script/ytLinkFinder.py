import urllib
from urllib.request import urlopen
import webbrowser

toSearch = input("Search: ")
toSearch = toSearch.replace(" ", "+")
link = "https://www.youtube.com/results?search_query=" + toSearch
url = urlopen(link)
s = str(url.read())

tofind = '''<div class="yt-lockup yt-lockup-tile yt-lockup-video vve-check clearfix"'''
index = s.find(tofind)

s = s[index:]

tofind = '''<div class="yt-lockup-content"><h3 class="yt-lockup-title "><a href="/watch'''
p = s
index = s.find(tofind)

s = s[index:]

tofind = 'title="'
index = s.find(tofind)

s = s[index+7:]

tofind = '"'
index = s.find(tofind)
title = s[:index]

tofind = '''<a href="'''
index = p.find(tofind)
p = p[index+len(tofind):]
tofind = '"'
index = p.find(tofind)
vidLink = p[:index]
vidLink = "https://www.youtube.com" + vidLink

print("Title: ", title)
print("Link: ", vidLink)
fo = open("options.txt", "r")
fo.read(10)
choice = fo.read(5)
if choice == "true":
    webbrowser.open(vidLink)

print("Press ENTER to continue...")
input()
