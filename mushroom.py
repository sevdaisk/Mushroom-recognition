from PIL import Image
from PIL import ImageFilter
from rembg import remove
import os
# image_filename="img1"
for i in (1, 51):
    image_filename = f'img{i}'
    img = Image.open(f"{image_filename}.jpg") #открыли изображение
    img=remove(img) #удалили фон
    img.thumbnail((100, 100), Image.NEAREST) #уменьшили разрешение
    img.save(f"images/{image_filename}_1.png") #сохранили
    img2 = img.filter(ImageFilter.SHARPEN)
    img2.save(f"images/{image_filename}_2.png")
    img2=img.transpose(Image.FLIP_LEFT_RIGHT) #развернули
    img2.save(f"images/{image_filename}_3.png") #сохранили
    img2 = img2.filter(ImageFilter.DETAIL)
    img2.save(f"images/{image_filename}_4.png")
    os.remove(f"{image_filename}.jpg") #удалили исходный
