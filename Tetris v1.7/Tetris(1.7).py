import math
import os
import pygame
from random import randint
hg=1080
wd=int(hg/9 *16)
bw=hg//18
comp=0
esc=4
w = pygame.display.set_mode((wd, hg))
BGCOLOR = (20, 30, 40)
esc=4
clock = pygame.time.Clock()
def Legal_Screen():
    pygame.init()
    seconds=2.5
    time=seconds*60
    tick=0
    pygame.draw.rect(w, (0, 0, 0), (0, 0, wd, hg))
    while tick<time+30:
        clock.tick(60)
        bls = (hg // 2) // time
        tick+=1
        image = pygame.image.load(os.path.join("Assets", "Data", "tetris.png"))
        w.blit(pygame.transform.scale(image, (wd // 3, hg * 0.3946045062)), ((wd - wd // 3) // 2 + bw // 4, hg // 5))
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "vgasys.fon"), int(hg / 25))
        text = font.render(("TM AND © 1987"), True, (255, 255, 255))
        trex = text.get_rect()
        trex.center = (wd // 2, hg // 2 - bw + bw + bw + bw + bw)
        w.blit(text, trex)
        text = font.render(("V/O ELECTRONORGTECHNICA (\"ELORG\")"), True, (255, 255, 255))
        trex = text.get_rect()
        trex.center = (wd // 2, hg // 2 - bw // 2 + bw + bw + bw + bw)
        w.blit(text, trex)
        text = font.render(("UNLICENSED"), True, (255, 255, 255))
        trex = text.get_rect()
        trex.center = (wd // 2, hg // 2 + bw + bw + bw + bw)
        w.blit(text, trex)
        text = font.render(("ORIGINAL CONCEPT,DESIGN AND PROGRAM"), True, (255, 255, 255))
        trex = text.get_rect()
        trex.center = (wd // 2, hg // 2 + bw // 2 + bw + bw + bw + bw)
        w.blit(text, trex)
        text = font.render(("BY ALEXEY PAZHITNAO"), True, (255, 255, 255))
        trex = text.get_rect()
        trex.center = (wd // 2, hg // 2 + bw + bw + bw + bw + bw)
        w.blit(text, trex)
        pygame.draw.rect(w, (0, 0, 0), (0,-hg//2+bls*tick+7*bw//4, wd, hg//2))
        pygame.draw.rect(w, (0, 0, 0), (0, hg - bls * tick, wd, hg // 2))
        pygame.display.update()
def Main_Menu():
    pygame.init()
    es=0
    newp=0
    base_font = pygame.font.Font(os.path.join("Assets" , "Fonts", "MAGNETOB.ttf"), int(hg//24))
    Name_Editor = ''
    color_passive = (0,0,84)
    color = color_passive
    active = False
    doc=open(os.path.join("Assets","Data","Variables.txt"),"r")
    L = doc.readlines()
    Name= (L[0]).rstrip()
    Name_Editor=Name
    FPS_Settings= int((L[1]).rstrip())
    Music_Settings = int((L[2]).rstrip())
    SFX_Settings = int((L[3]).rstrip())
    High_Score = int((L[4]).rstrip())
    Neww=int((L[5]).rstrip())
    doc.close()
    if Neww==0:
        newp=1
    
    settings_color= (150, 150, 200)
    clock = pygame.time.Clock()
    if esc==3:
        load = 55
        xo = 0
        image = pygame.image.load(os.path.join("Assets", "Data", "LOAD.png"))
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        while load < 61:
            load += 1
            clock.tick(60)
            w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
            if xo > bw // 8:
                xo = 6 * bw - int(load / 5 * (6 * bw // 12))
            pygame.draw.rect(w, (255, 255, 255),
                             (wd // 2 - 3 * bw - bw // 8, 2 * hg // 5 - bw // 8, 6 * bw + bw // 4, bw + bw // 4), 2,
                             bw // 8)
            pygame.draw.rect(w, (255, 255, 255), (wd // 2 - 3 * bw, 2 * hg // 5, 6 * bw - xo, bw))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(hg / 25))
            if load % 9 <= 2:
                text = font.render(("LOADING."), True, (255, 255, 255))
            elif load % 9 <= 5:
                text = font.render(("LOADING.."), True, (255, 255, 255))
            else:
                text = font.render(("LOADING..."), True, (255, 255, 255))
            trex = text.get_rect()
            trex.midleft = (wd // 2 - 2 * bw + bw // 2, 2 * hg // 5 + bw + hg // 20)
            w.blit(text, trex)
            pygame.display.update()

    run=True
    pygame.init()
    disp = ""
    clc=1
    cl=0
    conts=0
    Block_1_Height=hg//2
    Block_2_Y_Loc= hg // 2
    Block_Width = wd
    r=120
    g=50
    b=200
    rp=1
    bp=1
    xc= -hg
    gp=1
    xdiff=0
    ydiff=0
    Click=0
    d_x=int(wd*1.015625)
    d_color=(0,0,82)
    dx2= wd - 7 // 4 * bw  +0.125*wd
    dx3= wd*1.2
    pau=0
    pygame.init()
    ml=1
    Trigger=0
    BGM_Main_Screen = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "M-m.wav"))
    if Music_Settings!=0:
        BGM_Main_Screen.play(loops=-1)
    Text_1_Color=(r,g, b)
    while(run):
        if conts==1:
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            newp = 0
            L[5] = "1\n"
            doc.writelines(L)
            doc.close()
        if conts==0 and xc>-hg:
            xc-=hg/5
        elif conts==1 and xc!=0:
            xc+= hg/5
        if Trigger==1:
            pygame.init()
            BGM_Main_Screen = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "M-m.wav"))
            BGM_Main_Screen.play(loops=-1)
            Trigger=0
        elif Trigger==2:
            BGM_Main_Screen.stop()
            Trigger=0
        settings_color = (150, 150, 200)
        Mouse_Loc = pygame.mouse.get_pos()
        clock.tick(60)
        cl+=1
        if(cl%4==0):
            clc+=1
        if clc < 126:
            disp = "mv (" + str(clc) + ").jpg"
        else:
            clc = 1
        if Block_1_Height >0:
            Block_1_Height-=20
        if Block_2_Y_Loc <hg:
            Block_2_Y_Loc+=20
        if r==250:
            rp=0
        elif r==0:
            rp=1
        if g==100:
            gp=0
        elif g==0:
            gp=1
        if b == 200:
            bp = 0
        elif b == 100:
            bp = 1
        if rp==1:
            r+=10
        elif rp==0:
            r-=10
        if bp==1:
            b+=10
        elif bp==0:
            b-=10
        if gp==100:
            g+=10
        elif gp==0:
            g-=10
        if xdiff<=0:
            ydiff=0
        if xdiff>=25:
            ydiff=1
        if ydiff==0:
           xdiff+=5
        elif ydiff==1:
           xdiff-=5
        Text_1_Color = (r, g, b)
        image = pygame.image.load(os.path.join("Assets", "Main Menu", disp))
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "STENCIL.ttf"), int(hg / 7.2))
        text = font.render('TETRIS', True, (50,50,105))
        trex = text.get_rect()
        trex.center = (6*wd //21, hg / 3 )
        w.blit(text, trex)
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "STENCIL.ttf"), int(hg /15))
        text = font.render("High Score:", True, (50, 50, 105))
        trex = text.get_rect()
        trex.center = (18 * wd / 21, 3* hg /9)
        w.blit(text, trex)
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "STENCIL.ttf"), int(hg /14))
        text = font.render(str(High_Score), True, Text_1_Color)
        trex = text.get_rect()
        trex.center = (19 * wd / 21, 4 *hg/9)
        w.blit(text, trex)
        font = pygame.font.Font(os.path.join("Assets" , "Fonts", "STENCIL.ttf"),int( hg/24))
        text = font.render('    Press Space To Start    ', True, (20,20,105))
        trex = text.get_rect()
        trex.center = (6*wd /21, 37*hg /50)
        w.blit(text, trex)
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "MAGNETOB.ttf"), int(hg / 24))
        text = font.render(Name, True, (150,150,200))
        trex = text.get_rect()
        trex.midright = ((wd-  8/4 *bw, 21/16 *bw))
        w.blit(text, trex)
        if ml==1 and Mouse_Loc[0]<wd//2:
            Click=0
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "STENCIL.ttf"), int(hg / 24))
        if ml==1 and Mouse_Loc[0] >=(wd-  7/4 *bw) and Mouse_Loc[0]<=wd-  3/4 *bw and Mouse_Loc[1] >=3/4 *bw and Mouse_Loc[1]<=7/4 *bw and pau==15:
            pau = 0
            if Click == 0:
                Click = 1
            else:
                Click = 0
        image = pygame.image.load(os.path.join("Assets", "Main Menu", "Settings.png"))        
        w.blit(pygame.transform.scale(image,(int(bw), int(bw))), (int(wd-  7/4 *bw), int(3/4 *bw)))        
        pygame.draw.rect( w, d_color, (d_x, 0, int( wd/2),hg))
        image = pygame.image.load(os.path.join("Assets", "Main Menu", "Back.png"))
        w.blit(pygame.transform.scale(image, (int(bw), int(bw))), (dx2-bw//2, 2/4 * bw))
        image = pygame.image.load(os.path.join("Assets", "Main Menu", "gpad2.png"))
        w.blit(pygame.transform.scale(image, (int(bw), int(bw))), (int(wd//10 - 11 / 4 * bw), int(1 / 4 * bw)))
        if newp==1:
            pygame.draw.rect(w, Text_1_Color, (int(wd//10 - 11/ 4 * bw-bw//15),int(1 / 4 * bw), int(bw*1.15), int(bw*1.15)),5,bw//8)
        text = font.render("FPS:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = ((dx3, 2 / 5 * hg))
        w.blit(text, trex)
        text = font.render("PLayer Name:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = ((dx3, 1/7 * hg))
        w.blit(text, trex)
        input_rect = pygame.Rect(dx3 -0.005*wd, 1/7 * hg + int(hg / 24) , 0.777*hg,int(hg/20) )
        pygame.draw.rect(w, d_color, (dx3 +0.095*wd, 3/5*hg- int(hg/40), 1.6*bw, int(hg/24))) #off
        if ml==1 and Mouse_Loc[0] >=dx3 +0.095*wd and Mouse_Loc[0]<=dx3 +0.095*wd +1.6*bw and Mouse_Loc[1] >=3/5*hg- int(hg/40) and Mouse_Loc[1]<=3/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            Trigger=2
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings=0
            L[2]="0\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.178 * wd, 3 / 5 * hg - int(hg / 40), 4 * bw, int(hg / 24)))
        if ml==1 and Mouse_Loc[0] >=dx3 +0.178*wd and Mouse_Loc[0]<=dx3 +0.178*wd +4*bw and Mouse_Loc[1] >=3/5*hg- int(hg/40) and Mouse_Loc[1]<=3/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            if Music_Settings==0:
                Trigger=1
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings=1
            L[2]="1\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.3175 * wd, 3 / 5 * hg - int(hg / 40), 2.8 * bw, int(hg / 24))) 
        if ml==1 and Mouse_Loc[0] >=dx3 +0.3175*wd and Mouse_Loc[0]<=dx3 +0.3175*wd +2.8*bw and Mouse_Loc[1] >=3/5*hg- int(hg/40) and Mouse_Loc[1]<=3/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            if Music_Settings==0:
                Trigger=1
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings=2
            L[2]="2\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.174 * wd, 3.4 / 5 * hg - int(hg / 40), 4.3 * bw, int(hg / 24))) 
        if ml==1 and Mouse_Loc[0] >=dx3 +0.174*wd and Mouse_Loc[0]<=dx3 +0.174*wd +4.3*bw and Mouse_Loc[1] >=3.4/5*hg- int(hg/40) and Mouse_Loc[1]<=3.4/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            if Music_Settings==0:
                Trigger=1
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings=3
            L[2]="3\n"
            doc.writelines(L)
            doc.close()
        text = font.render("Music:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = ((dx3, 3/5 * hg))
        w.blit(text, trex)
        if Music_Settings==0:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("OFF", True, settings_color)
        trex = text.get_rect()
        trex.center = ((dx3 + 0.12 * wd, 3 / 5 * hg))
        w.blit(text, trex)
        if Music_Settings==1:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("Mordern", True, settings_color)
        trex = text.get_rect()
        trex.center = ((dx3 + 0.24 * wd, 3 / 5 * hg))
        w.blit(text, trex)
        if Music_Settings==2:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("Retro", True, settings_color)
        trex = text.get_rect()
        trex.center = ((dx3 + 0.36 * wd, 3 / 5 * hg))
        w.blit(text, trex)
        if Music_Settings==3:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("Randomize", True, settings_color)
        trex = text.get_rect()
        trex.center = ((dx3 + 0.24 * wd, 3.4 / 5 * hg))
        w.blit(text, trex)
        text = font.render("SFX:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = ((dx3, 4.2 / 5 * hg))
        w.blit(text, trex)
        pygame.draw.rect(w, d_color, (dx3 + 0.155 * wd, 4.2 / 5 * hg - int(hg / 40), 1.6 * bw, int(hg / 24)))
        if ml==1 and Mouse_Loc[0] >=dx3 +0.155*wd and Mouse_Loc[0]<=dx3 +0.155*wd +1.6*bw and Mouse_Loc[1] >=4.2/5*hg- int(hg/40) and Mouse_Loc[1]<=4.2/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            SFX_Settings=1
            L[3]="1\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.285 * wd, 4.2 / 5 * hg - int(hg / 40), 1.6 * bw, int(hg / 24)))
        if ml==1 and Mouse_Loc[0] >= dx3 + 0.285 * wd and Mouse_Loc[0] <= dx3 + 0.285 * wd + 1.6 * bw and Mouse_Loc[1] >= 4.2 / 5 * hg - int(hg / 40) and Mouse_Loc[1] <= 4.2 / 5 * hg - int(hg / 40 - hg / 24) and pau == 15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            SFX_Settings = 0
            L[3] = "0\n"
            doc.writelines(L)
            doc.close()
        if SFX_Settings==1:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("ON", True, settings_color)
        trex = text.get_rect()
        trex.center = ((dx3 + 0.18 * wd, 4.2 / 5 * hg))
        w.blit(text, trex)
        if SFX_Settings == 0:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("OFF", True, settings_color)
        trex = text.get_rect()
        trex.center = ((dx3 + 0.31 * wd, 4.2 / 5 * hg))
        w.blit(text, trex)
        if FPS_Settings == 0:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        pygame.draw.rect(w, d_color, (dx3 + 0.095 * wd, 2 / 5 * hg - int(hg / 40), 1.6 * bw, int(hg / 24))) 
        if ml==1 and Mouse_Loc[0] >=dx3 +0.095*wd and Mouse_Loc[0]<=dx3 +0.095*wd +1.6*bw and Mouse_Loc[1] >=2/5*hg- int(hg/40) and Mouse_Loc[1]<=2/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            FPS_Settings=0
            L[1]="0\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.215 * wd, 2 / 5 * hg - int(hg / 40), 1.6 * bw, int(hg / 24))) 
        if ml==1 and Mouse_Loc[0] >=dx3 +0.215*wd and Mouse_Loc[0]<=dx3 +0.215*wd +1.6*bw and Mouse_Loc[1] >=2/5*hg- int(hg/40) and Mouse_Loc[1]<=2/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            FPS_Settings=1
            L[1]="1\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.335 * wd, 2 / 5 * hg - int(hg / 40), 1.6 * bw, int(hg / 24))) 
        if ml==1 and Mouse_Loc[0] >=dx3 +0.335*wd and Mouse_Loc[0]<=dx3 +0.335*wd +1.6*bw and Mouse_Loc[1] >=2/5*hg- int(hg/40) and Mouse_Loc[1]<=2/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            FPS_Settings=2
            L[1]="2\n"
            doc.writelines(L)
            doc.close()
        text = font.render("30", True, settings_color)
        trex = text.get_rect()
        trex.center = ((dx3 + 0.12*wd, 2 / 5 * hg))
        w.blit(text, trex)
        if FPS_Settings == 1:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("60", True, settings_color)
        trex = text.get_rect()
        trex.center = ((dx3 + 0.24 * wd, 2 / 5 * hg))
        w.blit(text, trex)
        if FPS_Settings == 2:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("120", True, settings_color)
        trex = text.get_rect()
        trex.center = ((dx3 + 0.36 * wd, 2 / 5 * hg))
        w.blit(text, trex)
        if Name != Name_Editor:
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            L[0] = Name_Editor + "\n"
            Name= Name_Editor
            doc.writelines(L)
            doc.close()
        if active and pau%5==0:
            color = (50,50,100)
        elif pau==15:
            color = color_passive
        elif active==True:
            color= (255,0,0)
        pygame.draw.rect(w, color, input_rect)
        text_surface = base_font.render(Name_Editor, True, (200, 100, 100))
        w.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, int(hg/20))
        d_color=d_color
        if conts==1or conts==0:
            pygame.draw.rect(w, d_color, (0+wd // 2 - 2 * wd // 5, xc+hg // 2 - 5.5 * hg // 14, 4 * wd // 5, 9.5 * hg // 14))
            pygame.draw.rect(w, (235, 80, 78), (0+wd // 2 - 3 * bw+bw//2, xc+hg * 2 / 3 - bw // 2, 5 * bw, bw-bw//8))
            pygame.draw.rect(w, (235, 80, 78), (0+wd // 2 - 3 * bw, xc+hg * 2 / 3 - bw // 2, 6 * bw, bw), bw // 2,int(bw / 8))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 2, xc+hg / 3, bw, bw), bw // 2, int(bw / 8))
            pygame.draw.rect(w, (235, 80, 78),(0+2.5 * wd // 8 - bw // 2 - bw - bw // 20, xc+hg / 3 + bw + bw // 20, bw, bw), bw // 2, int(bw / 8))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 2, xc+hg / 3 + bw + bw // 20, bw, bw), bw // 2,int(bw / 8))
            pygame.draw.rect(w, (235, 80, 78),(0+2.5 * wd // 8 - bw // 2 + bw + bw // 20, xc+hg / 3 + bw + bw // 20, bw, bw), bw // 2,int(bw / 8))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 2 - 4 * bw, xc+hg // 6, bw, bw), bw // 2,int(bw / 8))
            pygame.draw.rect(w, (235, 80, 78), (0 + 11 * wd // 16 - 3*bw // 2, xc + hg / 3, bw, bw), bw // 2, int(bw / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "Everson Mono Bold.ttf"), int(hg / 10))
            text = font.render(("⎵"), True, (d_color))
            trex = text.get_rect()
            trex.center = (0+wd // 2, xc+hg * 2 / 3 - bw // 8)
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(hg / 32))
            text = font.render(("ESC"), True, (d_color))
            trex = text.get_rect()
            trex.center = (0+2.5 * wd // 8 - 4 * bw, xc+hg // 6 + bw // 2)
            w.blit(text, trex)

            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 + bw // 2 - 4 * bw, xc+hg // 6 + bw // 2 - bw // 40, wd // 3 - 2 * bw, bw // 20))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 40, xc+hg // 6 + 3 * bw // 2, bw // 20, 2 * bw))
            pygame.draw.rect(w, (235, 80, 78),(0+2.5 * wd // 8 - bw // 40, xc+hg // 6 + 3 * bw // 2, wd // 3 - 7 * bw + bw // 4, bw // 20))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 2 + bw + bw // 20 + bw // 2 - bw // 40, xc+hg // 6 + 5 * bw // 2, bw // 20, 4 * bw // 2))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 40 + bw + bw // 20, xc+hg // 6 + 5 * bw // 2, wd // 3 - 7 * bw + bw // 6 - bw, bw // 20))
            pygame.draw.rect(w, (235, 80, 78),(0+2.5 * wd // 8 - bw // 40, xc+hg / 3 + bw + bw + bw // 20, bw // 20, bw // 2))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 40, xc+hg / 3 + bw + 3 * bw // 2 + bw // 20, (wd // 3 - 7 * bw + bw // 4) // 2,bw // 20))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 40 + (wd // 3 - 7 * bw + bw // 4) // 2, xc+hg // 6 + 7 * bw // 2, bw // 20,4 * bw // 2 + bw // 10))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 40 + (wd // 3 - 7 * bw + bw // 4) // 2, xc+hg // 6 + 7 * bw // 2,(wd // 3 - 7 * bw + bw // 4) // 2, bw // 20))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 40 + (wd // 3 - 7 * bw + bw // 4) // 2 + bw, xc+hg / 3 + bw // 2 + bw + bw // 20,(wd // 3 - 9 * bw + bw // 4) // 2, bw // 20))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw // 40 + (wd // 3 - 7 * bw + bw // 4) // 2 + bw, xc+hg / 3 + bw // 2 + bw + bw // 20,bw // 20, 4 * bw // 2 + bw // 10))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw - bw // 20 - bw // 40, xc+hg / 3 + 2 * bw // 2 + bw + bw // 20, bw // 20,3 * bw // 2 + bw // 10))
            pygame.draw.rect(w, (235, 80, 78), (0+2.5 * wd // 8 - bw - bw // 20 - bw // 40, xc+hg / 3 + 2 * bw // 2 + bw + bw // 20 + 3 * bw // 2 + bw // 20,(2.5 * wd // 8 - bw // 40 + (wd // 3 - 7 * bw + bw // 4) // 2 + bw) - (2.5 * wd // 8 - bw - bw // 20) + bw // 15, bw // 20))
            pygame.draw.rect(w, (235, 80, 78), (0+wd // 2 + 2 * bw, xc+hg // 6 + 11 * bw // 2,  bw//22+(8.5* wd // 16 + bw + 3 * bw) - (wd // 2 + 2 * bw), bw // 20))
            pygame.draw.rect(w, (235, 80, 78), (0+4 * wd // 8 + bw + 4 * bw - bw // 40, xc-2*bw +hg // 6 + 11 * bw // 2, bw // 20,(0+hg * 2 / 3 - bw // 2) - (hg // 6 + 11 * bw // 2)-bw))
            pygame.draw.rect(w, (235, 80, 78), (0+wd // 2 - bw // 40, xc+hg // 6 + 14 * bw // 2, bw // 20,(hg * 2 / 3 ) - (hg // 6 + 15* bw // 2)))

            text = font.render(("QUIT"), True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (0+wd // 2, xc+hg // 6 + bw // 2)
            w.blit(text, trex)

            text = font.render(("INSTANT DOWN"), True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (0+wd // 2, xc+hg // 6 + 3 * bw // 2)
            w.blit(text, trex)

            text = font.render(("MOVE RIGHT"), True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (0+wd // 2, xc+hg // 6 + 5 * bw // 2)
            w.blit(text, trex)

            text = font.render(("MOVE DOWN"), True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (0+wd // 2, xc+hg // 6 + 7 * bw // 2)
            w.blit(text, trex)

            text = font.render(("MOVE LEFT"), True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (0+wd // 2, xc+hg // 6 + 9 * bw // 2)
            w.blit(text, trex)

            text = font.render(("PAUSE/RESUME"), True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (0+wd // 2, xc+hg // 6 + 11 * bw // 2)
            w.blit(text, trex)

            text = font.render(("ROTATE"), True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (0+wd // 2, xc+hg // 6 + 13 * bw // 2)
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(hg / 25))
            text = font.render(("W"), True, (d_color))
            trex = text.get_rect()
            trex.center = (0+2.5 * wd // 8, xc+hg / 3 + bw // 2)
            w.blit(text, trex)

            text = font.render(("A"), True, (d_color))
            trex = text.get_rect()
            trex.center = (0+2.5 * wd // 8 - bw - bw // 20, xc+hg / 3 + bw // 2 + bw + bw // 20)
            w.blit(text, trex)

            text = font.render(("S"), True, (d_color))
            trex = text.get_rect()
            trex.center = (0+2.5 * wd // 8, xc+hg / 3 + bw // 2 + bw + bw // 20)
            w.blit(text, trex)

            text = font.render(("D"), True, (d_color))
            trex = text.get_rect()
            trex.center = (0+2.5 * wd // 8 + bw + bw // 20, xc+hg / 3 + bw // 2 + bw + bw // 20)
            w.blit(text, trex)

            text = font.render(("P"), True, (d_color))
            trex = text.get_rect()
            trex.center = (0 + 11 * wd // 16 - bw, xc + hg / 3 + bw // 2)
            w.blit(text, trex)

        if esc==4:
            pygame.draw.rect(w, (0, 0, 0), (0, 0, Block_Width, Block_1_Height))
            pygame.draw.rect(w, (0, 0, 0), (0, Block_2_Y_Loc, Block_Width, Block_1_Height))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "MAGNETOB.ttf"), int(hg / 25))
            text = font.render(("By: Jatan Bhatt"), True, Text_1_Color)
            trex = text.get_rect()
            trex.center = (18.7 * wd / 21, Block_2_Y_Loc + int(hg / 25))
            w.blit(text, trex)
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "STENCIL.ttf"), int(hg / 25))
            text = font.render(("ver 2.0"), True, (settings_color))
            trex = text.get_rect()
            trex.center = (1 * wd / 21, Block_1_Height - int(hg / 25))
            w.blit(text, trex)
        if Click==0:
            if(d_x < int(wd + 20)):
                d_x+=150
                dx2+=40
                dx3+=200
        if Click == 1:
            if (d_x > 103*wd/180 ):
                d_x -=150
                dx2-=40
                dx3-=200
        if pau!=15:
            pau+=1
        pygame.display.update()
        if ml==1:
            ml=0
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                run = False
                es=1
            if event.type == pygame.MOUSEBUTTONUP:
                if Mouse_Loc[0] >= dx3 + wd*0.1 and Mouse_Loc[1]<=1/7 * hg + int(hg / 24 + hg/20) and Mouse_Loc[1]>=1/7 * hg + int(hg / 24):
                    active = True
                else:
                    active = False
            if event.type == pygame.MOUSEBUTTONUP:
                if 1==1:
                    ml=1
                if wd//10 - 11 / 4 * bw < Mouse_Loc[0] < wd//10 - 11 / 4 * bw+ bw and 1 / 4 * bw <Mouse_Loc[1] < 5 / 4 * bw:
                    conts=1
                elif   Mouse_Loc[0] >0 and Mouse_Loc[0] <wd/2 and Mouse_Loc[1]<hg and Mouse_Loc[1] >hg//4 and active==False and Click==0 and conts==0:
                    run=False
                elif comp==0 and Mouse_Loc[0] >0 and Mouse_Loc[0] <hg//7 and Mouse_Loc[1]<hg and Mouse_Loc[1] <hg//4 and active==False and Click==0 and conts==0:
                    run=False
                    es=1
                else:
                    conts=0
            if keypress[pygame.K_SPACE] and active==False:
                run = False
            if event.type == pygame.KEYDOWN and active ==True:
                if event.key == pygame.K_BACKSPACE:   
                    Name_Editor = Name_Editor[:-1]             
                elif (event.key !=pygame.K_ESCAPE):
                    if (len(Name_Editor))<=24:
                        Name_Editor += event.unicode
                    else:
                        pau=0
    BGM_Main_Screen.stop()
    load=0
    xo=6*bw
    image = pygame.image.load(os.path.join("Assets", "Data", "LOAD.png"))
    w.blit(pygame.transform.scale(image, (wd, hg)), (0,0))
    if es==1:
        load = 0
        xo = 6 * bw
        image = pygame.image.load(os.path.join("Assets", "Data", "LOAD2.png"))
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        while load < 61:
            load += 1
            clock.tick(60)
            w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
            if xo >=0:
                xo = 6 * bw - int(load / 5 * (6 * bw // 12))-5
            pygame.draw.rect(w, (255, 255, 255),
                             (wd // 2 - 3 * bw - bw // 8, 2 * hg // 5 - bw // 8, 6 * bw + bw // 4, bw + bw // 4), 2,
                             bw // 8)
            pygame.draw.rect(w, (255, 255, 255), (wd // 2 - 3 * bw, 2 * hg // 5, 6 * bw - xo, bw))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(hg / 25))
            if load  <= 20:
                text = font.render(("ENDING BACKGROUD PROCESSES"), True, (255, 255, 255))
            elif load  <= 40:
                text = font.render(("CLOSING GAME ENGINE"), True, (255, 255, 255))
            else:
                text = font.render(("THANK YOU FOR PLAYING"), True, (255, 255, 255))
            trex = text.get_rect()
            trex.center = (wd // 2, 2 * hg // 5 + bw + hg // 20)
            w.blit(text, trex)
            pygame.display.update()
    while load<61 and es!=1:
        load+=1
        clock.tick(60)
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        if xo>bw//8:
            xo = 6 * bw - int(load / 5 * (6 * bw // 12))
        pygame.draw.rect(w, (255, 255, 255), (wd//2-3*bw-bw//8, 2*hg//5-bw//8,6*bw+bw//4, bw+bw//4),2,bw//8)
        pygame.draw.rect(w, (255, 255, 255), (wd // 2 - 3 * bw , 2 * hg // 5, 6 * bw -xo, bw ))
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(hg / 25))
        if load%9<=2:
            text = font.render(("LOADING."), True, (255, 255, 255))
        elif load%9<=5:
            text = font.render(("LOADING.."), True, (255, 255, 255))
        else:
            text = font.render(("LOADING..."), True, (255, 255, 255))
        trex = text.get_rect()
        trex.midleft = (wd//2-2*bw+bw//2,2 * hg // 5 +bw+hg//20)
        w.blit(text, trex)
        pygame.display.update()


    return(es)
#Convert To X-Axis Co-ordinates
def convx(n):
    x = int((n - (n % 100)) / 100)
    return (x)
#Convert To Y-Axis Co-ordinates
def convy(n):
    x = n % 100
    return (x)
def main():
    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "r")
    L = doc.readlines()
    FPS_Settings = int((L[1]).rstrip())
    Music_Settings = int((L[2]).rstrip())
    SFX_Settings = int((L[3]).rstrip())
    High_Score = int((L[4]).rstrip())
    doc.close()
    run = True
    INTEp=1
    pygame.init()
    clock = pygame.time.Clock()

    if FPS_Settings==0:
        FPS=30
    elif FPS_Settings==2:
        FPS=120
    else:
        FPS=60
    #Frequency
    Rotation_Frequency = FPS
    Left_Movement_Clock_Frequency  = FPS
    Right_Movement_Clock_Frequency = FPS
    Down_Movement_Clock_Frequency  = FPS
    IMD_Movement_Clock_Frequency   = FPS*2
    #Default Clock Values
    Rotation_Clock       = Rotation_Frequency
    IMD_Movement_Clock   = IMD_Movement_Clock_Frequency
    Down_Movement_Clock = Down_Movement_Clock_Frequency
    Left_Movement_Clock  = Left_Movement_Clock_Frequency
    Right_Movement_Clock = Right_Movement_Clock_Frequency
    # Defauult Variable Values
    es=0
    play = 0
    Score = 0
    TA=0
    TD=0
    TS=0
    TW=0
    TP=0
    TR=0
    i = 0
    endmusicclock = 0
    visi = 0
    ng = 0
    Score=0
    modder=0
    clc=1
    Block_Grid_Color=(0,0,0)
    disp=""
    ticker=0
    Rotaion_Status = 0
    Rotation_Shape = 0
    Vert_Movement_Clock = 0
    Stop_Current_Shape_Movement = 0
    Spawn_New_Block = 1
    Rotation_Mananger_Boolean = 1
    Block_X_No=10
    Block_Y_No=17
    #Set Grids/Arrays
    Current_Shape = [0] * 4
    Next_Shape = [0] * 4
    Block_Grid_X = [0] * Block_X_No
    Block_Grid_Y = [0] * Block_Y_No
    Block_Grid_Color_Boolean = [0] * (Block_X_No*(Block_Y_No+4))
    Current_Shape_Display_Grid = [0] * (Block_X_No * Block_Y_No)
    Next_Shape_Display_Grid = [0] * 12
    #Colors
    Current_Shape_Color = (0, 0, 0)
    Block_Grid_Free_Color = (150, 150, 150)
    Block_Grid_Red = (170, 30, 40)
    Next_Shape_Color = (randint(0, 255), randint(0, 255), randint(0, 255))
    #Shape Randomizer and Color Picker
    Current_Shape_Randomizer = randint(1, 7)
    Next_Shape_Randomizer = randint(1, 7)
    if Next_Shape_Randomizer==1:
        Next_Shape_Color= (26, 194, 241)
    elif Next_Shape_Randomizer==2:
        Next_Shape_Color= (253, 223, 102)
    elif Next_Shape_Randomizer==3:
        Next_Shape_Color= (151, 59, 152)
    elif Next_Shape_Randomizer==4:
        Next_Shape_Color= (0, 131, 196)
    elif Next_Shape_Randomizer==5:
        Next_Shape_Color= (247, 160, 67)
    elif Next_Shape_Randomizer==6:
        Next_Shape_Color= (148, 202, 100)
    elif Next_Shape_Randomizer==7:
        Next_Shape_Color= (238, 69, 51)
   #Decide BGM
    if Music_Settings==3:
        if randint(0, 1) == 0:
            BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm.ogg"))
        else:
            BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm2.ogg"))
    elif Music_Settings==1:
        BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm2.ogg"))
    elif Music_Settings==2:
        BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm.ogg"))
    if Music_Settings!=0:
        BGM_Game_Playing2 = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "INTE.ogg"))
        BGM_Game_Playing2.play(loops=-1)
        BGM_Game_Playing2.set_volume(0)
    #Set Arrays
    i=0
    while(i<Block_X_No):
        Block_Grid_X[i]= int (wd/2-(Block_X_No/2)*bw +i*bw)
        i+=1
    i=0
    while(i<Block_Y_No):
        Block_Grid_Y[i]= int(hg/2 - bw/2 - (Block_Y_No//2 -i)*bw)
        i+=1
    xxx = 0
    yyy = 0
    ng = 0
    while (yyy < Block_Y_No):
        xxx = 0
        yyy += 1
        while (xxx < Block_X_No):
            Current_Shape_Display_Grid[(ng)] = (xxx * 100) + yyy - 1
            xxx += 1
            ng += 1
    xxx = 0
    yyy = 0
    ng3 = 0
    while (yyy < 3):
        xxx = 0
        yyy += 1
        while (xxx < 4):
            Next_Shape_Display_Grid[(ng3)] = (((15+Block_X_No+ xxx) * bw) * 10000) + 100 + ((yyy - 1) * bw)
            ng3 += 1
            xxx += 1
    if Music_Settings != 0:
        BGM_Game_Playing.play(loops=-1)
    load = 55
    xo = 0
    image = pygame.image.load(os.path.join("Assets", "Data", "LOAD.png"))
    w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
    while load < 61:
        load += 1
        clock.tick(60)
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        if xo > bw // 8:
            xo = 6 * bw - int(load / 5 * (6 * bw // 12))
        pygame.draw.rect(w, (255, 255, 255),
                         (wd // 2 - 3 * bw - bw // 8, 2 * hg // 5 - bw // 8, 6 * bw + bw // 4, bw + bw // 4), 2,
                         bw // 8)
        pygame.draw.rect(w, (255, 255, 255), (wd // 2 - 3 * bw, 2 * hg // 5, 6 * bw - xo, bw))
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(hg / 25))
        if load % 9 <= 2:
            text = font.render(("LOADING."), True, (255, 255, 255))
        elif load % 9 <= 5:
            text = font.render(("LOADING.."), True, (255, 255, 255))
        else:
            text = font.render(("LOADING..."), True, (255, 255, 255))
        trex = text.get_rect()
        trex.midleft = (wd // 2 - 2 * bw + bw // 2, 2 * hg // 5 + bw + hg // 20)
        w.blit(text, trex)
        pygame.display.update()
    while (run):
        clock.tick(FPS)
        Mouse_Loc = pygame.mouse.get_pos()

        if Music_Settings != 0 and INTEp==1 and Score>100000:
            BGM_Game_Playing.fadeout(2)
            BGM_Game_Playing2.set_volume(1)

            INTEp= 0

        pygame.draw.rect(w, BGCOLOR, (0, 0, wd, hg))
        if ticker<FPS:
            ticker+=1
        else:
            ticker=0
        if ticker%(FPS//15)==0:
            clc+=1
        if clc < 33:
            disp = "mv (" + str(clc) + ").jpg"
        else:
            clc = 1
        image = pygame.image.load(os.path.join("Assets", "Gameplay", disp))
        w.blit(pygame.transform.scale(image, (wd//2, hg)), (0, 0))
        w.blit(pygame.transform.scale(image, (wd// 2, hg)), (wd//2, 0))
        pygame.draw.rect(w, (5, 5, 25), (wd / 2 - (Block_X_No * bw) / 2, (hg - (Block_Y_No * bw)) / 2, Block_X_No * bw, Block_Y_No * bw))
        lm = 0
        j = 0
        Vert_Movement_Clock += 1 + ((Score//5000)/5)
        BGC_Grid_Color_Matcher = 0
        ng = (Block_X_No * Block_Y_No) - 1
        Instantaneous_Block_No = 0
        Instant_Row_Completion_No = 0
        Row_Deletion_Start_Block_No = 0
        if comp==0:
            pygame.draw.rect(w, (235, 80, 78),((wd//2 - (Block_X_No*bw)//2-bw//8)//4-bw, 4*hg//5-bw,2* bw,2* bw),bw, int(bw / 8))
            pygame.draw.rect(w, (235, 80, 78),((wd//2 - (Block_X_No*bw)//2-bw//8)//2-bw, 2*hg//5+bw,2* bw,2* bw),bw , int(bw / 8))
            pygame.draw.rect(w, (235, 80, 78),(3*(wd//2 - (Block_X_No*bw)//2-bw//8)//4-bw, 4*hg//5-bw,2* bw,2* bw),bw , int(bw / 8))
            pygame.draw.rect(w, (235, 80, 78),
                             (wd//2+(wd // 2 - (Block_X_No * bw) // 2 - bw // 8) -3* bw//2, 4 * hg // 5 - bw, 2 * bw, 2 * bw),
                             bw, int(bw / 8))
                             

            pygame.draw.rect(w, (235, 80, 78),(wd-3*bw//2,bw//2,  bw, bw),bw, int(bw / 8)) 
            pygame.draw.rect(w, (235, 80, 78),(bw//2,bw//2,  bw, bw),bw, int(bw / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "Everson Mono Bold.ttf"), int(1.5*bw))
            text = font.render(("△"), True, (1,5,9))
            trex = text.get_rect()
            trex.center = ((wd//2 - (Block_X_No*bw)//2-bw//8)//2,  2*hg//5+bw+bw)
            w.blit(text, trex)
            text = font.render(("◁"), True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = ((wd//2 - (Block_X_No*bw)//2-bw//8)//4, 4*hg//5+bw//10)
            w.blit(text, trex)
            text = font.render(("▷"), True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = (3*(wd // 2 - (Block_X_No * bw) // 2 - bw // 8) // 4, 4 * hg // 5 + bw // 10)
            w.blit(text, trex)
            text = font.render(("⟳"), True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = ( wd//2+(wd//2-(Block_X_No * bw) // 2 + bw // 8-5*bw//8), 4 * hg // 5 + bw // 10)
            w.blit(text, trex)
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "Everson Mono Bold.ttf"), int(1*bw))
            text = font.render(("\u23F8"), True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = ( wd-bw, bw)
            w.blit(text, trex)
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "Everson Mono Bold.ttf"), int(1*bw))
            text = font.render(("☓"), True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = ( bw, bw)
            w.blit(text, trex)

        if Spawn_New_Block == 1:
            if Score//1000 - modder//1000 !=0:                
                modder=Score
            else:
                modder=Score
            while (ng >= 0):
                if Block_Grid_Color_Boolean[(ng)] != 0:
                    Instantaneous_Block_No += 1
                if ng % Block_X_No  == 0:
                    if Instantaneous_Block_No == Block_X_No :
                        Instant_Row_Completion_No += 1
                        if Row_Deletion_Start_Block_No == 0:
                            Row_Deletion_Start_Block_No = ng + 9
                    Instantaneous_Block_No = 0
                ng -= 1
            if Current_Shape[0] < 16 and Current_Shape[0] > 2 and Current_Shape[1] < 16 and Current_Shape[1] > 2 and Current_Shape[2] < 16 and Current_Shape[2] > 2 and Current_Shape[3] < 16 and Current_Shape[3] > 2:
                if Block_Grid_Color_Boolean[(Current_Shape[0] + Block_X_No )] != 0 or Block_Grid_Color_Boolean[(Current_Shape[1] + Block_X_No )] != 0 or Block_Grid_Color_Boolean[(Current_Shape[2] + Block_X_No )] != 0 or                        Block_Grid_Color_Boolean[(Current_Shape[3] + Block_X_No )] != 0:
                    endmusicclock = 1
                    run = False

        if Instant_Row_Completion_No != 0:
            if Instant_Row_Completion_No == 4:
                Score += 5000
                if randint(0, 1) == 0:
                    SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "4l-1.wav"))
                    if SFX_Settings == 1:
                        SFX.play()
                else:
                    SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "4l-2.wav"))
                    if SFX_Settings==1:
                        SFX.play()
            elif Instant_Row_Completion_No == 1:
                Score += 625
                SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "1l.wav"))
                if SFX_Settings==1:
                    SFX.play()
            else:
                SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "2-3l.wav"))
                if SFX_Settings==1:
                    SFX.play()
                if Instant_Row_Completion_No == 3:
                    Score += 2850
                else:
                    Score += 1625
            while (Row_Deletion_Start_Block_No >= 0):
                if Instant_Row_Completion_No == 4 and Row_Deletion_Start_Block_No <= 39:                    Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = 0
                elif Instant_Row_Completion_No == 3 and Row_Deletion_Start_Block_No <= 29: Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = 0
                elif Instant_Row_Completion_No == 2 and Row_Deletion_Start_Block_No <= 19:       Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = 0
                elif Instant_Row_Completion_No == 1 and Row_Deletion_Start_Block_No <= 9:                 Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = 0
                elif Instant_Row_Completion_No == 4:    Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = Block_Grid_Color_Boolean[
                    (Row_Deletion_Start_Block_No - 40)]
                elif Instant_Row_Completion_No == 3:      Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = Block_Grid_Color_Boolean[
                    (Row_Deletion_Start_Block_No - 30)]
                elif Instant_Row_Completion_No == 2:      Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = Block_Grid_Color_Boolean[
                    (Row_Deletion_Start_Block_No - 20)]
                elif Instant_Row_Completion_No == 1:      Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = Block_Grid_Color_Boolean[
                    (Row_Deletion_Start_Block_No - Block_X_No )]
                Row_Deletion_Start_Block_No -= 1
        while (lm < Block_Y_No):
            j = 0
            lm += 1
            while (j < Block_X_No):
                ng = 0
                x3 = convx(Current_Shape_Display_Grid[(ng)])
                y3 = convy(Current_Shape_Display_Grid[(ng)])
                if (Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 0):
                    pygame.draw.rect(w, Block_Grid_Free_Color, ((Block_Grid_X[(j)]), Block_Grid_Y[(lm - 1)], bw, bw),int(bw/40), int(bw/8))
                elif (Stop_Current_Shape_Movement != 0 and Block_Grid_Color_Boolean[(Current_Shape[0])] != 0 and                     Block_Grid_Color_Boolean[(Current_Shape[1])] != 0 and Block_Grid_Color_Boolean[
                          (Current_Shape[2])] != 0 and Block_Grid_Color_Boolean[
                          (Current_Shape[3])] != 0):
                    pygame.draw.rect(w, Block_Grid_Free_Color, ((Block_Grid_X[(j)]), Block_Grid_Y[(lm - 1)], bw, bw),
                                     int(bw / 40), int(bw / 8))
                    pygame.draw.rect(w, Block_Grid_Red,((Block_Grid_X[(j)]) + int(bw/20), Block_Grid_Y[(lm - 1)]+int(bw/20), int(9*bw/10), int(9*bw/10)),bw,int(bw/8))
                elif ((Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] != 0)):
                    if Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 1:
                        Block_Grid_Color = (26, 194, 241)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 2:
                        Block_Grid_Color = (253, 223, 102)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 3:
                        Block_Grid_Color = (151, 59, 152)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 4:
                        Block_Grid_Color = (0, 131, 196)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 5:
                        Block_Grid_Color = (247, 160, 67)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 6:
                        Block_Grid_Color = (148, 202, 100)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 7:
                        Block_Grid_Color = (238, 69, 51)

                    pygame.draw.rect(w, Block_Grid_Free_Color, ((Block_Grid_X[(j)]), Block_Grid_Y[(lm - 1)], bw, bw),
                                     int(bw / 40), int(bw / 8))
                    pygame.draw.rect(w, Block_Grid_Color,((Block_Grid_X[(j)]) + int(bw/20), Block_Grid_Y[(lm - 1)]+int(bw/20), int(9*bw/10), int(9*bw/10)),28*int(bw/40),int(bw/8))
                j += 1
                BGC_Grid_Color_Matcher += 1
        if (Spawn_New_Block == 1):
            Current_Shape_Randomizer = Next_Shape_Randomizer
            Next_Shape_Randomizer = randint(1, 7)            
            Stop_Current_Shape_Movement = 0
            Rotaion_Status = 0
            Current_Shape_Color = Next_Shape_Color
            if Next_Shape_Randomizer == 1:
                Next_Shape_Color = (26, 194, 241)
            elif Next_Shape_Randomizer == 2:
                Next_Shape_Color = (253, 223, 102)
            elif Next_Shape_Randomizer == 3:
                Next_Shape_Color = (151, 59, 152)
            elif Next_Shape_Randomizer == 4:
                Next_Shape_Color = (0, 131, 196)
            elif Next_Shape_Randomizer == 5:
                Next_Shape_Color = (247, 160, 67)
            elif Next_Shape_Randomizer == 6:
                Next_Shape_Color = (148, 202, 100)
            elif Next_Shape_Randomizer == 7:
                Next_Shape_Color = (238, 69, 51)
        if Spawn_New_Block==1 and Current_Shape_Randomizer == 1:
            Current_Shape[0] = 3
            Current_Shape[1] = 4
            Current_Shape[2] = 5
            Current_Shape[3] = 6
            Spawn_New_Block = 0
            Rotation_Shape = 1
        if Spawn_New_Block==1 and Current_Shape_Randomizer == 2:
            Current_Shape[0] = 14
            Current_Shape[1] = 15
            Current_Shape[2] = 4
            Current_Shape[3] = 5
            Spawn_New_Block= 0
            Rotation_Shape = 2
        if Spawn_New_Block==1 and Current_Shape_Randomizer == 3:
            Current_Shape[0] = 3
            Current_Shape[1] = 4
            Current_Shape[2] = 5
            Current_Shape[3] = 14
            Spawn_New_Block = 0
            Rotation_Shape = 3
        if Spawn_New_Block==1 and Current_Shape_Randomizer == 4:
            Current_Shape[0] = 3
            Current_Shape[1] = 13
            Current_Shape[2] = 14
            Current_Shape[3] = 15
            Spawn_New_Block = 0
            Rotation_Shape = 4
        if Spawn_New_Block==1 and Current_Shape_Randomizer == 5:
            Current_Shape[0] = 5
            Current_Shape[1] = 15
            Current_Shape[2] = 14
            Current_Shape[3] = 13
            Spawn_New_Block = 0
            Rotation_Shape = 5
        if Spawn_New_Block==1 and Current_Shape_Randomizer == 6:
            Current_Shape[0] = 13
            Current_Shape[1] = 14
            Current_Shape[2] = 4
            Current_Shape[3] = 5
            Spawn_New_Block = 0
            Rotation_Shape = 6
        if Spawn_New_Block==1 and Current_Shape_Randomizer == 7:
            Current_Shape[0] = 3
            Current_Shape[1] = 4
            Current_Shape[2] = 14
            Current_Shape[3] = 15
            Spawn_New_Block = 0
            Rotation_Shape = 7
        if Next_Shape_Randomizer == 1:
            Next_Shape[0] = 4
            Next_Shape[1] = 5
            Next_Shape[2] = 6
            Next_Shape[3] = 7
        if Next_Shape_Randomizer == 2:
            Next_Shape[0] = 1
            Next_Shape[1] = 2
            Next_Shape[2] = 5
            Next_Shape[3] = 6
        if Next_Shape_Randomizer == 3:
            Next_Shape[0] = 1
            Next_Shape[1] = 2
            Next_Shape[2] = 3
            Next_Shape[3] = 6
        if Next_Shape_Randomizer == 4:
            Next_Shape[0] = 1
            Next_Shape[1] = 5
            Next_Shape[2] = 6
            Next_Shape[3] = 7
        if Next_Shape_Randomizer == 5:
            Next_Shape[0] = 3
            Next_Shape[1] = 5
            Next_Shape[2] = 6
            Next_Shape[3] = 7
        if Next_Shape_Randomizer == 6:
            Next_Shape[0] = 1
            Next_Shape[1] = 5
            Next_Shape[2] = 6
            Next_Shape[3] = 10
        if Next_Shape_Randomizer == 7:
            Next_Shape[0] = 2
            Next_Shape[1] = 5
            Next_Shape[2] = 6
            Next_Shape[3] = 9
        if Rotation_Clock < Rotation_Frequency:
            Rotation_Clock += 5
        keypress = pygame.key.get_pressed()
        if Rotation_Clock == Rotation_Frequency and (keypress[pygame.K_SPACE]or TR==1):
            TR=0
            Rotation_Mananger_Boolean = 0
            Rotation_Clock = 0
        if Rotation_Mananger_Boolean == 0:
            Rotation_Mananger_Boolean = 1
            SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "rot.wav"))
            if SFX_Settings==1:
                SFX.play()
            if Rotation_Shape == 1 :
                if Rotaion_Status == 0 and Current_Shape[3]>19 and Block_Grid_Color_Boolean[(Current_Shape[0]+11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]-11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]-22)]==0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 11
                    Current_Shape[2] -= 11
                    Current_Shape[3] -= 22
                elif Rotaion_Status == 0 and Current_Shape[3] > 9 and Block_Grid_Color_Boolean[(Current_Shape[0] + 22)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 11)] == 0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 22
                    Current_Shape[1] += 11
                    Current_Shape[3] -= 11
                elif Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 33)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 22)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2]+33)] == 0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 33
                    Current_Shape[1] += 22
                    Current_Shape[2] += 11
                elif Rotaion_Status == 1 and Current_Shape[3]%10<(Current_Shape[3] +22)%10 and Current_Shape[0]%10>(Current_Shape[0] - 11)%10 and Block_Grid_Color_Boolean[(Current_Shape[0]-11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]+11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+22)]==0:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] += 11
                    Current_Shape[3] += 22
                elif Rotaion_Status == 1 and Current_Shape[3]%10<(Current_Shape[3] +11)%10 and Current_Shape[0]%10>(Current_Shape[0] - 22)%10 and Block_Grid_Color_Boolean[(Current_Shape[0]-22)]==0 and Block_Grid_Color_Boolean[(Current_Shape[1]-11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+11)]==0:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 22
                    Current_Shape[1] -= 11
                    Current_Shape[3] += 11
                elif Rotaion_Status == 1 and Current_Shape[0]%10==0 and Block_Grid_Color_Boolean[(Current_Shape[1]+11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]+22)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+33)]==0:
                    Rotaion_Status = 0
                    Current_Shape[1] += 11
                    Current_Shape[2] += 22
                    Current_Shape[3] += 33
                elif Rotaion_Status == 1 and Current_Shape[0]%10==9 and Block_Grid_Color_Boolean[(Current_Shape[0]-13)]==0 and Block_Grid_Color_Boolean[(Current_Shape[1]-2)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]+9)]==0 and Block_Grid_Color_Boolean[(20+Current_Shape[3])]==0:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 13
                    Current_Shape[1] -= 2
                    Current_Shape[2] +=9
                    Current_Shape[3]+=20
                Rotation_Shape = 1
            if Rotation_Shape == 3:
                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0]-9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]+9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]-11)]==0:
                    Rotaion_Status = 1
                    Current_Shape[0] -= 9
                    Current_Shape[2] += 9
                    Current_Shape[3] -= 11
                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0]+11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]-11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]-9)]==0:
                    Rotaion_Status = 2
                    Current_Shape[0] += 11
                    Current_Shape[2] -= 11
                    Current_Shape[3] -= 9
                elif Rotaion_Status == 2 and Block_Grid_Color_Boolean[(Current_Shape[0]+9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]-9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+11)]==0:
                    Rotaion_Status = 3
                    Current_Shape[0] += 9
                    Current_Shape[2] -= 9
                    Current_Shape[3] += 11
                elif Rotaion_Status == 3 and Block_Grid_Color_Boolean[(Current_Shape[0]-11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]+11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+9)]==0:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] += 11
                    Current_Shape[3] += 9
            if Rotation_Shape == 4:
                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0]+2)]==0 and Block_Grid_Color_Boolean[(Current_Shape[1]-9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+9)]==0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 2
                    Current_Shape[1] -= 9
                    Current_Shape[3] += 9
                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0]+20)]==0 and Block_Grid_Color_Boolean[(Current_Shape[1]+11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]-11)]==0:
                    Rotaion_Status = 2
                    Current_Shape[0] += 20
                    Current_Shape[1] += 11
                    Current_Shape[3] -= 11
                elif Rotaion_Status == 2 and Block_Grid_Color_Boolean[(Current_Shape[0]-2)]==0 and Block_Grid_Color_Boolean[(Current_Shape[1]+9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]-9)]==0:
                    Rotaion_Status = 3
                    Current_Shape[0] -= 2
                    Current_Shape[1] += 9
                    Current_Shape[3] -= 9
                elif Rotaion_Status == 3 and Block_Grid_Color_Boolean[(Current_Shape[0]-20)]==0 and Block_Grid_Color_Boolean[(Current_Shape[1]-11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+11)]==0:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 20
                    Current_Shape[1] -= 11
                    Current_Shape[3] += 11
            if Rotation_Shape == 5:
                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0]+20)]==0 and Block_Grid_Color_Boolean[(Current_Shape[1]+9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]-9)]==0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 20
                    Current_Shape[1] += 9
                    Current_Shape[3] -= 9
                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0]-2)]==0 and Block_Grid_Color_Boolean[(Current_Shape[1]-11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+11)]==0:
                    Rotaion_Status = 2
                    Current_Shape[0] -= 2
                    Current_Shape[1] -= 11
                    Current_Shape[3] += 11
                elif Rotaion_Status == 2 and Block_Grid_Color_Boolean[(Current_Shape[0]-20)]==0 and Block_Grid_Color_Boolean[(Current_Shape[1]-9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+9)]==0:
                    Rotaion_Status = 3
                    Current_Shape[0] -= 20
                    Current_Shape[1] -= 9
                    Current_Shape[3] += 9
                elif Rotaion_Status == 3 and Block_Grid_Color_Boolean[(Current_Shape[0]+2)]==0 and Block_Grid_Color_Boolean[(Current_Shape[1]+11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]-11)]==0:
                    Rotaion_Status = 0
                    Current_Shape[0] += 2
                    Current_Shape[1] += 11
                    Current_Shape[3] -= 11
            if Rotation_Shape == 6:
                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0]+11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]+9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]-2)]==0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 11
                    Current_Shape[2] += 9
                    Current_Shape[3] -= 2
                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0]-11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]-9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+2)]==0:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] -= 9
                    Current_Shape[3] += 2
            if Rotation_Shape == 7:
                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0]+11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]-9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]-20)]==0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 11
                    Current_Shape[2] -= 9
                    Current_Shape[3] -= 20
                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0]-11)]==0 and Block_Grid_Color_Boolean[(Current_Shape[2]+9)]==0 and Block_Grid_Color_Boolean[(Current_Shape[3]+20)]==0:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] += 9
                    Current_Shape[3] += 20
        if (Stop_Current_Shape_Movement == 0 and Block_Grid_Color_Boolean[(Current_Shape[0])] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1])] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2])] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3])] == 0):
            ng = Current_Shape[0]
            x3 = convx(Current_Shape_Display_Grid[(ng)])
            y3 = convy(Current_Shape_Display_Grid[(ng)])          
            pygame.draw.rect(w, Current_Shape_Color, (Block_Grid_X[(x3)]+bw/20, Block_Grid_Y[(y3)]+bw/20, int(9*bw/10), int(9*bw/10)) ,28*int(bw/40),int(bw/8) )
            ng = Current_Shape[1]
            x3 = convx(Current_Shape_Display_Grid[(ng)])
            y3 = convy(Current_Shape_Display_Grid[(ng)])            
            pygame.draw.rect(w, Current_Shape_Color, (Block_Grid_X[(x3)]+bw/20, Block_Grid_Y[(y3)]+bw/20, int(9*bw/10), int(9*bw/10)) ,28*int(bw/40),int(bw/8) )
            ng = Current_Shape[2]
            x3 = convx(Current_Shape_Display_Grid[(ng)])
            y3 = convy(Current_Shape_Display_Grid[(ng)])            
            pygame.draw.rect(w, Current_Shape_Color, (Block_Grid_X[(x3)]+bw/20, Block_Grid_Y[(y3)]+bw/20, int(9*bw/10), int(9*bw/10)) ,28*int(bw/40),int(bw/8) )
            ng = Current_Shape[3]
            x3 = convx(Current_Shape_Display_Grid[(ng)])
            y3 = convy(Current_Shape_Display_Grid[(ng)])           
            pygame.draw.rect(w, Current_Shape_Color, (Block_Grid_X[(x3)]+bw/20, Block_Grid_Y[(y3)]+bw/20, int(9*bw/10), int(9*bw/10)) ,28*int(bw/40),int(bw/8) )
        if (Stop_Current_Shape_Movement == 0 ):
            ng = Next_Shape[0]
            x3 = math.floor(int(Next_Shape_Display_Grid[ng]/10000))
            y3 = Next_Shape_Display_Grid[ng]%10000
            pygame.draw.rect(w, Next_Shape_Color, (x3 + bw/20, y3+bw/20, int(9*bw/10), int(9*bw/10)),28*int(bw/40),int(bw/8))
            ng = Next_Shape[1]
            x3 = math.floor(int(Next_Shape_Display_Grid[ng] / 10000))
            y3 = Next_Shape_Display_Grid[ng] % 10000
            pygame.draw.rect(w, Next_Shape_Color, (x3 + bw/20, y3+bw/20, int(9*bw/10), int(9*bw/10)),28*int(bw/40),int(bw/8))
            ng = Next_Shape[2]
            x3 = math.floor(int(Next_Shape_Display_Grid[ng] / 10000))
            y3 = Next_Shape_Display_Grid[ng] % 10000
            pygame.draw.rect(w, Next_Shape_Color, (x3 + bw/20, y3+bw/20, int(9*bw/10), int(9*bw/10)),28*int(bw/40),int(bw/8))
            ng = Next_Shape[3]
            x3 = math.floor(int(Next_Shape_Display_Grid[ng] / 10000))
            y3 = Next_Shape_Display_Grid[ng] % 10000
            pygame.draw.rect(w, Next_Shape_Color, (x3 + bw/20, y3+bw/20, int(9*bw/10), int(9*bw/10)),28*int(bw/40),int(bw/8))
        if Vert_Movement_Clock >=60:
            ijx = 0
            Vert_Movement_Clock = 0
        else:
            ijx = 5
        if (Current_Shape[0] > (Block_X_No * Block_Y_No - Block_X_No -1) or Current_Shape[1] > (Block_X_No * Block_Y_No - Block_X_No -1) or Current_Shape[2] > (Block_X_No*Block_Y_No - Block_X_No -1) or Current_Shape[3] > (Block_X_No*Block_Y_No - Block_X_No -1)):
            ijx = 5
            inx = 0
            Stop_Current_Shape_Movement = 1
            Spawn_New_Block = 1
            SFX= pygame.mixer.Sound(os.path.join( "Assets" , "Music and SFX","land.wav"))
            if SFX_Settings==1:
                SFX.play()
            while (inx < 4):
                Block_Grid_Color_Boolean[(Current_Shape[(inx)])] = Current_Shape_Randomizer
                inx += 1
        elif (Block_Grid_Color_Boolean[(Current_Shape[0] + Block_X_No )] != 0 or Block_Grid_Color_Boolean[(Current_Shape[1] + Block_X_No )] != 0 or Block_Grid_Color_Boolean[(Current_Shape[2] + Block_X_No )] != 0 or Block_Grid_Color_Boolean[(Current_Shape[3] + Block_X_No )] != 0):
            ijx = 5
            inx = 0
            Stop_Current_Shape_Movement = 1
            Spawn_New_Block = 1
            while (inx < 4):
                Block_Grid_Color_Boolean[(Current_Shape[(inx)])] = Current_Shape_Randomizer
                inx += 1
            if (Current_Shape[0] >9 and Current_Shape[1]  >9 and Current_Shape[2]  >9 and Current_Shape[3] >9):
                SFX= pygame.mixer.Sound(os.path.join( "Assets" , "Music and SFX","land.wav"))
                if SFX_Settings==1:
                    SFX.play()
        while (ijx < 4):
            Current_Shape[ijx] += Block_X_No
            ijx += 1
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("        Score:      ", True, (255, 189, 164))
        trex = text.get_rect()
        trex.center = (int(((15+Block_X_No+ 2.1) * bw)), int(0.475 * hg))
        w.blit(text, trex)
        text = font.render(str(Score), True, (255, 189, 164))
        trex = text.get_rect()
        trex.center = (int(((15+Block_X_No+ 2.1) * bw)), int(0.475 * hg) + 35)
        w.blit(text, trex)
        keypress = pygame.key.get_pressed()
        if Left_Movement_Clock < Left_Movement_Clock_Frequency:
            Left_Movement_Clock += 5
        if Right_Movement_Clock < Right_Movement_Clock_Frequency:
            Right_Movement_Clock += 5
        if Down_Movement_Clock < Down_Movement_Clock_Frequency:
            Down_Movement_Clock += 5
        if IMD_Movement_Clock < IMD_Movement_Clock_Frequency:
            IMD_Movement_Clock += 5
        if (keypress[pygame.K_a] or TA==1) and Left_Movement_Clock == Left_Movement_Clock_Frequency and (
        Current_Shape[0]) % Block_X_No  != 0 and (Current_Shape[1]) % Block_X_No  != 0 and (Current_Shape[2]) % Block_X_No  != 0 and (
        Current_Shape[3]) % Block_X_No  != 0 and Block_Grid_Color_Boolean[(Current_Shape[0] - 1)] == 0 and \
                Block_Grid_Color_Boolean[(Current_Shape[1] - 1)] == 0 and Block_Grid_Color_Boolean[
            (Current_Shape[2] - 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 1)] == 0:
            ijx = 0
            TA=0
            Left_Movement_Clock = 0
            SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "move.wav"))
            if SFX_Settings==1:
                SFX.play()
            while (ijx < 4):
                Current_Shape[ijx] -= 1
                ijx += 1
        if (keypress[pygame.K_d] or TD==1) and Right_Movement_Clock == Right_Movement_Clock_Frequency and (
                Current_Shape[0] - 9) % Block_X_No  != 0 and (Current_Shape[1] - 9) % Block_X_No  != 0 and (
                Current_Shape[2] - 9) % Block_X_No  != 0 and (Current_Shape[3] - 9) % Block_X_No  != 0 and Block_Grid_Color_Boolean[
            (Current_Shape[0] + 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 1)] == 0 and \
                Block_Grid_Color_Boolean[(Current_Shape[2] + 1)] == 0 and Block_Grid_Color_Boolean[
            (Current_Shape[3] + 1)] == 0:
            ijx = 0
            TD=0
            Right_Movement_Clock = 0
            SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "move.wav"))
            if SFX_Settings==1:
                SFX.play()
            while (ijx < 4):
                Current_Shape[ijx] += 1
                ijx += 1
        if ((keypress[pygame.K_s] or TS==1) and Down_Movement_Clock  == Down_Movement_Clock_Frequency and Current_Shape[0] < Block_X_No*Block_Y_No - Block_X_No and Current_Shape[
            1] < Block_X_No*Block_Y_No - Block_X_No and Current_Shape[2] < Block_X_No*Block_Y_No - Block_X_No and Current_Shape[3] < Block_X_No*Block_Y_No - Block_X_No):
            ijx = 0
            TS=0
            Down_Movement_Clock = 0
            while (ijx < 4):
                Current_Shape[ijx] += Block_X_No
                ijx += 1
        if ((keypress[pygame.K_w] or TW==1)and IMD_Movement_Clock == IMD_Movement_Clock_Frequency and Current_Shape[0] < Block_X_No*Block_Y_No - Block_X_No  and Current_Shape[1] < Block_X_No*Block_Y_No - Block_X_No and Current_Shape[2] < Block_X_No*Block_Y_No - Block_X_No  and
                Current_Shape[3] < Block_X_No*Block_Y_No - Block_X_No ):
            ifx=0
            TW=0
            IMD_Movement_Clock =0
            while (ifx!=5):
                ifx=0
                if (Current_Shape[0] > (Block_X_No * Block_Y_No - Block_X_No - 1) or Current_Shape[1] > (
                        Block_X_No * Block_Y_No - Block_X_No - 1) or Current_Shape[2] > (
                        Block_X_No * Block_Y_No - Block_X_No - 1) or Current_Shape[3] > (
                        Block_X_No * Block_Y_No - Block_X_No - 1)):
                    ifx = 5
                    inx = 0
                    Stop_Current_Shape_Movement = 1
                    Spawn_New_Block = 1
                    SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "land.wav"))
                    if SFX_Settings==1:
                        SFX.play()
                    while (inx < 4):
                        Block_Grid_Color_Boolean[(Current_Shape[(inx)])] = Current_Shape_Randomizer
                        inx += 1
                elif (Block_Grid_Color_Boolean[(Current_Shape[0] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[
                    (Current_Shape[1] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[
                          (Current_Shape[2] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[
                          (Current_Shape[3] + Block_X_No)] != 0):
                    ifx = 5
                    inx = 0
                    Stop_Current_Shape_Movement = 1
                    Spawn_New_Block = 1
                    while (inx < 4):
                        Block_Grid_Color_Boolean[(Current_Shape[(inx)])] = Current_Shape_Randomizer
                        inx += 1
                    if (Current_Shape[0] > 9 and Current_Shape[1] > 9 and Current_Shape[2] > 9 and Current_Shape[
                        3] > 9):
                        SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "land.wav"))
                        if SFX_Settings==1:
                            SFX.play()
                while (ifx < 4):
                    Current_Shape[ifx] += Block_X_No
                    ifx += 1
        if (keypress[pygame.K_p] or TP==1):
            pause = 1
            disp = ""
            TP=0
            if Music_Settings!=0 and BGM_Game_Playing2.get_volume()==0:
                BGM_Game_Playing.set_volume(0)
            elif  Music_Settings!=0 and BGM_Game_Playing2.get_volume()!=0:
                BGM_Game_Playing2.set_volume(0)
            SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "pause.wav"))
            if SFX_Settings==1:
                SFX.play()
            BGM_Paused = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "paused.wav"))
            click=0
            spaceb=0
            dec=0
            tnx=0
            clc2=0
            if Music_Settings!=0:
                BGM_Paused.play(loops=-1)
            while (pause == 1):
                Mouse_Loc = pygame.mouse.get_pos()
                clock.tick(FPS)
                clc2 += 1
                if clc2==11 :
                    spaceb=1
                if clc < 128 and tnx%int(FPS/11)==0:
                    clc += 1
                    disp = "mv (" + str(clc) + ").jpg"
                elif clc>127:
                    clc = 0
                if tnx<FPS+1:
                    tnx+=1
                if tnx>FPS:
                    tnx=0
                pygame.draw.rect(w, BGCOLOR, (0, 0, wd, hg))
                image = pygame.image.load(os.path.join("Assets", "Pause", disp))
                w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
                font = pygame.font.Font('freesansbold.ttf', bw)
                text = font.render('    Score:    ', True, (231,171,196))
                trex = text.get_rect()
                trex.center = (4*wd //5, 1*hg//5)
                w.blit(text, trex)
                text = font.render(str(Score), True, (231, 171, 196))
                trex = text.get_rect()
                trex.center = (4*wd //5, hg //5+bw//2+bw)
                w.blit(text, trex)                
                font = pygame.font.Font(os.path.join("Assets", "Fonts", "Everson Mono Bold.ttf"), 6*bw//10)               
                pygame.draw.rect(w,(115, 132, 200),((bw/2),(bw/2),3*bw//4,3*bw//4),bw//2,int(bw/4))
                text = font.render('☓', True, (231,171,196))
                trex = text.get_rect()
                trex.center = (7*bw//8, 14*bw//16)
                w.blit(text, trex)     
                font = pygame.font.Font('freesansbold.ttf', 6*bw//10)                                                               
                pygame.draw.rect(w,(231,171,196),((wd//2 + wd//17),(4*hg//7), 3*bw,bw),bw//2,int(bw/4))
                pygame.draw.rect(w,(231,171,196),(int(wd//2 + wd//17+0.1*bw),(401*hg//700), int(2.7*bw),9*bw//10))               
                pygame.draw.rect(w,(231,171,196),((wd//2 - wd//17 -3*bw),(4*hg//7), 3*bw,bw),bw//2,int(bw/4))
                pygame.draw.rect(w,(231,171,196),(int(wd//2 - wd//17-0.1*bw-int(2.7*bw)),(401*hg//700), int(2.7*bw),9*bw//10))
                text = font.render('  Resume', True, (115, 132, 200))
                trex = text.get_rect()
                trex.topleft = (wd // 2 + wd//17-bw//35, 4*hg//7+bw//5)
                w.blit(text, trex)
                text = font.render('Menu  ', True, (115, 132, 200))
                trex = text.get_rect()
                trex.topright = (wd // 2- wd//16-bw//5, 4*hg//7+bw//5)                           
                w.blit(text, trex)

                if visi==1:
                    pygame.draw.rect(w, (115, 132, 200), (
                        (wd // 2 - wd // 17 - 3.5 * bw), (hg // 2 - hg // 6), 2 * wd // 17 + 7 * bw, hg // 3), 3 * bw,
                                     int(bw))
                    pygame.draw.rect(w, (231, 171, 196), ((wd // 2 + wd // 25), (4 * hg // 7), 3 * bw, bw), bw // 2,
                                     int(bw / 4))
                    pygame.draw.rect(w, (231, 171, 196), (
                        int(wd // 2 + wd // 25 + 0.1 * bw), (401 * hg // 700), int(2.7 * bw), 9 * bw // 10))
                    pygame.draw.rect(w, (231, 171, 196), ((wd // 2 - wd // 25 - 3 * bw), (4 * hg // 7), 3 * bw, bw),
                                     bw // 2, int(bw / 4))
                    pygame.draw.rect(w, (231, 171, 196), (
                        int(wd // 2 - wd // 25 - 0.1 * bw - int(2.7 * bw)), (401 * hg // 700), int(2.7 * bw),
                        9 * bw // 10))
                    pygame.draw.rect(w, (115, 132, 200), ((wd // 2 - 3 * bw), (hg // 2 - hg // 8), 6 * bw, hg // 6),
                                     3 * bw, int(bw))
                    font = pygame.font.Font('freesansbold.ttf', 7 * bw // 10)
                    text = font.render('Are You Sure', True, (231, 171, 196))
                    trex = text.get_rect()
                    trex.center = (wd // 2, 3 * hg // 7)
                    w.blit(text, trex)
                    text = font.render('You Want To Exit?', True, (231, 171, 196))
                    trex = text.get_rect()
                    trex.center = (wd // 2, 3 * hg // 7 + bw)
                    w.blit(text, trex)
                    font = pygame.font.Font('freesansbold.ttf', 4 * bw // 10)
                    text = font.render('All Unsaved Data Will Be Lost', True, (231, 101, 106))
                    trex = text.get_rect()
                    trex.center = (wd // 2, 3 * hg // 7 + 19 * bw // 10)
                    w.blit(text, trex)
                    font = pygame.font.Font('freesansbold.ttf', 6 * bw // 10)
                    text = font.render('   NO', True, (115, 132, 200))
                    trex = text.get_rect()
                    trex.topleft = (wd // 2 + wd // 17 - bw // 35, 4 * hg // 7 + bw // 5)
                    w.blit(text, trex)
                    text = font.render('YES', True, (115, 132, 200))
                    trex = text.get_rect()
                    trex.topright = (wd // 2 - wd // 16 - bw // 5, 4 * hg // 7 + bw // 5)
                    w.blit(text, trex)
                    if click == 1:
                        click = 0
                        if 4 * hg // 7 < Mouse_Loc[1] < 4 * hg // 7 + 9 * bw // 10:
                            if int(wd // 2 + wd // 25) < Mouse_Loc[0] < int(wd // 2 + wd // 25) + 3 * bw:
                                visi = 0
                            elif (wd // 2 - wd // 25 - 3 * bw) < Mouse_Loc[0] < (
                                    wd // 2 - wd // 25 - 3 * bw) + 3 * bw:
                                visi = 0
                                dec = 1
                    if dec == 1:
                        run = False
                        pause = 0

                        es = 1


                if visi==2:
                    pygame.draw.rect(w, (115, 132, 200), ((wd // 2 - wd // 17 - 3.5 * bw), (hg // 2 - hg // 6), 2 * wd // 17 + 7 * bw, hg // 3), 3 * bw,int(bw))
                    pygame.draw.rect(w, (231, 171, 196), ((wd // 2 + wd // 25), (4 * hg // 7), 3 * bw, bw), bw // 2,
                                     int(bw / 4))
                    pygame.draw.rect(w, (231, 171, 196), (
                    int(wd // 2 + wd // 25 + 0.1 * bw), (401 * hg // 700), int(2.7 * bw), 9 * bw // 10))
                    pygame.draw.rect(w, (231, 171, 196), ((wd // 2 - wd // 25 - 3 * bw), (4 * hg // 7), 3 * bw, bw),
                                     bw // 2, int(bw / 4))
                    pygame.draw.rect(w, (231, 171, 196), (
                    int(wd // 2 - wd // 25 - 0.1 * bw - int(2.7 * bw)), (401 * hg // 700), int(2.7 * bw), 9 * bw // 10))
                    pygame.draw.rect(w, (115, 132, 200), ((wd // 2 - 3 * bw), (hg // 2 - hg // 8), 6 * bw, hg // 6),
                                     3 * bw, int(bw))
                    font = pygame.font.Font('freesansbold.ttf', 7 * bw // 10)
                    text = font.render('Are You Sure You Want', True, (231, 171, 196))
                    trex = text.get_rect()
                    trex.center = (wd // 2, 3 * hg // 7)
                    w.blit(text, trex)
                    text = font.render('To Return To The Main Menu?', True, (231, 171, 196))
                    trex = text.get_rect()
                    trex.center = (wd // 2, 3 * hg // 7 + bw)
                    w.blit(text, trex)
                    font = pygame.font.Font('freesansbold.ttf', 4 * bw // 10)
                    text = font.render('All Unsaved Data Will Be Lost', True, (231, 101, 106))
                    trex = text.get_rect()
                    trex.center = (wd // 2, 3 * hg // 7 + 19 * bw // 10)
                    w.blit(text, trex)
                    font = pygame.font.Font('freesansbold.ttf', 6 * bw // 10)
                    text = font.render('   NO', True, (115, 132, 200))
                    trex = text.get_rect()
                    trex.topleft = (wd // 2 + wd // 17 - bw // 35, 4 * hg // 7 + bw // 5)
                    w.blit(text, trex)
                    text = font.render('YES', True, (115, 132, 200))
                    trex = text.get_rect()
                    trex.topright = (wd // 2 - wd // 16 - bw // 5, 4 * hg // 7 + bw // 5)
                    w.blit(text, trex)
                    if click == 1:
                        click = 0
                        if 4 * hg // 7 < Mouse_Loc[1] < 4 * hg // 7 + 9 * bw // 10:
                            if int(wd // 2 + wd // 25) < Mouse_Loc[0] < int(wd // 2 + wd // 25) + 3 * bw:
                                visi = 0
                            elif (wd // 2 - wd // 25 - 3 * bw) < Mouse_Loc[0] < (wd // 2 - wd // 25 - 3 * bw) + 3 * bw:
                                visi = 0
                                dec = 1
                    if dec == 1:
                        run = False

                        pause = 0
                        es = 3

                if bw//2 < Mouse_Loc[1] < bw//2+ 3*bw//4 and bw//2 < Mouse_Loc[0] < bw//2+ 3*bw//4 and click==1:
                    visi=1
                keypress = pygame.key.get_pressed()
                pygame.display.update()  
                if click==1:
                    click=0
                    if 4*hg//7 < Mouse_Loc[1] < 4*hg//7 + 9*bw//10:
                        if int(wd // 2 + wd // 17) < Mouse_Loc[0] < int(wd // 2 + wd // 17) +3*bw:
                            run=True
                            pause=0
                        elif (wd // 2 - wd // 17 - 3 * bw) < Mouse_Loc[0] < (wd // 2 - wd // 17 - 3 * bw) + 3*bw:
                            visi=2
                for event in pygame.event.get():
                    if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                        visi=1
                    if keypress[pygame.K_p] and spaceb==1 :
                        run = True
                        pause = 0
                    if event.type==pygame.MOUSEBUTTONUP:
                        click=1                  
            pygame.init()
            BGM_Paused.fadeout(1)
            clc=1
            SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "pause.wav"))
            if SFX_Settings==1:
                SFX.play()
            if Music_Settings != 0 and Score<100000:
                BGM_Game_Playing.set_volume(1)
            elif Score>100000 and Music_Settings != 0:
                BGM_Game_Playing2.set_volume(1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keypress[pygame.K_ESCAPE]:
                TP=1
                visi=1
            if event.type==pygame.MOUSEBUTTONUP and comp==0:
                if Mouse_Loc[0]>wd//2 - (Block_X_No/2)*bw and Mouse_Loc[0]<wd//2 +(Block_X_No/2)*bw and Mouse_Loc[1]<hg:
                    TS=1
                if Mouse_Loc[0]<wd//2 - (Block_X_No/2)*bw and Mouse_Loc[1]<hg:
                    if(Mouse_Loc[1]<hg//7):
                        run=False
                        es=1
                    elif(Mouse_Loc[1]<4* hg//7):
                        TW=1
                    elif (Mouse_Loc[0]<(wd//2 - Block_X_No//2*bw)/2):
                        TA=1
                    else:
                        TD=1
                elif Mouse_Loc[0]<wd and Mouse_Loc[0]>wd//2 + (Block_X_No/2)*bw and Mouse_Loc[1]<hg:
                    if(Mouse_Loc[1]<hg//7):
                        TP=1
                    else:
                        TR=1            
    play = 0
    click=0
    nhs = 0
    if Score >=High_Score and es!=1:
        doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
        L[4] = str(Score) + "\n"
        nhs = 1
        doc.writelines(L)
        doc.close()
    resetg = 0
    if Music_Settings != 0 :
        BGM_Game_Playing.set_volume(0)
        BGM_Game_Playing2.set_volume(0)

    if es==3:
        resetg=1
        load = 0
        xo = 6 * bw
        image = pygame.image.load(os.path.join("Assets", "Data", "LOAD.png"))
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        while load < 61:
            load += 1
            clock.tick(60)
            w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
            if xo > bw // 8:
                xo = 6 * bw - int(load / 5 * (6 * bw // 12))
            pygame.draw.rect(w, (255, 255, 255),
                             (wd // 2 - 3 * bw - bw // 8, 2 * hg // 5 - bw // 8, 6 * bw + bw // 4, bw + bw // 4), 2,
                             bw // 8)
            pygame.draw.rect(w, (255, 255, 255), (wd // 2 - 3 * bw, 2 * hg // 5, 6 * bw - xo, bw))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(hg / 25))
            if load % 9 <= 2:
                text = font.render(("LOADING."), True, (255, 255, 255))
            elif load % 9 <= 5:
                text = font.render(("LOADING.."), True, (255, 255, 255))
            else:
                text = font.render(("LOADING..."), True, (255, 255, 255))
            trex = text.get_rect()
            trex.midleft = (wd // 2 - 2 * bw + bw // 2, 2 * hg // 5 + bw + hg // 20)
            w.blit(text, trex)
            pygame.display.update()

    if es==1:
        resetg=1
        load = 0
        xo = 6 * bw
        image = pygame.image.load(os.path.join("Assets", "Data", "LOAD2.png"))
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        while load < 61:
            load += 1
            clock.tick(60)
            w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
            if xo >=0:
                xo = 6 * bw - int(load / 5 * (6 * bw // 12))-5
            pygame.draw.rect(w, (255, 255, 255),
                             (wd // 2 - 3 * bw - bw // 8, 2 * hg // 5 - bw // 8, 6 * bw + bw // 4, bw + bw // 4), 2,
                             bw // 8)
            pygame.draw.rect(w, (255, 255, 255), (wd // 2 - 3 * bw, 2 * hg // 5, 6 * bw - xo, bw))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(hg / 25))
            if load  <= 20:
                text = font.render(("ENDING BACKGROUD PROCESSES"), True, (255, 255, 255))
            elif load  <= 40:
                text = font.render(("CLOSING GAME ENGINE"), True, (255, 255, 255))
            else:
                text = font.render(("THANK YOU FOR PLAYING"), True, (255, 255, 255))
            trex = text.get_rect()
            trex.center = (wd // 2, 2 * hg // 5 + bw + hg // 20)
            w.blit(text, trex)
            pygame.display.update()
    if Music_Settings!=0:
        BGM_Game_Playing.stop()
        BGM_Game_Playing2.stop()

    if endmusicclock == 1:
        SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "go.wav"))
        if SFX_Settings == 1:
            SFX.play()
        while (endmusicclock < 4):
            clock.tick(1)
            endmusicclock += 1
    BGM_End_Screen = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "endth.ogg"))
    if Music_Settings!=0:
        BGM_End_Screen.play(loops=-1)
    disp = ""   
    clc = 0
    tsk=0
    r=84
    g=54
    b=55
    rm=0
    bm=0
    gm=0


    
    if es!=0:
        run=True
    while (run == False):


        Mouse_Loc = pygame.mouse.get_pos()
        clock.tick(FPS)
        clc += 1
        if clc < 60 and tsk%(FPS//10)==0:
            disp = "mv (" + str(clc) + ").jpg"
        elif clc>60:
            clc = 0
        if tsk<FPS+1:
            tsk+=1
        else:
            tsk=0
        pygame.draw.rect(w, BGCOLOR, (0, 0, wd, hg))
        image = pygame.image.load(os.path.join("Assets", "End", disp))
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        font = pygame.font.Font('freesansbold.ttf', int(hg/22.5))

        pygame.draw.rect(w, BGCOLOR, (0, 0, wd, hg))
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        font = pygame.font.Font('freesansbold.ttf', bw)


        if nhs==1:
            nhscolor = (r, g, b)
            if r==84:
                rm=1
            if r==0:
                rm=0
            if g==84:
                gm=1
            if g==0:
                gm=0
            if b==84:
                bm=1
            if b==0:
                bm=0
            if rm==1:
                r-=1
            else:
                r+=1
            if gm==1:
                g-=1
            else:
                g+=1
            if bm==1:
                b-=1
            else:
                b+=1
            
            pygame.draw.rect(w, (88, 112, 115), (wd // 8, hg // 2 - hg // 3 - 15 * bw // 12, wd // 16, hg // 16))

            font = pygame.font.Font('freesansbold.ttf', hg // 60)
            text = font.render('NEW', True, (nhscolor))
            trex = text.get_rect()
            trex.center = (wd // 8 + wd // 31, hg // 32 + hg // 2 - hg // 3 - 15 * bw // 12 - hg // 50)
            w.blit(text, trex)
            text = font.render('HIGH', True, (nhscolor))
            trex = text.get_rect()
            trex.center = (wd // 8 + wd // 31, hg // 32 + hg // 2 - hg // 3 - 15 * bw // 12)
            w.blit(text, trex)
            text = font.render('SCORE', True, (nhscolor))
            trex = text.get_rect()
            trex.center = (wd // 8 + wd // 31, hg // 32 + hg // 2 - hg // 3 - 15 * bw // 12 + hg // 50)
            w.blit(text, trex)
        font = pygame.font.Font('freesansbold.ttf', int(hg / 22.5))
        text = font.render('    Score:    ', True, (24, 42, 50))
        trex = text.get_rect()
        trex.center = (wd//2, 3 * hg //11 -bw//6)
        w.blit(text, trex)
        text = font.render(str(Score), True, (24, 42, 50))
        trex = text.get_rect()
        trex.center = (wd//2, 3*hg // 11 +int(hg / 16)-bw//6)
        w.blit(text, trex)
        font = pygame.font.Font('freesansbold.ttf', 6 * bw // 10)
        pygame.draw.rect(w, (70, 58, 58), ((bw / 2), (bw / 2), 3 * bw // 4, 3 * bw // 4), bw // 2, int(bw / 4))
        text = font.render('<', True, (103, 147, 160))
        trex = text.get_rect()
        trex.center = (7 * bw // 8, 13 * bw // 16)
        w.blit(text, trex)
        pygame.draw.rect(w, (115, 149, 151), ((wd // 2 + wd // 17), (5 * hg // 7), 3 * bw, bw), bw // 2, int(bw / 4))
        pygame.draw.rect(w, (115, 149, 151),(int(wd // 2 + wd // 17 + 0.1 * bw), (501 * hg // 700), int(2.7 * bw), 9 * bw // 10))
        pygame.draw.rect(w, (115, 149, 151), ((wd // 2 - wd // 17 - 3 * bw), (5 * hg // 7), 3 * bw, bw), bw // 2,int(bw / 4))
        pygame.draw.rect(w, (115, 149, 151), (int(wd // 2 - wd // 17 - 0.1 * bw - int(2.7 * bw)), (501 * hg // 700), int(2.7 * bw), 9 * bw // 10))
        text = font.render('   Restart', True, (34, 50, 56))
        trex = text.get_rect()
        trex.topleft = (wd // 2 + wd // 17 - bw // 35, 5 * hg // 7 + bw // 5)
        w.blit(text, trex)
        text = font.render('Menu  ', True, (34, 50, 56))
        trex = text.get_rect()
        trex.topright = (wd // 2 - wd // 16 - bw // 5, 5 * hg // 7 + bw // 5)
        w.blit(text, trex)
        if bw // 2 < Mouse_Loc[1] < bw // 2 + 3 * bw // 4 and bw // 2 < Mouse_Loc[0] < bw // 2 + 3 * bw // 4 and click == 1:
            run=True
            es=1

        if click==1:
            click=0
            if 5 * hg // 7 < Mouse_Loc[1] < 5 * hg // 7 + 9 * bw // 10:
                if int(wd // 2 + wd // 17) < Mouse_Loc[0] < int(wd // 2 + wd // 17) + 3 * bw:
                    run = True
                    es=2

                elif (wd // 2 - wd // 17 - 3 * bw) < Mouse_Loc[0] < (wd // 2 - wd // 17 - 3 * bw) + 3 * bw:
                    run=True
                    es=3

        pygame.display.update()
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                run = True
                es=1
            if keypress[pygame.K_p]:
                run = True             
                es=2
            if event.type==pygame.MOUSEBUTTONUP:
                click=1
    if Music_Settings!=0:
        BGM_End_Screen.set_volume(0)
    if (es==3 or es==2) and resetg==0 :
        load = 0
        xo = 6 * bw
        image = pygame.image.load(os.path.join("Assets", "Data", "LOAD.png"))
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        while load < 61:
            load += 1
            clock.tick(60)
            w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
            if xo > bw // 8:
                xo = 6 * bw - int(load / 5 * (6 * bw // 12))
            pygame.draw.rect(w, (255, 255, 255),
                             (wd // 2 - 3 * bw - bw // 8, 2 * hg // 5 - bw // 8, 6 * bw + bw // 4, bw + bw // 4), 2,
                             bw // 8)
            pygame.draw.rect(w, (255, 255, 255), (wd // 2 - 3 * bw, 2 * hg // 5, 6 * bw - xo, bw))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(hg / 25))
            if load % 9 <= 2:
                text = font.render(("LOADING."), True, (255, 255, 255))
            elif load % 9 <= 5:
                text = font.render(("LOADING.."), True, (255, 255, 255))
            else:
                text = font.render(("LOADING..."), True, (255, 255, 255))
            trex = text.get_rect()
            trex.midleft = (wd // 2 - 2 * bw + bw // 2, 2 * hg // 5 + bw + hg // 20)
            w.blit(text, trex)
            pygame.display.update()

    if es==1 and resetg==0:
        load = 0
        xo = 6 * bw
        image = pygame.image.load(os.path.join("Assets", "Data", "LOAD2.png"))
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        while load < 61:
            load += 1
            clock.tick(60)
            w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
            if xo >=0:
                xo = 6 * bw - int(load / 5 * (6 * bw // 12))-5
            pygame.draw.rect(w, (255, 255, 255),
                             (wd // 2 - 3 * bw - bw // 8, 2 * hg // 5 - bw // 8, 6 * bw + bw // 4, bw + bw // 4), 2,
                             bw // 8)
            pygame.draw.rect(w, (255, 255, 255), (wd // 2 - 3 * bw, 2 * hg // 5, 6 * bw - xo, bw))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(hg / 25))
            if load  <= 20:
                text = font.render(("ENDING BACKGROUD PROCESSES"), True, (255, 255, 255))
            elif load  <= 40:
                text = font.render(("CLOSING GAME ENGINE"), True, (255, 255, 255))
            else:
                text = font.render(("THANK YOU FOR PLAYING"), True, (255, 255, 255))
            trex = text.get_rect()
            trex.center = (wd // 2, 2 * hg // 5 + bw + hg // 20)
            w.blit(text, trex)
            pygame.display.update()
    if Music_Settings!=0:
        BGM_End_Screen.stop()


    return(es)    
Legal_Screen()
while(esc!=1):
    if esc==3 or esc==4:
        esc=Main_Menu()
    if esc!=1:
        esc=main()
pygame.quit()