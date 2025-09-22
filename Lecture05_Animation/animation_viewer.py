from pico2d import *
import time

open_canvas()

grass = load_image('grass.png')
character = load_image('sheet.png')

#jump 함수 sheet 프레임 크기 직접 설정 //좌표 직접 계산
location=[(90,25,120,225,130),(205,45,110,225,170),(310,70,123,225,190),
            (440,45,120,225,175),(555,25,116,225,150),(670,25,115,225,130),]

def stay(frame=0):
    x = 400
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 120 + 25, 717, 120, 238, x, 250, 500, 500)
    update_canvas()
    delay(0.1)

def run(frame=0):
    x = 400
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 120 + 10 + 730, 495, 116, 238, x, 250, 500, 500)
    update_canvas()
    delay(0.1)

def walk(frame=0):
    x = 400
    clear_canvas()
    grass.draw(400, 30)
    character.clip_draw(frame * 120 + 25, 495, 120, 238, x, 250, 500, 500)
    update_canvas()
    delay(0.1)

def jump(frame=0):
    x = 400
    clear_canvas()
    grass.draw(400, 30)
    sx, sy, sw, sh, y = location[frame % len(location)]
    character.clip_draw(sx, sy, sw, sh, x, y + 120, 500, 500)
    update_canvas()
    delay(0.1)

#코파일럿 도움
def repeat_animation(func, set_count=5, frame_count=6):
    for _ in range(set_count):
        for frame in range(frame_count):
            func(frame)
    delay(1)

while True:
    repeat_animation(stay)
    repeat_animation(walk)
    repeat_animation(run)
    repeat_animation(jump)

close_canvas()
