from ast import literal_eval as make_tuple
from PIL import Image
f = open('62f4ea780ecf4e6bbef5f40d674ec073.txt', 'r')
corl = [make_tuple(line) for line in f.readlines()]
f.close()
img0 = Image.new('RGB', (270, 270), '#ffffff')
k=0
for i in range(246):
    for j in range(246):
        img0.putpixel ([i , j], corl[k])
        k=k+1
img0.save("result.png")
