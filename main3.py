import pyxel

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER1 = 2
SCENE_GAMEOVER2 = 3
SCENE_GAMEOVER3 = 4
SCENE_GAMECLEAR = 5


class Boy:
    def __init__(self):
        self.px = 2
        self.py = 5

       

    
    def update(self):
        pass
    
    def move(self,map,dx,dy):
        if pyxel.tilemap(1).pget(self.px + dx, self.py + dy) == (10, 0):
            self.px += dx
            self.py += dy
            map.move(self.px)
        print( pyxel.tilemap(1).pget(self.px + dx, self.py + dy))

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

class Enemy:
    def __init__(self):
        self.px = 80
        self.py = 143
        

    def update(self):
        pass
    
    def catch(self,boy):
        if self.px -8 < boy.px < self.px +8 and  self.py -8 < boy.py < self.py +8 :
            return True

    def draw(self):
        pyxel.blt(self.px, self.py,  0, 16 * ((pyxel.frame_count // 15) % 2),0, 16, 16, 0)
       
class Enemy2:
    
    def __init__(self):
        self.px = 80
        self.py = 60
    
    def update(self):
        pass
    
    def catch(self,boy):
        if self.px -8 < boy.px < self.px +8 and  self.py -8 < boy.py < self.py +8 :
            return True


    def draw(self):
        pyxel.blt(self.px, self.py,  0, 32+16 * ((pyxel.frame_count // 15) % 2),0, 16, 16, 0)

class Enemy3:
    
    def __init__(self):
        self.px = 90
        self.py = 80

    def update(self):
        pass
    
    def catch(self,boy):
        if self.px -4 < boy.px < self.px +4 and  self.py -4 < boy.py < self.py +4 :
            return True


    def draw(self):
        pyxel.blt(self.px, self.py,  0, 16+16 * ((pyxel.frame_count // 15) % 2),16 , 16, 16, 0)




class App:
    def __init__(self):
        pyxel.init(200, 135)
        pyxel.load("my_resource.pyxres")
        self.scene = SCENE_PLAY
        self.map = Map()
        self.boy =Boy()
        self.enemy =Enemy()
        self.enemy2 =Enemy2()
        self.enemy3 =Enemy3()
        pyxel.run(self.update, self.draw)


    def update(self):
    
        if self.scene == SCENE_TITLE:
            self.update_title_scene()
        elif self.scene == SCENE_PLAY:
            self.update_play_scene()
        elif self.scene ==SCENE_GAMEOVER1:
            self.update_gameover1_scene()
        elif self.scene ==SCENE_GAMEOVER1:
            self.update_gameover2_scene()
        elif self.scene ==SCENE_GAMEOVER2:
            self.update_gameover3_scene()
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
        
        if self.enemy.catch(self.boy):
            self.scene=SCENE_GAMEOVER1
        if self.enemy2.catch(self.boy):
            self.scene=SCENE_GAMEOVER1
        if self.enemy3.catch(self.boy):
            self.scene=SCENE_GAMEOVER1
    
    def update_gameover1_scene(self):
        pyxel.cls(0)
    def update_gameover2_scene(self):
        pass
    def update_gameover3_scene(self):
        pass
    def update_gameclear_scene(self):
        pass

    def draw(self):
        if self.scene == SCENE_TITLE:
            self.draw_title_scene()
        elif self.scene == SCENE_PLAY:
            self.draw_play_scene()
        elif self.scene ==SCENE_GAMEOVER1:
            self.draw_gameover1_scene()
        elif self.scene ==SCENE_GAMEOVER1:
            self.draw_gameover2_scene()
        elif self.scene ==SCENE_GAMEOVER2:
            self.draw_gameover3_scene()
        elif self.scene ==SCENE_GAMECLEAR:
            self.draw_gameclear_scene()


    def draw_title_scene(self):
        pass
    def draw_play_scene(self):
        
        pyxel.cls(0)
        pyxel.bltm(0,0,1,0,0,560,135)
        self.map.draw()
        self.boy.draw(self.map)
        self.enemy.draw()
        self.enemy2.draw()
        self.enemy3.draw()
    
    def draw_gameover1_scene(self):
        pass
    def draw_gameover2_scene(self):
        pass
    def draw_gameover3_scene(self):
        pass
    def draw_gameclear_scene(self):
        pass


App()
