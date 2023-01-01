import pyxel

SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER1 = 2
SCENE_GAMEOVER2 = 3
SCENE_GAMEOVER3 = 4
SCENE_GAMECLEAR = 5


class Boy:
    def __init__(self):
        self.x = 100
        self.y = 100
    
    def update(self):
        pass
    
    def move(self):
    
        if pyxel.btn(pyxel.KEY_UP):
            self.y -= 3
        elif pyxel.btn(pyxel.KEY_DOWN):
            self.y += 3
        elif pyxel.btn(pyxel.KEY_RIGHT):
            self.x += 3
        elif pyxel.btn(pyxel.KEY_LEFT):
            self.x -= 3
    

    
    def draw(self):
        pyxel.blt(self.x, self.y,  0, 16+16 * ((pyxel.frame_count // 15) % 2), 32, 16, 16, 0)

class Enemy:
    def __init__(self):
        self.x = 80
        self.y = 143
        

    def update(self):
        pass
    
    def catch(self,boy):
        if self.x -8 < boy.x < self.x +8 and  self.y -8 < boy.y < self.y +8 :
            return True

    def draw(self):
        pyxel.blt(self.x, self.y,  0, 16 * ((pyxel.frame_count // 15) % 2),0, 16, 16, 0)
       
class Enemy2:
    
    def __init__(self):
        self.x = 80
        self.y = 60
    
    def update(self):
        pass
    
    def catch(self,boy):
        if self.x -8 < boy.x < self.x +8 and  self.y -8 < boy.y < self.y +8 :
            return True


    def draw(self):
        pyxel.blt(self.x, self.y,  0, 32+16 * ((pyxel.frame_count // 15) % 2),0, 16, 16, 0)

class Enemy3:
    
    def __init__(self):
        self.x = 90
        self.y = 80

    def update(self):
        pass
    
    def catch(self,boy):
        if self.x -4 < boy.x < self.x +4 and  self.y -4 < boy.y < self.y +4 :
            return True


    def draw(self):
        pyxel.blt(self.x, self.y,  0, 16+16 * ((pyxel.frame_count // 15) % 2),16 , 16, 16, 0)




class App:
    def __init__(self):
        pyxel.init(200, 200)
        pyxel.load("my_resource.pyxres")
        self.scene = SCENE_PLAY
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
        self.boy.move()
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
        pyxel.bltm(0,0,0,self.boy.x-100,self.boy.x-100, self.boy.x +100, self.boy.y+100)
        self.boy.draw()
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
