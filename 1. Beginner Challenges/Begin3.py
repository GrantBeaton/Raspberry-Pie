import unicornhathd as uch
uch.brightness(0.25)

(width,height) = uch.get_shape()

uch.set_pixel(0,7,255,255,0)
uch.set_pixel(1,6,255,255,0)
uch.set_pixel(2,5,255,255,0)
uch.set_pixel(3,4,255,255,0)
uch.set_pixel(4,3,255,255,0)
uch.set_pixel(5,2,255,255,0)
uch.set_pixel(6,1,255,255,0)
uch.set_pixel(7,0,255,255,0)

uch.show()