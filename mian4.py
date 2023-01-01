import pyxel

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER = 2
SCENE_GAMECLEAR = 3

CAMERA_W = 200
CAMERA_H = 135
MAP_W = 560
MAP_H = 135


class Boy:
    def __init__(self):
        self.px = 2
        self.py = 5
    
        # 死んでる１死んでない０
        self.is_dead = False
    
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

class Camera:

    def __init__(self,boy):
        self.boy = boy

        if self.boy.px <= CAMERA_W / 2:
            self.x = 0
        elif self.boy.px <= MAP_W - CAMERA_W/2:
            self.x = MAP_W - CAMERA_W/2
        else:
            self.x = self.boy.px

    def update(self):
        if self.boy.px <= CAMERA_W / 2:
            self.x = 0
        elif self.boy.px <= MAP_W - CAMERA_W/2:
            self.x = MAP_W - CAMERA_W/2
        else:
            self.x = self.boy.px

    
class Map:
    def __init__(self):
        self.offset = 0

    def move(self, px):
        if px - self.offset >= 14:
            self.offset += 1
        elif px - self.offset <= 1 and self.offset > 1:
            self.offset -= 1

    def draw(self):
        pyxel.bltm(0,0,1,self.offset * 8,0,MAP_W,MAP_H) 

class Enemy:
    def __init__(self):
        self.px = 10
        self.py = 2
        

    def update(self):
        pass
    
    def catch(self,boy):
        if self.px -8 < boy.px < self.px + 1 and  self.py -1 < boy.py < self.py + 1 :
            return True
        

    def draw(self):
        pyxel.blt(self.px, self.py,  0, 16 * ((pyxel.frame_count // 15) % 2),0, 16, 16, 0)
       
class Enemy2:
    
    def __init__(self):
        self.px = 8
        self.py = 6
    
    def update(self):
        pass
    
    def catch(self,boy):
        if self.px -1 < boy.px < self.px + 1 and  self.py -1 < boy.py < self.py + 1 :
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
        if self.px -1 < boy.px < self.px +1 and  self.py -1 < boy.py < self.py + 1 :
            return True


    def draw(self):
        pyxel.blt(self.px, self.py,  0, 16+16 * ((pyxel.frame_count // 15) % 2),16 , 16, 16, 0)




class App:
    def __init__(self):
        pyxel.init(CAMERA_W, CAMERA_H)
        pyxel.load("my_resource.pyxres")
        self.scene = SCENE_PLAY
        self.map = Map()
        self.boy =Boy()
        self.enemy =Enemy()
        self.enemy2 =Enemy2()
        self.enemy3 =Enemy3()
        self.camera =Camera(self.boy)
        pyxel.run(self.update, self.draw)


    def update(self):
    
        if self.boy.is_dead: 
            self.scene = SCENE_GAMEOVER
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
        
        if self.enemy.catch(self.boy):
            self.scene=SCENE_GAMEOVER
        if self.enemy2.catch(self.boy):
            self.scene=SCENE_GAMEOVER
        if self.enemy3.catch(self.boy):
            self.scene=SCENE_GAMEOVER
    
    def update_gameover_scene(self):
        pyxel.cls(0)
   
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
        pass
    def draw_play_scene(self):
        
        pyxel.cls(0)
        pyxel.bltm(0,0,1,0,0,MAP_W,MAP_H)
        self.map.draw()
        self.boy.draw(self.map)
        self.enemy.draw()
        self.enemy2.draw()
        self.enemy3.draw()
    
    def draw_gameover_scene(self):
        pass
   
    def draw_gameclear_scene(self):
        pass


App()
