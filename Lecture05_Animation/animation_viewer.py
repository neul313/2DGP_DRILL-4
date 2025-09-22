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
        character.clip_draw(frame * 120 + 25, 717, 120, 238, x, 130, 200, 200)

        update_canvas()
        frame = (frame + 1) % 6
        delay(0.1)


def run():
    frame = 0
    x = 400
    while True:
        clear_canvas()
        grass.draw(400, 30)

        character.clip_draw(frame * 120 + 10 + 730, 955 - 460, 116, 238, x, 130, 200, 200)

        update_canvas()
        frame = (frame + 1) % 6
        delay(0.1)
    pass


def walk():
    frame = 0
    x = 400
    while True:
        clear_canvas()
        grass.draw(400, 30)

        character.clip_draw(frame * 120 + 25, 955 - 460, 120, 238, x, 130, 200, 200)

        update_canvas()
        frame = (frame + 1) % 6
        delay(0.1)


def jump():
    pass

def ouch():
    pass

while True:
    #stay()
    #walk()
    run()
    #jump()

close_canvas()

