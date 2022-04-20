'''
Name: Nathan Swinger
HW 5
'''
from tkinter import *
import tkinter.font
import math
class Pong(Frame):
    "A class to represent a game of Pong"

    def __init__(self):
        "Constructor for the class"
        Frame.__init__(self)
        self.master.title("Pong")
        self.grid()
        livesLeft = 5
        self.label = Label(self, font = "Verdana", text = "Lives left: " + str(livesLeft))
                                                                            
        self.label.grid()
        #making the canvas
        
        canvas_width = 800
        canvas_height = 400
        self.canvas = Canvas(self, width = canvas_width, height = canvas_height)
        self.canvas.grid()
        self.grid(row = 0, column = 0)
        #making the ball
        
        ball_diameter = 20
        top_left_x = 0
        top_left_y = 0
        self.canvas.create_oval(top_left_x, top_left_y, top_left_x + ball_diameter,
                                top_left_y + ball_diameter, fill = "red", tags = "ball")

        #making the paddle
        
        self.canvas.create_rectangle(360, 380, 440, 400, fill = "black", tags = "paddle")
        self.paddleTopX = 360
        self.paddleTopY = 380

        #Binding keyboard events
        
        self.canvas.bind("<Left>", self.movePaddleLeft)
        self.canvas.bind("<Right>", self.movePaddleRight)
        self.canvas.focus_set()
        
        #controlling the ball
                         
        startingdirection = "southeast"
        dy = 2
        dx = 2
        livesLeft = 5
        #checking for collision
        #move the ball
                         
        while True:
            try:
                if startingdirection == "southeast":
                    self.canvas.move("ball", dx, dy)
                    top_left_y += dy
                    top_left_x += dx
                    distance = math.sqrt((top_left_x-self.paddleTopX)**2 + (top_left_y-self.paddleTopY)**2)
                    if distance <= 30 and dy > 0:
                        dy = dy * -1
                    elif top_left_y + ball_diameter >= canvas_height or top_left_y < 0:
                        dy = dy * -1
                        if top_left_y + ball_diameter >= canvas_height:
                            livesLeft = livesLeft - 1
                            self.label["text"] = "Lives left: " + str(livesLeft)
                    if top_left_x + ball_diameter >= canvas_width or top_left_x < 0:
                        dx = dx * -1
                self.canvas.after(15)
                self.canvas.update()
                if livesLeft == 0:
                    self.canvas.delete("ball")
                    top_x, top_y = 2, 2
                    self.canvas.create_oval(top_x, top_y, top_x + ball_diameter,
                                            top_y + ball_diameter, fill = "red", tags = "ball")
                    break
            except:
                break
            

    def movePaddleRight(self, event):
        "A method to move the paddle right"
        if self.paddleTopX + 80 < 800:
            self.canvas.move("paddle", 5, 0)
            self.paddleTopX += 5

    def movePaddleLeft(self, event):
        "A method to move the paddle left"
        if self.paddleTopX > 0:
            self.canvas.move("paddle", -5, 0)
            self.paddleTopX -= 5
    
        
def main():
    Pong().mainloop()

main()
