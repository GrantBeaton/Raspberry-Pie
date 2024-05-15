import unicornhathd as uch
x = 0
y = 0
while x < 16 and y < 16:
    
    uch.set_pixel(x, y, 255, 100, 255)
    uch.show()
    x = x + 1
    y = y + 1


z = 0
u = 16
while z < 16 and u>0:
    
    uch.set_pixel(z, u, 255, 100, 255)
    uch.show()
    z = z + 1
    u = u - 1