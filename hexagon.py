#!/usr/bin/python
# -*- coding: utf-8 -*-
  
from tkinter import *
from math import cos, sin, sqrt, radians

#------------------------------------------------------------------------------
class Field:
    types = {
        "grass": "#a1e2a1",
        "water": "#60ace6",
        "moutain": "#a1603a"
    } 
    def __init__(self, parent, x, y, kind, size):
        self.parent = parent
        self.x = x
        self.y = y
        self.kind = kind
        self.color = Field.types[self.kind]
        self.selected = False

    def draw(self):
        FillHexagon(self.parent, self.x, self.y, self.size, self.color)

    def enlight(self):
        pass

#------------------------------------------------------------------------------
class StrokeHexagon:
    def __init__(self, parent, x, y, length, color):
        self.parent = parent # canvas
        self.x = x           # top left x
        self.y = y           # top left y
        self.length = length # length of a side
        self.color = color   # outline color
        
        self.draw()

    def draw(self):
       
        start_x = self.x
        start_y = self.y
        angle = 60

        for i in range(6):
            end_x = start_x + self.length * cos(radians(angle * i))
            end_y = start_y + self.length * sin(radians(angle * i))
            self.parent.create_line(start_x,
                                    start_y,
                                    end_x,
                                    end_y,
                                    fill=self.color)
            start_x = end_x
            start_y = end_y

#------------------------------------------------------------------------------
class FillHexagon:
    def __init__(self, parent, x, y, length, color, tags):
        self.parent = parent # canvas
        self.x = x           # top left x
        self.y = y           # top left y
        self.length = length # length of a side
        self.color = color   # fill color

        self.selected = False
        self.tags = tags
        
        self.draw()

    def draw(self):
    	start_x = self.x
    	start_y = self.y
    	angle = 60
    	coords = []
    	for i in range(6):
    		end_x = start_x + self.length * cos(radians(angle * i))
    		end_y = start_y + self.length * sin(radians(angle * i))
    		coords.append([start_x, start_y])
    		start_x = end_x
    		start_y = end_y
    	self.parent.create_polygon(coords[0][0],
                                   coords[0][1], 
                                   coords[1][0], 
                                   coords[1][1],
                                   coords[2][0],
                                   coords[2][1],
                                   coords[3][0],
                                   coords[3][1],
                                   coords[4][0],
                                   coords[4][1], 
                                   coords[5][0],
                                   coords[5][1], 
                                   fill=self.color,
                                   outline="gray",
                                   tags=self.tags)
#---------------------------------------------------------
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Hexagon Grid")
        self.can = Canvas(self, width=400, height=300, bg="#a1e2a1")
        self.can.pack()

        self.hexagons = []
        self.initGrid(10, 7, 30, debug=False)

        self.can.bind("<Button-1>", self.click)
        
    def initGrid(self, cols, rows, size, debug):
        """
        2d grid of hexagons
        """
        for c in range(cols):
            if c % 2 == 0:
                offset = size * sqrt(3) / 2
            else:
                offset = 0
            for r in range(rows):
                
                h = FillHexagon(self.can,
                            c * (size * 1.5),
                            (r * (size * sqrt(3))) + offset ,
                            size,
                            "#a1e2a1",
                            "{}.{}".format(r, c))
                self.hexagons.append(h)

                if debug :
                    coords = "{}, {}".format(r, c)
                    self.can.create_text(c * (size * 1.5) + (size/2),
                                         (r * (size * sqrt(3))) + offset + (size/2),
                                         text=coords)

    def click(self, evt):
    	"""
		hexagon detection on mouse click
    	"""
    	x , y = evt.x, evt.y
    	for i in self.hexagons:
    		i.selected = False
    		i.isNeighbour = False
    		self.can.itemconfigure(i.tags, fill=i.color)
    	clicked = self.can.find_closest(x, y)[0] # find closest
    	self.hexagons[int(clicked)-1].selected = True
    	for i in self.hexagons: # re-configure selected only
    		if i.selected:
    			self.can.itemconfigure(i.tags, fill="#53ca53")
    		if i.isNeighbour:
    			self.can.itemconfigure(i.tags, fill="#76d576")
#----------------------------------------------------------
if __name__ =='__main__':
    app =App()
    app.mainloop()
