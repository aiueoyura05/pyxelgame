#
# 黄泉の国脱出RPGゲーム
# tt2095yi 稲垣響
#

import pyxel

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2
SCENE_GAMECLEAR = 3
SCENE_NEW = 4
SCENE_SETUMEI = 5

STAR_COLOR_HIGH = 12
STAR_COLOR_LOW = 5

score = 0
life  = 3
add = 0
zax = 16
zay = 32

class Boy:
    def __init__(self):
        self.px = 2
        self.py = 5

    def update(self):
        self.scene = SCENE_PLAY

    def move(self,map,dx,dy):
        global score, life, add ,zay,zax

        #通路
        if pyxel.tilemap(1).pget(self.px + dx, self.py + dy) == (10,0):
            self.px += dx
            self.py += dy
            map.move(self.px)

        #コイン判定後の通り道を作る方法
        if pyxel.tilemap(1).pget(self.px + dx, self.py + dy) == (22, 0):
            self.px += dx
            self.py += dy

        #隠し通路
        if pyxel.tilemap(1).pget(self.px + dx, self.py + dy) == (9, 5):
            self.px += dx
            self.py += dy
            map.move(self.px)
        if pyxel.tilemap(1).pget(self.px + dx, self.py + dy) == (14, 0):
            self.px += dx
            self.py += dy
            map.move(self.px)

        #墓、隠しコース
        if pyxel.tilemap(1).pget(self.px + dx, self.py + dy) == (8,19):
            add += 1

        #コイン判定
        if (11,3) == pyxel.tilemap(1).pget(self.px + dx,self.py + dy):
            pyxel.tilemap(1).pset(self.px + dx,self.py + dy,(22,0))
            pyxel.play(2,4,loop = False)
            score += 1

        #トラップ火の玉、猫出現
        if (13,6) == pyxel.tilemap(1).pget(self.px + dx,self.py + dy):
            pyxel.tilemap(1).pset(self.px + dx,self.py + dy,(10,14))
            life -= 1
            pyxel.play(1,0,loop = False)

        #マップ上の敵と当たり判定、効果音
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (0,0):
            life -= 1
            pyxel.play(1,0,loop = False)
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (4,0):
            life -= 1
            pyxel.play(1,0,loop = False)
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (2,2):
            life -= 1
            pyxel.play(1,0,loop = False)
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (1,22):
            life -= 1
            pyxel.play(1,0,loop = False)
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (2,22):
            life -= 1
            pyxel.play(1,0,loop = False)
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (3,22):
            life -= 1
            pyxel.play(1,0,loop = False)

        #主人公の画像替え
        if pyxel.btnp(pyxel.KEY_UP):
            zax = 184
            zay = 224
        if pyxel.btnp(pyxel.KEY_DOWN):
            zax = 200
            zay = 240
        if pyxel.btnp(pyxel.KEY_RIGHT):
            zax = 16
            zay = 32
        if pyxel.btnp(pyxel.KEY_LEFT):
            zax = 216
            zay = 224


    def draw(self,map):
        global zay,zax
        pyxel.blt((self.px - map.offset) * 8, self.py * 8 ,0,zax+16* ((pyxel.frame_count // 15) % 2), zay, 16, 16, 0)
        for i in range(life):
            pyxel.blt(i * 8 + 5, 12, 0, 104, 88, 8, 8, 0)

class Boy2():
    def __init__(self):
        self.px = 5
        self.py = 65

    def update(self):
        self.scene = SCENE_NEW

    def move(self,dx,dy):
        print(pyxel.tilemap(2).pget(self.px + dx, self.py + dy))
        if pyxel.tilemap(2).pget(self.px + dx, self.py + dy) == (0,0):
            self.px += dx
            self.py += dy
        print(pyxel.tilemap(2).pget(self.px + dx, self.py + dy))
        if pyxel.tilemap(2).pget(self.px + dx, self.py + dy) == (14,0):
            self.px += dx
            self.py += dy

    def draw(self):
        pyxel.blt(self.px,self.py,0,16+16 * ((pyxel.frame_count // 15) % 2), 32, 16, 16, 0)

class Fire():
    def __init__(self):
        self.x = pyxel.rndi(30,55)
        self.y =pyxel.rndi(40,85)
        #通路に来ないように設定

    def update(self):
        pass

    def draw(self):
        pyxel.blt( self.x,self.y , 0, 32+16 * ((pyxel.frame_count // 15) % 2), 96 , 16, 16, 0)

class Background:
    def __init__(self):
        self.stars = []
        for i in range(500):
            self.stars.append(
                (
                    pyxel.rndi(0, 200 ),
                    pyxel.rndi(0, 135 ),
                    pyxel.rndf(1, 2.5),
                )
            )

    def update(self):
        for i, (x, y, speed) in enumerate(self.stars):
            y += speed
            if y >= 135:
                y -= 135
            self.stars[i] = (x, y, speed)

    def draw(self):
        for (x, y, speed) in self.stars:
            pyxel.pset(x, y, STAR_COLOR_HIGH if speed > 1.8 else STAR_COLOR_LOW)

class Map:
    def __init__(self):
        self.offset = 0

    def move(self, px):
        if px - self.offset >= 14:
            self.offset += 1
        elif px - self.offset <= 1 and self.offset > 1:
            self.offset -= 1

    def draw(self):
        pyxel.bltm(0,0,1,self.offset * 8,0,560,135)


class App:
    def __init__(self):
        pyxel.init(150, 135)
        pyxel.load("my_resource.pyxres")
        self.scene = SCENE_SETUMEI
        self.map = Map()
        self.boy =Boy()
        self.boy2 = Boy2()
        self.fire = Fire()
        self.reset()
        self.backgroud = Background()
        pyxel.run(self.update, self.draw)

    def reset(self):
        global score,life,add
        pyxel.load("my_resource.pyxres")
        score = 0
        life  = 3
        add = 0

    def update(self):
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_SETUMEI:
            self.update_setumei_scene()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene()
        elif self.scene ==SCENE_GAMEOVER:
            self.update_gameover_scene()
        elif self.scene ==SCENE_GAMECLEAR:
            self.update_gameclear_scene()
        elif self.scene == SCENE_NEW:
            self.update_new_scene()

    def update_title_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            pyxel.playm(0, loop=True)
            self.scene = SCENE_PLAY

    def update_setumei_scene(self):
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = SCENE_TITLE

    def update_play_scene(self):

        self.backgroud.update()
        if pyxel.btnp(pyxel.KEY_UP):
           self.boy.move(self.map,0, -1)
        if pyxel.btnp(pyxel.KEY_DOWN):
           self.boy.move(self.map,0, 1)
        if pyxel.btnp(pyxel.KEY_RIGHT):
           self.boy.move(self.map,1, 0)
        if pyxel.btnp(pyxel.KEY_LEFT):
           self.boy.move(self.map,-1, 0)

        if score == 7:
            pyxel.stop()
            pyxel.playm(3, loop=True)
            self.scene= SCENE_GAMECLEAR

        if life == 0:
            pyxel.stop()
            pyxel.playm(7, loop=True)
            self.scene=SCENE_GAMEOVER

        if add == 1:
            self.scene= SCENE_NEW

    def update_gameover_scene(self):
        global add,life
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.reset()
            self.scene = SCENE_TITLE

    def update_gameclear_scene(self):
        pass

    def update_new_scene(self):
        global add

        if pyxel.btnp(pyxel.KEY_UP):
           self.boy2.move(0, -5)
        if pyxel.btnp(pyxel.KEY_DOWN):
           self.boy2.move(0, 5)
        if pyxel.btnp(pyxel.KEY_RIGHT):
           self.boy2.move(5, 0)
        if pyxel.btnp(pyxel.KEY_LEFT):
           self.boy2.move(-5, 0)

        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = SCENE_PLAY
            add += 1

    def draw(self):

        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()
        elif self.scene ==SCENE_GAMEOVER:
            self.draw_gameover_scene()
        elif self.scene ==SCENE_GAMECLEAR:
            self.draw_gameclear_scene()
        elif self.scene == SCENE_NEW:
            self.draw_new_scene()
        elif self.scene == SCENE_SETUMEI:
            self.draw_setumei_scene()

    def draw_title_scene(self):
        pyxel.cls(0)
        pyxel.text(57, 50, "GAME START", 8)
        pyxel.blt(48,60,  0, 16 * ((pyxel.frame_count // 15) % 2),0, 16, 16, 0)
        pyxel.blt(62,60,  0, 16+16 * ((pyxel.frame_count // 15) % 2),16, 16, 16, 0)
        pyxel.blt(76,60,  0, 32+16 * ((pyxel.frame_count // 15) % 2),0, 16, 16, 0)
        pyxel.blt(90,60,  0, 24+16 * ((pyxel.frame_count // 15) % 2),72, 16, 16, 0)

    def draw_setumei_scene(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,4,0,0,150,135)
        pyxel.blt(56,12, 0, 32+16 * ((pyxel.frame_count // 15) % 2), 96 , 16, 16, 0)
        pyxel.blt(104,44,0,144+16 * ((pyxel.frame_count // 15) % 2), 72, 16, 16, 0)
        pyxel.blt(24,75,  0, 16 * ((pyxel.frame_count // 15) % 2),0, 16, 16, 0)
        pyxel.blt(38,75,  0, 16+16 * ((pyxel.frame_count // 15) % 2),16, 16, 16, 0)
        pyxel.blt(52,75,  0, 32+16 * ((pyxel.frame_count // 15) % 2),0, 16, 16, 0)
        pyxel.blt(66,75,  0, 24+16 * ((pyxel.frame_count // 15) % 2),72, 16, 16, 0)


    def draw_play_scene(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,1,0,0,560,135)
        self.map.draw()
        self.boy.draw(self.map)
        self.fire.draw()
        self.backgroud.draw()
        pyxel.text(2, 5, "SCORE:" + str(score), 7)


    def draw_gameover_scene(self):
        pyxel.cls(0)
        pyxel.blt(65,65 ,  0, 32+16 * ((pyxel.frame_count // 15) % 2),56 , 16, 16, 0)
        pyxel.text(55, 50, "GAME OVER", 8)
        pyxel.text(25, 100, "- PRESS ENTER TO RESTART -", 6)

    def draw_new_scene(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,2,0,0,150,135)
        self.boy2.draw()
        pyxel.text(2, 5, "隠しマップ" , 7)

    def draw_gameclear_scene(self):
        pyxel.cls(0)
        pyxel.bltm(0,0,3,0,0,150,135)
        pyxel.blt(65,55,  0, 16 * ((pyxel.frame_count // 15) % 2),240, 16, 16, 0)
        pyxel.text(55,80 ,"GAME CLEAR", 10)
        pyxel.text(45,90, "CONGRATULATIONS!", 10)
        pyxel.text(71, 140, "- PRESS ENTER -", 6)

App()
