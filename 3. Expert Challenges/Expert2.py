import unicornhathd as uch
uch.brightness(0.5)

fav = input("What's your favourite colour? ")

if fav == "red":
    uch.set_all(255,0,0)
if fav == "orange":
    uch.set_all(255,165,0)
if fav == "yellow":
    uch.set_all(255,255,0)
if fav == "green":
    uch.set_all(0,255,0)
if fav == "aqua":
    uch.set_all(0,255,255)
if fav == "blue":
    uch.set_all(0,0,255)
if fav == "purple":
    uch.set_all(255,0,255)
if fav == "pink":
    uch.set_all(255,192,203)

uch.show()