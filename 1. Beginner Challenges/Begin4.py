import unicornhathd as uch
uch.brightness(0.25)

(width,height) = uch.get_shape()

for x in range(width):
    uch.set_pixel(x,11,255,255,0)
uch.show()