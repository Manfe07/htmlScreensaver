import os
import random

def getImage():
    imgs = os.listdir('static/backgrounds')
    n = imgs.__len__()
    i = random.sample(imgs,1)[0]
    return(i)

def getImageList():
    imgs = os.listdir('static/backgrounds')
    n = imgs.__len__()
    i = random.sample(imgs,n)
    return(i)
    
print(getImage())