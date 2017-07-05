import urllib2
import string

page = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
text = page.read().decode("utf8")
string = ""
start = text.find('%%$')
end = text.find('*-->')

for c in text[start:end]:
	if c.isalpha() == True:
		string += c

print string
