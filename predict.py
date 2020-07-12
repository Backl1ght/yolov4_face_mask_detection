from PIL import Image

from yolo import YOLO

yolo = YOLO()

while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image = yolo.detect_image(image)
        r_image.show()
        im = img.split('.')
        r_image.save(im[0] + '_res.jpg')
yolo.close_session()
