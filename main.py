import turtle
from tkinter import messagebox
from turtle import Turtle, Screen, clear
import subprocess
import random
import colorgram
turtle.colormode(255)
LARGE_FONT= ("Verdana", 12)
NORM_FONT = ("Helvetica", 10)
SMALL_FONT = ("Helvetica", 8)


def get_colors(image, num_of_colors):
    paint_colors = []
    for color in colorgram.extract(image, num_of_colors):
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        color_set = (r, g, b)
        paint_colors.append(color_set)
    return paint_colors


dots = get_colors('hirst_palet.webp', 30)
ze = Turtle()
ze.hideturtle()
ze.penup()
ze.goto(-300, -250)


def next_line(direction, spaces):
    if direction == 'left':
        ze.left(90)
        ze.forward(spaces + 60)
        ze.left(90)
    elif direction == 'right':
        ze.right(90)
        ze.forward(spaces)
        ze.right(90)


def make_line(dot_size, spaces, dot_num):
    """Makes a line starting with a in-place dot then draws the rest of the row.\n
    dot_size = circumference\nspaces = space between each dot\ndot_num = number of dots in each row"""
    ze.speed(0)
    ze.color(random.choice(dots))
    ze.down()
    ze.begin_fill()
    ze.circle(dot_size)
    ze.end_fill()
    ze.up()
    for dot in range(dot_num - 1):
        ze.speed(0)
        ze.forward(spaces)
        ze.color(random.choice(dots))
        ze.down()
        ze.begin_fill()
        ze.circle(dot_size)
        ze.end_fill()
        ze.up()


def make_hirst(rows):
    start = -250
    for lines in range(rows):
        ze.speed(0)
        ze.goto(-300, start)
        make_line(10, 60, rows)
        start += 60


def disco_hirst(times, rows):
    """Will make a Hirst painting of requested rows repeatedly for the requested times"""
    for num in range(times):
        make_hirst(rows)


like_it = False
while like_it is False:
    make_hirst(10)
    like = turtle.textinput("another?","Do you like it? y or n: ")
    if like == "n":
        continue
    if like == 'y':
        windows = turtle.textinput('Want it?', 'Are you on a Windows computer? y or n: ')
        if windows == 'y':
            subprocess.Popen(["snippingtool.exe"])
        else:
            messagebox.showinfo("Screen Grab", "Use your screenshot app of choice")
        like_it = True

# disco_hirst(3, 9)
screen = Screen()
screen.exitonclick()
