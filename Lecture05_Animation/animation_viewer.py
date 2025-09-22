from pico2d import *

open_canvas()

grass = load_image('grass.png')
character = load_image('sheet.png')


def stay():
    frame = 0
    x = 400
    while True:
        clear_canvas()
        grass.draw(400, 30)
        character.clip_draw(frame * 125 + 15, 717, 125, 238, x, 130, 200, 200)

        update_canvas()
        frame = (frame + 1) % 6
        delay(0.1)


def run():
    pass

def walk():
    pass

def jump():
    pass

def ouch():
    pass

while True:
    stay()

close_canvas()

