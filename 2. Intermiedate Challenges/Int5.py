import unicornhathd as uch
import time
uch.brightness(0.25)

(width,height) = uch.get_shape()

for y in range(0,7,2):
  for x in range(0,16):
    uch.set_pixel(x,y,0,255,0)

uch.show()