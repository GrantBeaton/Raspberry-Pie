import unicornhathd as uch
uch.brightness(0.25)

(width,height) = uch.get_shape()

for y in range (height):
    uch.set_pixel(11,y,0,255,255)
uch.show()