import pygame as py 

#colors
red = (255,0,0)
green = (0, 255, 0)
blue = (26, 224, 235)
dark_blue = (14, 29, 237)
orange = (217, 158, 33)
yellow = (249, 252, 38)
purple = (181, 4, 217)
black = (0, 0, 0)
grey_border = (31,31,31)
pinkish = (177, 189, 87)
background = (90,90,90)

colors = [blue, dark_blue, orange, yellow, green, purple, red]

py.init()


#sceen dimensions
buffer = 80
winHeiht = 960 + buffer
winWight = 400 + buffer


win = py.display.set_mode((winWight, winHeiht))


