from pico2d import *
import time

open_canvas()

grass = load_image('grass.png')
character = load_image('sheet.png')


location =[(80,25,115,225,130),(190,45,115,225,150),(300,70,955-870,225,170),(410,45,115,225,155),(520,25,115,225,130)]
location2 =[(90,25,120,225,130),(205,45,310-200,225,150),(310,70,433-310,225,170),
            (440,45,554-434,225,155),(555,25,668-552,225,130),(670,25,785-670,225,130),]
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
    frame = 0
    x = 400
    while True:
        clear_canvas()
        grass.draw(400, 30)
        sx, sy, sw, sh,y = location2[frame % len(location)]
        character.clip_draw(sx , sy, sw, sh , x, y, 200, 200)
        #character2.clip_draw(sx,sy, sw, sh , x, y, sw, sh)

        update_canvas()
        frame = (frame + 1) % 6
        delay(0.1)


def ouch():
    pass

while True:
    #stay()
    #walk()
    #run()
    jump()

close_canvas()

