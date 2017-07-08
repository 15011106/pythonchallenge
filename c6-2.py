import zipfile
string = ""
zip = zipfile.ZipFile("/Users/minhyeok/pythonchallenge/channel.zip")
text = zip.read("90052.txt")
i = int(filter(str.isdigit,text))
print i

while 1:
	text = zip.read("%d.txt"%i)
	i = int(filter(str.isdigit,text))
	print i
	string += zip.getinfo("%d.txt"%i).comment
	print string
