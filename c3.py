import urllib2
import string

page = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/equality.html")
text = page.read().decode("utf8")
string = ""
start = text.find('<!--')
end = text.find('-->')
for c in range(len(text[start:end])):
	if text[c].islower() == True:
		if text[c-3:c].isalpha() and text[c+1:c+4].isalpha():
			if text[c-3:c].isupper() and text[c+1:c+4].isupper() and text[c-4].islower() and text[c+4].islower():
				string += text[c]
		elif text[c-3:c].isalpha() == False:
			if text[c-4:c].isupper() and text[c+1:c+4].isupper() and text[c-5].islower() and text[c+4].islower():
				string += text[c]
		elif text[c+1:c+4].isalpha() == False:
			if text[c-3:c].isupper() and text[c+1:c+5].isupper() and text [c-4].islower() and text[c+5].islower():
				string += text[c]

print string
