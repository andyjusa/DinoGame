import pygame.event

from Colors import *
from Base import *

import random

base = r"resources/"

pygame.init()

started = False
size = [1500, 300]
screen = pygame.display.set_mode(size)
done = False
clock = pygame.time.Clock()

debugging = True
pressedKeys = []
frameRate = 60
gravity = 1
gravitySpeed = 0
jumpSpeed = 1
jumpAvailable = True
df = 0
off = 0
jumped = False
catus = 2
score = 10000
gameSpeed = 1

high = 0

GameObject(
    name='Player',
    image=pygame.image.load(base + "Idle.png"),
    size=(1, 1),
    position=(20, 200),
    collider=True
)
animManager(
    targetName='Player',
    animList=[
        'Idle.png',
        (f'Running{i}.png' for i in range(0, 2)),
        'Jump.png',
        'DIed.png'
    ],
    animOptions=[
        animOption(
            timing=1,
            num=1,
            offset=(0, 4.5)
        ),
        animOption(
            timing=200,
            num=2,
            offset=(0, 0)
        ),
        animOption(
            timing=1,
            num=1,
            offset=(0, 0)
        ),
        animOption(
            timing=1,
            num=1,
            offset=(0, 0)
        )
    ],
    resourceAddr=f'{base}',
    animCondition=[(lambda event: True), (lambda event: globals()['started']),
                   (lambda event: globals()['jumped']), (lambda event: not globals()['started'] and not globals()['score'] == 10000)
                   ]
)
GameObject(
    name='Ground0',
    image=pygame.image.load(base + "Ground.png"),
    size=(1, 1),
    position=(0, 270),
    collider=False
)
GameObject(
    name='Ground1',
    image=pygame.image.load(base + "Ground.png"),
    size=(1, 1),
    position=(2300, 270),
    collider=False
)
GameObject(
    name="Gameover",
    image=pygame.image.load(base + "Gameover.png"),
    size=(1, 1),
    position=(500,100),
    collider=False
)
animManager(
        targetName=f'Gameover',
        animList=[
            'Gameover.png' for i in range(0,2)
        ],
        animOptions=[
            animOption(
                timing=1,
                num=1,
                offset=(0, 800)
            ),
            animOption(
                timing=1,
                num=1,
                offset=(0, 0)
            )
        ],
        resourceAddr=f'{base}',
        animCondition=[(lambda event: True), (lambda event: not globals()['started'] and not globals()['score'] == 10000)]
    )
for i in range(0, 6):
    GameObject(
        name=f'Catus{i}',
        image=pygame.image.load(base + ('Catus' if i < 3 else 'Minicatus') + f'{i % 3}.png'),
        size=(1, 1),
        position=(1600, 200 if i < 3 else 220),
        collider=True
    )
    animManager(
        targetName=f'Catus{i}',
        animList=[
            ('Catus' if i < 3 else 'Minicatus') + f'{i % 3}.png'
        ],
        animOptions=[
            animOption(
                timing=1,
                num=1,
                offset=(0, 0)
            )
        ],
        resourceAddr=f'{base}',
        animCondition=[(lambda event: True)]
    )

GameObject(
    name=f'Num0',
    image=pygame.image.load(base + '0.png'),
    size=(1, 1),
    position=(1300 - 0 * 20, 20),
    collider=False
)
GameObject(
    name=f'Num1',
    image=pygame.image.load(base + '0.png'),
    size=(1, 1),
    position=(1300 - 1 * 20, 20),
    collider=False
)
GameObject(
    name=f'Num2',
    image=pygame.image.load(base + '0.png'),
    size=(1, 1),
    position=(1300 - 2 * 20, 20),
    collider=False
)
GameObject(
    name=f'Num3',
    image=pygame.image.load(base + '0.png'),
    size=(1, 1),
    position=(1300 - 3 * 20, 20),
    collider=False
)
GameObject(
    name=f'HINum0',
    image=pygame.image.load(base + '0.png'),
    size=(1, 1),
    position=(1300 - 5 * 20, 20),
    collider=False
)
GameObject(
    name=f'HINum1',
    image=pygame.image.load(base + '0.png'),
    size=(1, 1),
    position=(1300 - 6 * 20, 20),
    collider=False
)
GameObject(
    name=f'HINum2',
    image=pygame.image.load(base + '0.png'),
    size=(1, 1),
    position=(1300 - 7 * 20, 20),
    collider=False
)
GameObject(
    name=f'HINum3',
    image=pygame.image.load(base + '0.png'),
    size=(1, 1),
    position=(1300 - 8 * 20, 20),
    collider=False
)
GameObject(
    name=f'HI',
    image=pygame.image.load(base + 'HI.png'),
    size=(1, 1),
    position=(1300 - 11 * 20, 20),
    collider=False
)
animManager(
    targetName=f'Num0',
    animList=[
        f'{a}.png' for a in range(0, 10)
    ],
    animOptions=[
        animOption(
            timing=1,
            num=1,
            offset=(0, 0)
        ) for a in range(0, 10)
    ],
    resourceAddr=f'{base}',
    animCondition=[(lambda event: globals()['score'] < 10 ** 0 or str(globals()['score'])[-1] == '0'),
                   (lambda event: globals()['score'] > 10 ** 0 and str(globals()['score'])[-1] == '1'),
                   (lambda event: globals()['score'] > 10 ** 0 and str(globals()['score'])[-1] == '2'),
                   (lambda event: globals()['score'] > 10 ** 0 and str(globals()['score'])[-1] == '3'),
                   (lambda event: globals()['score'] > 10 ** 0 and str(globals()['score'])[-1] == '4'),
                   (lambda event: globals()['score'] > 10 ** 0 and str(globals()['score'])[-1] == '5'),
                   (lambda event: globals()['score'] > 10 ** 0 and str(globals()['score'])[-1] == '6'),
                   (lambda event: globals()['score'] > 10 ** 0 and str(globals()['score'])[-1] == '7'),
                   (lambda event: globals()['score'] > 10 ** 0 and str(globals()['score'])[-1] == '8'),
                   (lambda event: globals()['score'] > 10 ** 0 and str(globals()['score'])[-1] == '9')]
)
animManager(
    targetName=f'Num1',
    animList=[
        f'{a}.png' for a in range(0, 10)
    ],
    animOptions=[
        animOption(
            timing=1,
            num=1,
            offset=(0, 0)
        ) for a in range(0, 10)
    ],
    resourceAddr=f'{base}',
    animCondition=[(lambda event: globals()['score'] < 10 ** 1 or str(globals()['score'])[-2] == '0'),
                   (lambda event: globals()['score'] > 10 ** 1 and str(globals()['score'])[-2] == '1'),
                   (lambda event: globals()['score'] > 10 ** 1 and str(globals()['score'])[-2] == '2'),
                   (lambda event: globals()['score'] > 10 ** 1 and str(globals()['score'])[-2] == '3'),
                   (lambda event: globals()['score'] > 10 ** 1 and str(globals()['score'])[-2] == '4'),
                   (lambda event: globals()['score'] > 10 ** 1 and str(globals()['score'])[-2] == '5'),
                   (lambda event: globals()['score'] > 10 ** 1 and str(globals()['score'])[-2] == '6'),
                   (lambda event: globals()['score'] > 10 ** 1 and str(globals()['score'])[-2] == '7'),
                   (lambda event: globals()['score'] > 10 ** 1 and str(globals()['score'])[-2] == '8'),
                   (lambda event: globals()['score'] > 10 ** 1 and str(globals()['score'])[-2] == '9')]
)
animManager(
    targetName=f'Num2',
    animList=[
        f'{a}.png' for a in range(0, 10)
    ],
    animOptions=[
        animOption(
            timing=1,
            num=1,
            offset=(0, 0)
        ) for a in range(0, 10)
    ],
    resourceAddr=f'{base}',
    animCondition=[(lambda event: globals()['score'] < 10 ** 2 or str(globals()['score'])[-3] == '0'),
                   (lambda event: globals()['score'] > 10 ** 2 and str(globals()['score'])[-3] == '1'),
                   (lambda event: globals()['score'] > 10 ** 2 and str(globals()['score'])[-3] == '2'),
                   (lambda event: globals()['score'] > 10 ** 2 and str(globals()['score'])[-3] == '3'),
                   (lambda event: globals()['score'] > 10 ** 2 and str(globals()['score'])[-3] == '4'),
                   (lambda event: globals()['score'] > 10 ** 2 and str(globals()['score'])[-3] == '5'),
                   (lambda event: globals()['score'] > 10 ** 2 and str(globals()['score'])[-3] == '6'),
                   (lambda event: globals()['score'] > 10 ** 2 and str(globals()['score'])[-3] == '7'),
                   (lambda event: globals()['score'] > 10 ** 2 and str(globals()['score'])[-3] == '8'),
                   (lambda event: globals()['score'] > 10 ** 2 and str(globals()['score'])[-3] == '9')]
)
animManager(
    targetName=f'Num3',
    animList=[
        f'{a}.png' for a in range(0, 10)
    ],
    animOptions=[
        animOption(
            timing=1,
            num=1,
            offset=(0, 0)
        ) for a in range(0, 10)
    ],
    resourceAddr=f'{base}',
    animCondition=[(lambda event: globals()['score'] < 10 ** 3 or str(globals()['score'])[-4] == '0'),
                   (lambda event: globals()['score'] > 10 ** 3 and str(globals()['score'])[-4] == '1'),
                   (lambda event: globals()['score'] > 10 ** 3 and str(globals()['score'])[-4] == '2'),
                   (lambda event: globals()['score'] > 10 ** 3 and str(globals()['score'])[-4] == '3'),
                   (lambda event: globals()['score'] > 10 ** 3 and str(globals()['score'])[-4] == '4'),
                   (lambda event: globals()['score'] > 10 ** 3 and str(globals()['score'])[-4] == '5'),
                   (lambda event: globals()['score'] > 10 ** 3 and str(globals()['score'])[-4] == '6'),
                   (lambda event: globals()['score'] > 10 ** 3 and str(globals()['score'])[-4] == '7'),
                   (lambda event: globals()['score'] > 10 ** 3 and str(globals()['score'])[-4] == '8'),
                   (lambda event: globals()['score'] > 10 ** 3 and str(globals()['score'])[-4] == '9')]
)
animManager(
    targetName=f'HINum0',
    animList=[
        f'{a}.png' for a in range(0, 10)
    ],
    animOptions=[
        animOption(
            timing=1,
            num=1,
            offset=(0, 0)
        ) for a in range(0, 10)
    ],
    resourceAddr=f'{base}',
    animCondition=[(lambda event: globals()['high'] < 10 ** 0 or str(globals()['high'])[-1] == '0'),
                   (lambda event: globals()['high'] > 10 ** 0 and str(globals()['high'])[-1] == '1'),
                   (lambda event: globals()['high'] > 10 ** 0 and str(globals()['high'])[-1] == '2'),
                   (lambda event: globals()['high'] > 10 ** 0 and str(globals()['high'])[-1] == '3'),
                   (lambda event: globals()['high'] > 10 ** 0 and str(globals()['high'])[-1] == '4'),
                   (lambda event: globals()['high'] > 10 ** 0 and str(globals()['high'])[-1] == '5'),
                   (lambda event: globals()['high'] > 10 ** 0 and str(globals()['high'])[-1] == '6'),
                   (lambda event: globals()['high'] > 10 ** 0 and str(globals()['high'])[-1] == '7'),
                   (lambda event: globals()['high'] > 10 ** 0 and str(globals()['high'])[-1] == '8'),
                   (lambda event: globals()['high'] > 10 ** 0 and str(globals()['high'])[-1] == '9')]
)
animManager(
    targetName=f'HINum1',
    animList=[
        f'{a}.png' for a in range(0, 10)
    ],
    animOptions=[
        animOption(
            timing=1,
            num=1,
            offset=(0, 0)
        ) for a in range(0, 10)
    ],
    resourceAddr=f'{base}',
    animCondition=[(lambda event: globals()['high'] < 10 ** 1 or str(globals()['high'])[-2] == '0'),
                   (lambda event: globals()['high'] > 10 ** 1 and str(globals()['high'])[-2] == '1'),
                   (lambda event: globals()['high'] > 10 ** 1 and str(globals()['high'])[-2] == '2'),
                   (lambda event: globals()['high'] > 10 ** 1 and str(globals()['high'])[-2] == '3'),
                   (lambda event: globals()['high'] > 10 ** 1 and str(globals()['high'])[-2] == '4'),
                   (lambda event: globals()['high'] > 10 ** 1 and str(globals()['high'])[-2] == '5'),
                   (lambda event: globals()['high'] > 10 ** 1 and str(globals()['high'])[-2] == '6'),
                   (lambda event: globals()['high'] > 10 ** 1 and str(globals()['high'])[-2] == '7'),
                   (lambda event: globals()['high'] > 10 ** 1 and str(globals()['high'])[-2] == '8'),
                   (lambda event: globals()['high'] > 10 ** 1 and str(globals()['high'])[-2] == '9')]
)
animManager(
    targetName=f'HINum2',
    animList=[
        f'{a}.png' for a in range(0, 10)
    ],
    animOptions=[
        animOption(
            timing=1,
            num=1,
            offset=(0, 0)
        ) for a in range(0, 10)
    ],
    resourceAddr=f'{base}',
    animCondition=[(lambda event: globals()['high'] < 10 ** 2 or str(globals()['high'])[-3] == '0'),
                   (lambda event: globals()['high'] > 10 ** 2 and str(globals()['high'])[-3] == '1'),
                   (lambda event: globals()['high'] > 10 ** 2 and str(globals()['high'])[-3] == '2'),
                   (lambda event: globals()['high'] > 10 ** 2 and str(globals()['high'])[-3] == '3'),
                   (lambda event: globals()['high'] > 10 ** 2 and str(globals()['high'])[-3] == '4'),
                   (lambda event: globals()['high'] > 10 ** 2 and str(globals()['high'])[-3] == '5'),
                   (lambda event: globals()['high'] > 10 ** 2 and str(globals()['high'])[-3] == '6'),
                   (lambda event: globals()['high'] > 10 ** 2 and str(globals()['high'])[-3] == '7'),
                   (lambda event: globals()['high'] > 10 ** 2 and str(globals()['high'])[-3] == '8'),
                   (lambda event: globals()['high'] > 10 ** 2 and str(globals()['high'])[-3] == '9')]
)
animManager(
    targetName=f'HINum3',
    animList=[
        f'{a}.png' for a in range(0, 10)
    ],
    animOptions=[
        animOption(
            timing=1,
            num=1,
            offset=(0, 0)
        ) for a in range(0, 10)
    ],
    resourceAddr=f'{base}',
    animCondition=[(lambda event: globals()['high'] < 10 ** 3 or str(globals()['high'])[-4] == '0'),
                   (lambda event: globals()['high'] > 10 ** 3 and str(globals()['high'])[-4] == '1'),
                   (lambda event: globals()['high'] > 10 ** 3 and str(globals()['high'])[-4] == '2'),
                   (lambda event: globals()['high'] > 10 ** 3 and str(globals()['high'])[-4] == '3'),
                   (lambda event: globals()['high'] > 10 ** 3 and str(globals()['high'])[-4] == '4'),
                   (lambda event: globals()['high'] > 10 ** 3 and str(globals()['high'])[-4] == '5'),
                   (lambda event: globals()['high'] > 10 ** 3 and str(globals()['high'])[-4] == '6'),
                   (lambda event: globals()['high'] > 10 ** 3 and str(globals()['high'])[-4] == '7'),
                   (lambda event: globals()['high'] > 10 ** 3 and str(globals()['high'])[-4] == '8'),
                   (lambda event: globals()['high'] > 10 ** 3 and str(globals()['high'])[-4] == '9')]
)


@colliderDef('Player')
def onCollider(target):
    global started, high, score
    if target[:5] == 'Catus' and started:
        started = False
        removeKey(32)
        if high < score:
            high = score


@keyDef(pygame.K_SPACE)
def jump():
    global jumped, jumpSpeed, gravitySpeed, score, started
    if not jumped:
        jumpSpeed = 17 * gameSpeed
        jumped = True
        gravitySpeed = 0
    if not started:
        score = 0
        started = True
        for i in range(0, 6):
            catus: GameObject = getGameObj(f'Catus{i}')
            catus.Moveto(1600, 200 if i < 3 else 220)


@keyUpDef(pygame.K_SPACE)
def jumpUp():
    global gravitySpeed
    global jumpSpeed
    if jumped and gravitySpeed < jumpSpeed:
        gravitySpeed = 0
        jumpSpeed = 0


def everyTime():
    global gravitySpeed, jumpSpeed, jumped, catus, score, off
    if started:
        off += df
        if off >= 60:
            off -= 60
            score += 1
        ground0: GameObject = getGameObj('Ground0')
        ground1: GameObject = getGameObj('Ground1')
        player: GameObject = getGameObj('Player')
        catusObj: GameObject = getGameObj(f'Catus{catus}')
        ground0.x -= 15 * gameSpeed
        ground1.x -= 15 * gameSpeed
        catusObj.x -= 15 * gameSpeed
        if ground1.x <= -2300:
            ground1.x += 4600
        if ground0.x <= -2300:
            ground0.x += 4600
        if jumped:
            gravitySpeed += gravity * gameSpeed
            player.y += (gravitySpeed - jumpSpeed) / gameSpeed
            if player.y >= 200:
                jumpSpeed = 0
                jumped = False
                player.y = 200
        if player.y >= 200:
            jumped = False
        if catusObj.x <= -150:
            catusObj.x = 1600
            catus = random.randint(0, 5)


def RunGame():
    global done
    global df
    while not done:
        everyTime()
        df = clock.tick(frameRate)
        screen.fill(WALLPAPER.rgb)
        loop(pygame.event.get(), screen, df)
        pygame.display.update()


@eventDef(pygame.QUIT)
def onQuit(event):
    global done
    done = True


@eventDef(pygame.TEXTINPUT)
def onTextInput(event):
    pass


RunGame()
pygame.quit()
