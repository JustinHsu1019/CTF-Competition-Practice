from PIL import Image
import os
gifFileName = 'test.gif'
#使用Image模块的open()方法打开gif动态图像时，默认是第一帧
im = Image.open(gifFileName)
pngDir = gifFileName[:-4]
#创建存放每帧图片的文件夹
os.mkdir(pngDir)
try:
  while True:
    #保存当前帧图片
    current = im.tell()
    im.save(pngDir+'/'+str(current)+'.png')
    #获取下一帧图片
    im.seek(current+1)
except EOFError:
    pass
