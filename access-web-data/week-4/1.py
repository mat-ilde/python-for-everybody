
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
suma=0
numeros=list()
fhand= urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_353802.html")
soup=BeautifulSoup(fhand, "html.parser")
soup.find_all(class_="comments")
s=soup.find_all("span")
for num in s:
    s=str(s)
    y=re.findall("[0-9]+",s)
for i in y:
    i=int(i)
    suma=suma+i
print(suma)
