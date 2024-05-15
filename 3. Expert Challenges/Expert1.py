import unicornhathd as uch

uch.brightness(0.5)

red=(255,0,0)
orange=(255,165,0)
yellow=(255,255,0)
green=(0,255,0)
aqua=(0,255,255)
blue = (0,0,255)
purple=(255,0,255)
light_red=(255,192,203)
black=(0,0,0)

(width,height) = uch.get_shape()

a=["roygabplroygabpl",
   "oygabplroygabplr",
   "ygabplroygabplro",
   "gabplroygabplroy",
   "abplroygabplroyg",
   "bplroygabplroyga",
   "plroygabplroygab",
   "lroygabplroygabp",
   "roygabplroygabpl",
   "oygabplroygabplr",
   "ygabplroygabplro",
   "gabplroygabplroy",
   "abplroygabplroyg",
   "bplroygabplroyga",
   "plroygabplroygab",
   "lroygabplroygabp"]

for y,row in enumerate(a):
    for x,col in enumerate(row):
        colour = black
        if col == "r":
            colour = red
        if col == "o":
            colour = orange
        if col == "y":
            colour = yellow
        if col == "g":
            colour = green
        if col == "a":
            colour = aqua
        if col == "b":
            colour = blue
        if col == "p":
            colour = purple
        if col == "l":
            colour = light_red

        
        print(f"{x} {y} {col} {colour}")
        uch.set_pixel(x, y, *colour)
uch.show()