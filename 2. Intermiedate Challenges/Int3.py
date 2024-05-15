import unicornhathd as uch
import time
uch.brightness(0.25)

red_g = (255,0,0)
blue_g = (0,0,255)


(width,height) = uch.get_shape()

for x in range(width):
    for y in range(height):
        uch.set_pixel(x,y,*blue_g)
uch.show()
time.sleep(1)

for x in range(width):
    for y in range(height):
        uch.set_pixel(x,y,*red_g)
uch.show()
time.sleep(1)