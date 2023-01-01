import pyxel

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2
SCENE_GAMECLEAR = 3


class Boy:
    def __init__(self):
        self.px = 2
        self.py = 5
        self.life = 2

    def update(self):
        pass
    
    def move(self,map,dx,dy):
        #通路
        if pyxel.tilemap(1).pget(self.px + dx, self.py + dy) == (10, 0):
            self.px += dx
            self.py += dy
            map.move(self.px)
        
        #隠し通路
        if pyxel.tilemap(1).pget(self.px + dx, self.py + dy) == (9, 5):
            self.px += dx
            self.py += dy
            map.move(self.px)
        if pyxel.tilemap(1).pget(self.px + dx, self.py + dy) == (14, 0):
            self.px += dx
            self.py += dy
            map.move(self.px)
        
        print(pyxel.tilemap(1).pget(self.px + dx, self.py + dy))
        #マップ上の敵と当たり判定、効果音
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (0,0):
            self.life -= 1
            pyxel.play(1,0,loop = False)
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (4,0):
            self.life -= 1
            pyxel.play(1,0,loop = False)
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (2,2):
            self.life -= 1
            pyxel.play(1,0,loop = False)
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (1,22):
            self.life -= 1
            pyxel.play(1,0,loop = False)
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (2,22):
            self.life -= 1
            pyxel.play(1,0,loop = False)
        if pyxel.tilemap(1).pget(self.px + dx ,self.py + dy) == (3,22):
            self.life -= 1
            pyxel.play(1,0,loop = False)
        
    def draw(self,map):
        pyxel.blt((self.px - map.offset) * 8, self.py * 8 ,  0, 16+16 * ((pyxel.frame_count // 15) % 2), 32, 16, 16, 0)

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


class fire():
    def __init__(self):
        pass
    def update(self):
        pass
    def draw(self):
        pass

class App:
    def __init__(self):
        pyxel.init(200, 135)
        pyxel.load("my_resource.pyxres")
        self.scene = SCENE_PLAY
        self.score = 0
        self.map = Map()
        self.boy =Boy()
        pyxel.run(self.update, self.draw)


    def update(self):
    
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene()
        elif self.scene ==SCENE_GAMEOVER:
            self.update_gameover_scene()
        elif self.scene ==SCENE_GAMECLEAR:
            self.update_gameclear_scene()
    
    def update_title_scene(self):
        pass
    
    
    def update_play_scene(self):
        
        
       
        if pyxel.btnp(pyxel.KEY_UP):
           self.boy.move(self.map,0, -1)
        if pyxel.btnp(pyxel.KEY_DOWN):
           self.boy.move(self.map,0, 1)
        if pyxel.btnp(pyxel.KEY_RIGHT):
           self.boy.move(self.map,1, 0)
        if pyxel.btnp(pyxel.KEY_LEFT):
           self.boy.move(self.map,-1, 0)
        
        if self.boy.life == 0:
            self.scene=SCENE_GAMEOVER
        


    def update_gameover_scene(self):
        pyxel.cls(0)
        
        if pyxel.btnp(pyxel.KEY_RETURN):
            self.scene = SCENE_TITLE
            pyxel.playm(0,loop = True)
            pyxel.playm(1,loop = True)
    
    def update_gameclear_scene(self):
        pass

    def draw(self):
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()
        elif self.scene ==SCENE_GAMEOVER:
            self.draw_gameover_scene()
        elif self.scene ==SCENE_GAMECLEAR:
            self.draw_gameclear_scene()


    def draw_title_scene(self):
        pyxel.cls(0)
        pyxel.text(50, 50, "GAME START", 8)

    def draw_play_scene(self):
        
        pyxel.cls(0)
        pyxel.bltm(0,0,1,0,0,560,135)
        self.map.draw()
        self.boy.draw(self.map)
    

    def draw_gameover_scene(self):
        pyxel.cls(0)
        pyxel.blt(60,70 ,  0, 32+16 * ((pyxel.frame_count // 15) % 2),56 , 16, 16, 0)
        pyxel.text(50, 50, "GAME OVER", 8)
        pyxel.text(50, 80, "- PRESS R TO RESTART -", 6)


    def draw_gameclear_scene(self):
        
        pass
        pyxel.cls(0)
        pyxel.text(80, 83, "GAME CLEAR", 10)
        pyxel.text(69, 90, "CONGRATULATIONS!", 10)
        pyxel.text(71, 140, "- PRESS ENTER -", 6)



App()
