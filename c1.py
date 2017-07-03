a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
result = ""
for c in a:
	if c >= "a" and c <= "z":
		result += chr(ord('a')+(ord(c)+2-ord('a'))%26)
	else:
		result += c

print result
