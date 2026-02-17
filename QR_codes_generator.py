'''we are going to use Python library like qrcode and convert url to qr'''

import qrcode
url=input('enter your url: ')
filename=input('File name you want to save it as: ')
if not(filename.endswith('.png')):
    filename=filename+'.png'

img=qrcode.make(url)
img.save(filename)