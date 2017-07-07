import pickle
import urllib2

page = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
text = pickle.load(page)
string = ""
for i in text:
	for a in i:
		string += a[0]*a[1]
print string
