#Web Challenge
# Emdee five for life
# Author -- akverma00

import requests 
import hashlib

burl="http://docker.hackthebox.eu:30268/"

req=requests.session()
r=req.get(burl)
s1=r.text
tokens=s1.split('</h3><center>')[0].split("align='center'>")
tokens=tokens[len(tokens)-1]
#print(tokens)
res=hashlib.md5(tokens.encode()).hexdigest()
r=req.post(burl,{'hash':res})

s1=r.text
tokens=s1.split('</p><center>')[0].split("align='center'>")
tokens=tokens[len(tokens)-1]
print(tokens)









