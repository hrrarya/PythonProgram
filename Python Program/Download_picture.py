from urllib.request import urlopen
import os
import sys

url = 'https://paloimages.prothom-alo.com/contents/cache/images/0x213x1/uploads/media/2018/11/16/599a3f127aa6a4c5d6e8890ee58afb2a-5bee2f4acbdcf.jpg'
r = urlopen(url)

with open("dimik.jpg","wb") as f:
    f.write(r.read())

urlpath = os.path.realpath('dimil.jpg')
print(urlpath)

print("press enter to exit: ")

    
