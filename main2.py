import pyxel

pyxel.init(128,128)
SCENE_TITLE = 0
SCENE_PLAY = 1
SCENE_GAMEOVER1 = 2
SCENE_GAMEOVER2 = 3
SCENE_GAMEOVER3 = 4
SCENE_GAMECLEAR = 5
STAGE_WIDTH = 128 * 4
STAGE_HEIGHT =128 * 5
LEFT_LINE = 40
RIGHT_LINE = pyxel.width -40 
UPPER_LINE = 40
BOTTOM_LINE =pyxel.height - 48 
x = 50
y = 50
scroll_x = 0
scroll_y = 0
pldir = 1


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

class Wall:


    def __init__(c):
        c  = 0

    def chkwall(cx,cy):
            
        if cx < 0 or STAGE_WIDTH -8 < cx:
            c = c + 1
        if STAGE_HEIGHT < cy:
            c = c + 1
        return c

class App:



    def __init__(self):
        pyxel.load("my_resource.pyxres")
        self.scene = SCENE_PLAY
        self.boy =Boy()
        self.enemy =Enemy()
        self.enemy2 =Enemy2()
        self.enemy3 =Enemy3()
        self.wall = Wall()
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
        self.wall()
        if x < scroll_x + LEFT_LINE:
            scroll_x = x - LEFT_LINE
            if scroll_x < 0:
                scroll_x = 0
        if scroll_x + RIGHT_LINE < x:
            scroll_x = x - RIGHT_LINE
        if STAGE_WIDTH - pyxel.width < scroll_x:
            scroll_x = STAGE_WIDTH - pyxel.width
        
        
        if y < scroll_y + UPPER_LINE:
            scroll_y = y -UPPER_LINE
            if scroll_y < 0:
                scroll_y = 0
        if scroll_y + BOTTOM_LINE < y:
            scroll_y = y - BOTTOM_LINE
            if STAGE_HEIGHT - pyxel.height < scroll_y:
                scroll_y = STAGE_HEIGHT - pyxel.height
        
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
        pyxel.camera(scroll_x,scroll_y)
        pyxel.bltm(0,0,0, scroll_x, scroll_y, pyxel.width, pyxel.height)
        
        pyxel.camera(scroll_x,scroll_y)
        pyxel.blt( x, y, 0,  0, 8, pldir*8, 8, 0)

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
