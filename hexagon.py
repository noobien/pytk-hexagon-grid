#!/usr/bin/python
# -*- coding: utf-8 -*-
  
from tkinter import *
from math import cos, sin, sqrt, radians

#----------------------------------------------------------
class Hexagon:
    def __init__(self, parent, x, y, length, color):
        self.parent = parent # canvas
        self.x = x           # top left x
        self.y = y           # top left y
        self.length = length # length of a side
        self.color = color   # fill color
        
        self.draw()

    def draw(self):
       
        start_x = self.x
        start_y = self.y
        angle = 60

        for i in range(6):
            end_x = start_x + self.length * cos(radians(angle * i))
            end_y = start_y + self.length * sin(radians(angle * i))
            self.parent.create_line(start_x, start_y, end_x, end_y, fill=self.color)
            start_x = end_x
            start_y = end_y
        
#---------------------------------------------------------
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Hexagon Grid")
        self.can = Canvas(self, width=800, height=600, bg="#a1e2a1")
        self.can.pack()

        self.initGrid(18, 12, 30)
        
    def initGrid(self, cols, rows, size):
        """
        2d grid of hexagons
        """
        for c in range(cols):
            if c % 2 == 0:
                offset = size * sqrt(3) / 2
            else:
                offset = 0
            for r in range(rows):
                
                h = Hexagon(self.can,
                                   c * (size * 1.5),
                                   (r * (size * sqrt(3))) + offset ,
                                   6,
                                   size,
                                   "#71471e")

                # debug :
                # coords = "{}, {}".format(r, c)
                # self.can.create_text(c * (size * 1.5) + (size/2),
                #                    (r * (size * sqrt(3))) + offset + (size/2),
                #                    text=coords)
#----------------------------------------------------------
if __name__ =='__main__':
    app =App()
    app.mainloop()