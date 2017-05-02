import urllib.request

for i in range(101):
    urllib.request.urlretrieve("http://pokegym.net/gallery/displayimage.php?imageid={}".format(45696+i), "{}.jpg".format(i))

