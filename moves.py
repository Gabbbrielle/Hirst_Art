# class Moves():
#     import turtle
#     def __init__(self, name):
#         self.name = name.turtle()
#
#     def shape(self,sides, direction, thickness, length):
#         """by choosing the number of sides, you'll either draw a triangle, square, pentagon, hexagon, heptagon, octagon
#         nonagon or decagon. Length gives the length of sides"""
#         angle = 360 / sides
#         if sides != "circle":
#             for _ in range(sides):
#                 self.speed(0)
#                 if direction == "left":
#                     self.left(angle)
#                 else:
#                     self.rt(angle)
#                 self.circle(3)
#                 self.pensize(thickness)
#                 self.pencolor(new_color())
#                 self.forward(length)
#         else:
#             sides = self.circle(length)
#
#     def dashes(color, dash, length):
#         """move forward drawing a dashed line. Dash parameter allow for longer or
#         tighter dashes. Length = the distance to be covered. """
#         for _ in range(int(length / dash)):
#             ze.pencolor(color)
#             ze.forward(dash)
#             ze.penup()
#             ze.forward(dash)
#             ze.pendown()
#
#
#     def shape(name, sides, direction, thickness, length):
#     """by choosing the number of sides, you'll either draw a triangle, square, pentagon, hexagon, heptagon, octagon
#     nonagon or decagon. Length gives the length of sides"""
#     angle = 360 / sides
#     for _ in range(sides):
#         name.speed(0)
#         if direction == "left":
#             name.left(angle)
#         else:
#             name.rt(angle)
#         name.circle(3)
#         name.pensize(thickness)
#         name.pencolor(new_color())
#         name.forward(length)

    # def new_color():
    #     r = random.randint(0, 255)
    #     g = random.randint(0, 255)
    #     b = random.randint(0, 255)
    #     color = (r, g, b)
    #     return color

