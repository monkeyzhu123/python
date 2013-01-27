import urllib2,os
import re
import time
##url_name='http://python3.baike.com/article-362189.html'
url_name=raw_input("enter the url_name:")
input_path=raw_input("enter dir beyond d:/img/")

download_path=r'd:/img/'+input_path+'/'
if os.path.exists(download_path):
    pass
else:
    os.mkdir(download_path)

response=urllib2.urlopen(url_name)
bb=response.read()
##print bb
tu=re.compile('<img.*src.*="http://.*img.*src.*\.jpg"')
count=0
for file_url  in tu.findall(bb) :
##    print file_url
    aa=file_url.split("\"")
##    print
    count+=1
    for i in aa:
        if 'http' in i:
##            print "there is %d pictures" % int(len(aa))

            print "downloading......%s......%s" % (count,i)
            request = urllib2.Request(i)
            f=open(download_path+str((time.time()))+".jpg",'wb')
            f.write(urllib2.urlopen(request).read())
            f.close()
            print "download complete!"

print"there is %d pictures" % count
