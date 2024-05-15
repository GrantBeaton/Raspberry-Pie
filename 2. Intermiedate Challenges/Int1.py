import time

import unicornhathd as uch
red_g = (255,0,0)
green_g = (0,255,0)
blue_g = (0,0,255)
black_g = (0,0,0)


uch.brightness(0.2)
(width_g,height_g) = uch.get_shape()
ymax_g = height_g - 1
x_g = 0
def recursion(ymax_g):
    while True:
        for y_g in range(0,ymax_g,1):
            uch.set_pixel(x_g,y_g,*red_g)
            uch.show()
            uch.set_pixel(x_g,y_g,*black_g)
        for y_g in range(ymax_g,0,-1):
            uch.set_pixel(x_g,y_g,*red_g)
            uch.show()
            uch.set_pixel(x_g,y_g,*black_g)
            while True:
                for y_g in range(0,ymax_g,1):
                    uch.set_pixel(x_g,y_g,*green_g)
                    uch.show()
                    uch.set_pixel(x_g,y_g,*black_g)
                for y_g in range(ymax_g,0,-1):
                    uch.set_pixel(x_g,y_g,*green_g)
                    uch.show()
                    uch.set_pixel(x_g,y_g,*black_g)
                    while True:
                        for y_g in range(0,ymax_g,1):
                            uch.set_pixel(x_g,y_g,*blue_g)
                            uch.show()
                            uch.set_pixel(x_g,y_g,*black_g)
                        for y_g in range(ymax_g,0,-1):
                            uch.set_pixel(x_g,y_g,*blue_g)
                            uch.show()
                            uch.set_pixel(x_g,y_g,*black_g)
recursion(ymax_g)