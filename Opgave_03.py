import arcade
import random


RES_HEIGHT = 1080 # Skærm højde
RES_WIDTH = 1920 # Skærmbredde


arcade.open_window(RES_WIDTH, RES_HEIGHT, "Min Tegning") # Åbner vindue med tegning


def generateboat(x,y):
    arcade.draw_rectangle_filled(x, y, 400, 150, arcade.color.DARK_BROWN)  # Bådens bund
    arcade.draw_rectangle_filled(x, y+120, 15, 210, arcade.color.DARK_BROWN)  # Bådens Mast

    arcade.draw_rectangle_filled(x-48, y+220, 110, 60, arcade.color.RED)  # Flag baggrund

    arcade.draw_rectangle_filled(x-48, y+220, 10, 60, arcade.color.WHITE)  # Kors 1
    arcade.draw_rectangle_filled(x-48, y+220, 110, 10, arcade.color.WHITE)  # Kors 2



def tegnvand(height, width, color): # Vand funktioner defineres på 3 variable højde, bredde og farve
    arcade.draw_lrtb_rectangle_filled(0, width, height, 0, color)



def generatestjerner(): # Stjerne generator
    centrum_x = random.randint(0, RES_WIDTH) # tilfældig centrum x
    centrum_y = random.randint(390, RES_HEIGHT) # tilfældig centrum y

    arcade.draw_circle_filled(centrum_x, centrum_y, 5, arcade.color.GOLD) # Tegner en stjerne med værdierne centrum_x og centrum_y



tegnvand(RES_HEIGHT/3, RES_WIDTH, arcade.color.SEA_BLUE) # køre vand funktionen
generateboat(630, 160) # Køre båd funktionen

for i in range(25): # for i in range betyder blot at den skal køre den 25 gange så den generer 25 stjerner
    generatestjerner()

arcade.finish_render()

# Get ready to draw
arcade.start_render()
# Keep the window up until someone closes it.
arcade.run()
