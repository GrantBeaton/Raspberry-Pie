import unicornhathd as uch
import time
uch.brightness(0.25)

(width,height) = uch.get_shape()

for x in range(width):
    uch.set_pixel_hsv(x,0,1,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,1,0.9375,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,2,0.8723,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,3,0.8075,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,4,0.7425,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,5,0.6775,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,6,0.6125,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,7,0.5475,1,1)
    
for x in range(width):
    uch.set_pixel_hsv(x,8,0.4825,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,9,0.4175,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,10,0.3525,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,11,0.2875,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,12,0.2225,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,13,0.1575,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,14,0.0925,1,1)

for x in range(width):
    uch.set_pixel_hsv(x,15,0.0,1,1)
uch.show()