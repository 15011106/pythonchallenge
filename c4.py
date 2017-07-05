import urllib2
page = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345")
text = page.read()
i = int(filter(str.isdigit,text))

for a in range(400):
	page = urllib2.urlopen("http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%d" % i)
	text = page.read()
	i = int(filter(str.isdigit,text))
	a += 1
	print text
	print i
