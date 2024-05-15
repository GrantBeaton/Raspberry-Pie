import unicornhathd as uch
uch.brightness(0.25)

(width,height) = uch.get_shape()

uch.set_pixel(0,0,255,255,0)
uch.set_pixel(1,1,255,255,0)
uch.set_pixel(2,2,255,255,0)
uch.set_pixel(3,3,255,255,0)
uch.set_pixel(4,4,255,255,0)
uch.set_pixel(5,5,255,255,0)
uch.set_pixel(6,6,255,255,0)
uch.set_pixel(7,7,255,255,0)

uch.show()