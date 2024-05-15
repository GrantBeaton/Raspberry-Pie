import unicornhathd as uch
import time

red_g = (255,0,0)
black_g = (0,0,0)


uch.brightness(0.2)
(width_g,height_g) = uch.get_shape()
height_g = height_g - 1
width_g = width_g - 1
ymax_g = height_g 
x_g = 0
x1_g = 1
x2_g = 2
x3_g = 3
x4_g = 4
x5_g = 5
x6_g = 6
x7_g = 7
x8_g = 8
x9_g = 9
x10_g = 10
x11_g = 11
x12_g = 12
x13_g = 13
x14_g = 14
x15_g = 15


while True:
    for y_g in range(0,ymax_g,1):
        uch.set_pixel(x_g, y_g,*red_g)
        uch.set_pixel(x1_g, y_g,*red_g)
        uch.set_pixel(x2_g, y_g,*red_g)
        uch.set_pixel(x3_g, y_g,*red_g)
        uch.set_pixel(x4_g, y_g,*red_g)
        uch.set_pixel(x5_g, y_g,*red_g)
        uch.set_pixel(x6_g, y_g,*red_g)
        uch.set_pixel(x7_g, y_g,*red_g)
        uch.set_pixel(x8_g, y_g,*red_g)
        uch.set_pixel(x9_g, y_g,*red_g)
        uch.set_pixel(x10_g, y_g,*red_g)
        uch.set_pixel(x11_g, y_g,*red_g)
        uch.set_pixel(x12_g, y_g,*red_g)
        uch.set_pixel(x13_g, y_g,*red_g)
        uch.set_pixel(x14_g, y_g,*red_g)
        uch.set_pixel(x15_g, y_g,*red_g)
        time.sleep(0.1)
        
        uch.set_pixel(x_g,y_g,*black_g)
        uch.set_pixel(x1_g, y_g,*black_g)
        uch.set_pixel(x2_g, y_g,*black_g)
        uch.set_pixel(x3_g, y_g,*black_g)
        uch.set_pixel(x4_g, y_g,*black_g)
        uch.set_pixel(x5_g, y_g,*black_g)
        uch.set_pixel(x6_g, y_g,*black_g)
        uch.set_pixel(x7_g, y_g,*black_g)
        uch.set_pixel(x8_g, y_g,*black_g)
        uch.set_pixel(x9_g, y_g,*black_g)
        uch.set_pixel(x10_g, y_g,*black_g)
        uch.set_pixel(x11_g, y_g,*black_g)
        uch.set_pixel(x12_g, y_g,*black_g)
        uch.set_pixel(x13_g, y_g,*black_g)
        uch.set_pixel(x14_g, y_g,*black_g)
        uch.set_pixel(x15_g, y_g,*black_g)
        time.sleep(0.1)

    for y_g in range(ymax_g,0,-1):
        uch.set_pixel(x_g,y_g,*red_g)
        uch.set_pixel(x1_g, y_g,*red_g)
        uch.set_pixel(x2_g, y_g,*red_g)
        uch.set_pixel(x3_g, y_g,*red_g)
        uch.set_pixel(x4_g, y_g,*red_g)
        uch.set_pixel(x5_g, y_g,*red_g)
        uch.set_pixel(x6_g, y_g,*red_g)
        uch.set_pixel(x7_g, y_g,*red_g)
        uch.set_pixel(x8_g, y_g,*red_g)
        uch.set_pixel(x9_g, y_g,*red_g)
        uch.set_pixel(x10_g, y_g,*red_g)
        uch.set_pixel(x11_g, y_g,*red_g)
        uch.set_pixel(x12_g, y_g,*red_g)
        uch.set_pixel(x13_g, y_g,*red_g)
        uch.set_pixel(x14_g, y_g,*red_g)
        uch.set_pixel(x15_g, y_g,*red_g)
        uch.show()
        time.sleep(0.1)
        
        uch.set_pixel(x_g,y_g,*black_g)
        uch.set_pixel(x1_g, y_g,*black_g)
        uch.set_pixel(x2_g, y_g,*black_g)
        uch.set_pixel(x3_g, y_g,*black_g)
        uch.set_pixel(x4_g, y_g,*black_g)
        uch.set_pixel(x5_g, y_g,*black_g)
        uch.set_pixel(x6_g, y_g,*black_g)
        uch.set_pixel(x7_g, y_g,*black_g)
        uch.set_pixel(x8_g, y_g,*black_g)
        uch.set_pixel(x9_g, y_g,*black_g)
        uch.set_pixel(x10_g, y_g,*black_g)
        uch.set_pixel(x11_g, y_g,*black_g)
        uch.set_pixel(x12_g, y_g,*black_g)
        uch.set_pixel(x13_g, y_g,*black_g)
        uch.set_pixel(x14_g, y_g,*black_g)
        uch.set_pixel(x15_g, y_g,*black_g)
        time.sleep(0.1)