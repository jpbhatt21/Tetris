import math
import os
import pygame
from random import randint
hg=990
wd=int(hg/9 *16)
bw=hg//18
w = pygame.display.set_mode((wd, hg))
BGCOLOR = (20, 30, 40)
def Main_Menu():
    # Input
    pygame.init()
    base_font = pygame.font.Font(os.path.join("Assets" , "Fonts", "MAGNETOB.ttf"), int(hg//24))
    Name_Editor = ''

    # create rectangle

    # color_active stores color(lightskyblue3) which
    # gets active when input box is clicked by user
    color_active = pygame.Color('lightskyblue3')

    # color_passive store color(chartreuse4) which is
    # color of input box.
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
    H_P= (L[5]).rstrip()
    doc.close()
    settings_color= (150, 150, 200)
    clock = pygame.time.Clock()
    run=True
    pygame.init()
    disp = ""
    clc=0
    qt=True
    Block_1_Height=hg//2
    Block_2_Y_Loc= hg // 2
    Block_Width = wd
    r=120
    g=50
    b=200
    rp=1
    bp=1
    gp=1
    xdiff=0
    ydiff=0
    Click=0
    d_x=int(wd*1.015625)
    d_color=(0,0,82)
    dx2= wd - 7 // 4 * bw  +0.125*wd
    dx3= wd*1.06
    pau=0
    pygame.init()
    Trigger=0
    BGM_Main_Screen = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "M-m.wav"))
    if Music_Settings!=0:
        BGM_Main_Screen.play(loops=-1)
    Text_1_Color=(r,g, b)
    while(run):


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
        clock.tick(15)
        clc += 1
        if clc < 126:
            disp = "mv (" + str(clc) + ").jpg"
        else:
            clc = 0
        if Block_1_Height >0:
            Block_1_Height-=10
        if Block_2_Y_Loc <hg:
            Block_2_Y_Loc+=10
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
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "STENCIL.ttf"), int(hg / 24))
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0] and Mouse_Loc[0] >=(wd-  7/4 *bw) and Mouse_Loc[0]<=wd-  3/4 *bw and Mouse_Loc[1] >=3/4 *bw and Mouse_Loc[1]<=7/4 *bw and pau==15:
            pau = 0
            if Click == 0:
                Click = 1
            else:
                Click = 0
        image = pygame.image.load(os.path.join("Assets", "Main Menu", "Settings.png"))
        
        w.blit(pygame.transform.scale(image,(int(bw), int(bw))), (int(wd-  7/4 *bw), int(3/4 *bw)))
        
        pygame.draw.rect( w, d_color, (d_x, 0, int( wd/2),hg))
        
        text = font.render(">", True, (150, 150, 200))
        
        trex = text.get_rect()
        
        trex.topleft = ((dx2, 3 / 4 * bw))
        
        w.blit(text, trex)
        
        #FPS
        
        text = font.render("FPS:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = ((dx3, 2 / 5 * hg))
        w.blit(text, trex)

        text = font.render("PLayer Name:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = ((dx3, 1/7 * hg))
        w.blit(text, trex)

        input_rect = pygame.Rect(dx3 -0.005*wd, 1/7 * hg + int(hg / 24) , 0.777*hg,int(hg/20) )

        #Music
        pygame.draw.rect(w, d_color, (dx3 +0.095*wd, 3/5*hg- int(hg/40), 1.6*bw, int(hg/24))) #off
        if mouse_presses[0] and Mouse_Loc[0] >=dx3 +0.095*wd and Mouse_Loc[0]<=dx3 +0.095*wd +1.6*bw and Mouse_Loc[1] >=3/5*hg- int(hg/40) and Mouse_Loc[1]<=3/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            Trigger=2
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings=0
            L[2]="0\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.178 * wd, 3 / 5 * hg - int(hg / 40), 4 * bw, int(hg / 24))) #Mordern
        if mouse_presses[0] and Mouse_Loc[0] >=dx3 +0.178*wd and Mouse_Loc[0]<=dx3 +0.178*wd +4*bw and Mouse_Loc[1] >=3/5*hg- int(hg/40) and Mouse_Loc[1]<=3/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            if Music_Settings==0:
                Trigger=1
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings=1
            L[2]="1\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.3175 * wd, 3 / 5 * hg - int(hg / 40), 2.8 * bw, int(hg / 24)))  # Retro
        if mouse_presses[0] and Mouse_Loc[0] >=dx3 +0.3175*wd and Mouse_Loc[0]<=dx3 +0.3175*wd +2.8*bw and Mouse_Loc[1] >=3/5*hg- int(hg/40) and Mouse_Loc[1]<=3/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            if Music_Settings==0:
                Trigger=1
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings=2
            L[2]="2\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.174 * wd, 3.4 / 5 * hg - int(hg / 40), 4.3 * bw, int(hg / 24))) #Random
        if mouse_presses[0] and Mouse_Loc[0] >=dx3 +0.174*wd and Mouse_Loc[0]<=dx3 +0.174*wd +4.3*bw and Mouse_Loc[1] >=3.4/5*hg- int(hg/40) and Mouse_Loc[1]<=3.4/5*hg- int(hg/40 - hg/24)  and pau==15:
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
        #SFX
        text = font.render("SFX:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = ((dx3, 4.2 / 5 * hg))
        w.blit(text, trex)
        pygame.draw.rect(w, d_color, (dx3 + 0.155 * wd, 4.2 / 5 * hg - int(hg / 40), 1.6 * bw, int(hg / 24)))  # on
        if mouse_presses[0] and Mouse_Loc[0] >=dx3 +0.155*wd and Mouse_Loc[0]<=dx3 +0.155*wd +1.6*bw and Mouse_Loc[1] >=4.2/5*hg- int(hg/40) and Mouse_Loc[1]<=4.2/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            SFX_Settings=1
            L[3]="1\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.285 * wd, 4.2 / 5 * hg - int(hg / 40), 1.6 * bw, int(hg / 24)))  # off
        if mouse_presses[0] and Mouse_Loc[0] >= dx3 + 0.285 * wd and Mouse_Loc[0] <= dx3 + 0.285 * wd + 1.6 * bw and Mouse_Loc[1] >= 4.2 / 5 * hg - int(hg / 40) and Mouse_Loc[1] <= 4.2 / 5 * hg - int(hg / 40 - hg / 24) and pau == 15:
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
        pygame.draw.rect(w, d_color, (dx3 + 0.095 * wd, 2 / 5 * hg - int(hg / 40), 1.6 * bw, int(hg / 24)))  # 30
        if mouse_presses[0] and Mouse_Loc[0] >=dx3 +0.095*wd and Mouse_Loc[0]<=dx3 +0.095*wd +1.6*bw and Mouse_Loc[1] >=2/5*hg- int(hg/40) and Mouse_Loc[1]<=2/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            FPS_Settings=0
            L[1]="0\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.215 * wd, 2 / 5 * hg - int(hg / 40), 1.6 * bw, int(hg / 24))) #60
        if mouse_presses[0] and Mouse_Loc[0] >=dx3 +0.215*wd and Mouse_Loc[0]<=dx3 +0.215*wd +1.6*bw and Mouse_Loc[1] >=2/5*hg- int(hg/40) and Mouse_Loc[1]<=2/5*hg- int(hg/40 - hg/24)  and pau==15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            FPS_Settings=1
            L[1]="1\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.335 * wd, 2 / 5 * hg - int(hg / 40), 1.6 * bw, int(hg / 24)))  # 120
        if mouse_presses[0] and Mouse_Loc[0] >=dx3 +0.335*wd and Mouse_Loc[0]<=dx3 +0.335*wd +1.6*bw and Mouse_Loc[1] >=2/5*hg- int(hg/40) and Mouse_Loc[1]<=2/5*hg- int(hg/40 - hg/24)  and pau==15:
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
            color = (10,10,100)
        elif pau==15:
            color = color_passive
        elif active==True:
            color= (255,0,0)

        # draw rectangle and argument passed which should
        # be on screen
        pygame.draw.rect(w, color, input_rect)

        text_surface = base_font.render(Name_Editor, True, (200, 100, 100))

        # render at position stated in arguments
        w.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))

        # set width of textfield so that text cannot get
        # outside of user's text input
        input_rect.w = max(100, int(hg/20))




        pygame.draw.rect(w, (0, 0, 0), (0, 0, Block_Width, Block_1_Height))
        pygame.draw.rect(w, (0, 0, 0), (0, Block_2_Y_Loc, Block_Width, Block_1_Height))

        font = pygame.font.Font(os.path.join("Assets", "Fonts", "MAGNETOB.ttf"), int(hg / 25))
        text = font.render(("By: Jatan Bhatt"), True, Text_1_Color)
        trex = text.get_rect()
        trex.center = (18.7 * wd / 21, Block_2_Y_Loc + int(hg/25))
        w.blit(text, trex)
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "STENCIL.ttf"), int(hg / 25))
        text = font.render(("ver-1.7"), True, (settings_color))
        trex = text.get_rect()
        trex.center = (1 * wd / 21, Block_1_Height - int(hg / 25))
        w.blit(text, trex)
        if Click==0:
            if(d_x < int(wd + 20)):
                d_x+=75
                dx2+=20
                dx3+=80
        if Click == 1:
            if (d_x > 103*wd/180 ):
                d_x -=75
                dx2-=20
                dx3-=80
        if pau!=15:
            pau+=1
        pygame.display.update()
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP:
                if Mouse_Loc[0] >= dx3 + wd*0.1 and Mouse_Loc[1]<=1/7 * hg + int(hg / 24 + hg/20) and Mouse_Loc[1]>=1/7 * hg + int(hg / 24):
                    active = True
                else:
                    active = False

            if event.type == pygame.MOUSEBUTTONUP:
                if Mouse_Loc[0] >0 and Mouse_Loc[0] <wd/2 and Mouse_Loc[1]<hg and active==False:
                    run=False
            if keypress[pygame.K_SPACE] and active==False:
                run = False
            if event.type == pygame.KEYDOWN and active ==True:

                # Check for backspace
                if event.key == pygame.K_BACKSPACE:

                    # get text input from 0 to -1 i.e. end.
                    Name_Editor = Name_Editor[:-1]

                # Unicode standard is used for string
                # formation
                elif (event.key !=pygame.K_ESCAPE):
                    if (len(Name_Editor))<=24:
                        Name_Editor += event.unicode
                    else:
                        pau=0
    BGM_Main_Screen.stop()
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
    Name = (L[0]).rstrip()
    FPS_Settings = int((L[1]).rstrip())
    Music_Settings = int((L[2]).rstrip())
    SFX_Settings = int((L[3]).rstrip())
    High_Score = int((L[4]).rstrip())
    doc.close()
    run = True
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
    play = 0
    Score = 0
    TA=0
    TD=0
    TS=0
    TW=0
    TP=0
    TR=0
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
    #Shape Randomizer
    Current_Shape_Randomizer = randint(1, 7)
    Next_Shape_Randomizer = randint(1, 7)
    if Next_Shape_Randomizer==1:
        Next_Shape_Color= (255,131,112)
    elif Next_Shape_Randomizer==2:
        Next_Shape_Color= (162,242,189)
    elif Next_Shape_Randomizer==3:
        Next_Shape_Color= (255,229,112)
    elif Next_Shape_Randomizer==4:
        Next_Shape_Color= (182,194,245)
    elif Next_Shape_Randomizer==5:
        Next_Shape_Color= (211,150,237)
    elif Next_Shape_Randomizer==6:
        Next_Shape_Color= (255,171,92)
    elif Next_Shape_Randomizer==7:
        Next_Shape_Color= (153,216,255)


    if Music_Settings==3:
        if randint(0, 1) == 0:
            BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm.ogg"))
        else:
            BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm2.ogg"))
    elif Music_Settings==1:
        BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm2.ogg"))
    elif Music_Settings==2:
        BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm.ogg"))
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
    i = 0
    ng = 0
    Score=0
    T1 = 1
    modder=0
    clc=1
    Block_Grid_Color=(0,0,0)
    disp=""
    ticker=0
    while (run):
        clock.tick(FPS)
        Mouse_Loc = pygame.mouse.get_pos()
        if play==0 and Music_Settings!=0:
            BGM_Game_Playing.play(loops=-1)
            play=1
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
        x = 0
        Vert_Movement_Clock += 1 + ((Score//5000)/5)
        BGC_Grid_Color_Matcher = 0
        ng = (Block_X_No * Block_Y_No) - 1
        Instantaneous_Block_No = 0
        Instant_Row_Completion_No = 0
        Row_Deletion_Start_Block_No = 0
        if Spawn_New_Block == 1:
            if Score//1000 - modder//1000 !=0:
                T1=1
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
                if Block_Grid_Color_Boolean[(Current_Shape[0] + Block_X_No )] != 0 or Block_Grid_Color_Boolean[
                    (Current_Shape[1] + Block_X_No )] != 0 or Block_Grid_Color_Boolean[(Current_Shape[2] + Block_X_No )] != 0 or \
                        Block_Grid_Color_Boolean[(Current_Shape[3] + Block_X_No )] != 0:
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
                if Instant_Row_Completion_No == 4 and Row_Deletion_Start_Block_No <= 39:
                    Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = 0
                elif Instant_Row_Completion_No == 3 and Row_Deletion_Start_Block_No <= 29:
                    Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = 0
                elif Instant_Row_Completion_No == 2 and Row_Deletion_Start_Block_No <= 19:
                    Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = 0
                elif Instant_Row_Completion_No == 1 and Row_Deletion_Start_Block_No <= 9:
                    Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = 0
                elif Instant_Row_Completion_No == 4:
                    Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = Block_Grid_Color_Boolean[
                    (Row_Deletion_Start_Block_No - 40)]
                elif Instant_Row_Completion_No == 3:
                    Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = Block_Grid_Color_Boolean[
                    (Row_Deletion_Start_Block_No - 30)]
                elif Instant_Row_Completion_No == 2:
                    Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = Block_Grid_Color_Boolean[
                    (Row_Deletion_Start_Block_No - 20)]
                elif Instant_Row_Completion_No == 1:
                    Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No)] = Block_Grid_Color_Boolean[
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
                elif (Stop_Current_Shape_Movement != 0 and Block_Grid_Color_Boolean[(Current_Shape[0])] != 0 and
                      Block_Grid_Color_Boolean[(Current_Shape[1])] != 0 and Block_Grid_Color_Boolean[
                          (Current_Shape[2])] != 0 and Block_Grid_Color_Boolean[
                          (Current_Shape[3])] != 0):
                    pygame.draw.rect(w, Block_Grid_Free_Color, ((Block_Grid_X[(j)]), Block_Grid_Y[(lm - 1)], bw, bw),
                                     int(bw / 40), int(bw / 8))
                    pygame.draw.rect(w, Block_Grid_Red,((Block_Grid_X[(j)]) + int(bw/20), Block_Grid_Y[(lm - 1)]+int(bw/20), int(9*bw/10), int(9*bw/10)),20*int(bw/40),int(bw/8))
                elif ((Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] != 0)):

                    if Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 1:
                        Block_Grid_Color = (255, 131, 112)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 2:
                        Block_Grid_Color = (162, 242, 189)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 3:
                        Block_Grid_Color = (255, 229, 112)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 4:
                        Block_Grid_Color = (182, 194, 245)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 5:
                        Block_Grid_Color = (211, 150, 237)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 6:
                        Block_Grid_Color = (255, 171, 92)
                    elif Block_Grid_Color_Boolean[(BGC_Grid_Color_Matcher)] == 7:
                        Block_Grid_Color = (153, 216, 255)

                    pygame.draw.rect(w, Block_Grid_Free_Color, ((Block_Grid_X[(j)]), Block_Grid_Y[(lm - 1)], bw, bw),
                                     int(bw / 40), int(bw / 8))
                    pygame.draw.rect(w, Block_Grid_Color,((Block_Grid_X[(j)]) + int(bw/20), Block_Grid_Y[(lm - 1)]+int(bw/20), int(9*bw/10), int(9*bw/10)),25*int(bw/40),int(bw/8))
                j += 1
                BGC_Grid_Color_Matcher += 1
        if (Spawn_New_Block == 1):
            Current_Shape_Randomizer = Next_Shape_Randomizer
            Next_Shape_Randomizer = randint(1, 7)
            
            Stop_Current_Shape_Movement = 0
            Rotaion_Status = 0
            Current_Shape_Color = Next_Shape_Color
            if Next_Shape_Randomizer == 1:
                Next_Shape_Color = (255, 131, 112)
            elif Next_Shape_Randomizer == 2:
                Next_Shape_Color = (162, 242, 189)
            elif Next_Shape_Randomizer == 3:
                Next_Shape_Color = (255, 229, 112)
            elif Next_Shape_Randomizer == 4:
                Next_Shape_Color = (182, 194, 245)
            elif Next_Shape_Randomizer == 5:
                Next_Shape_Color = (211, 150, 237)
            elif Next_Shape_Randomizer == 6:
                Next_Shape_Color = (255, 171, 92)
            elif Next_Shape_Randomizer == 7:
                Next_Shape_Color = (153, 216, 255)
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
        if Rotation_Clock == Rotation_Frequency and (keypress[pygame.K_RIGHT]or TR==1):
            TR=0
            Rotation_Mananger_Boolean = 0
            Rotation_Clock = 0
        if Rotation_Mananger_Boolean == 0:
            Rotation_Mananger_Boolean = 1
            SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "rot.wav"))
            if SFX_Settings==1:
                SFX.play()
            if Rotation_Shape == 1:
                if Rotaion_Status == 0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 11
                    Current_Shape[2] -= 11
                    Current_Shape[3] -= 22
                elif Rotaion_Status == 1:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] += 11
                    Current_Shape[3] += 22
                Rotation_Shape = 1
            if Rotation_Shape == 3:
                if Rotaion_Status == 0:
                    Rotaion_Status = 1
                    Current_Shape[0] -= 9
                    Current_Shape[2] += 9
                    Current_Shape[3] -= 11
                elif Rotaion_Status == 1:
                    Rotaion_Status = 2
                    Current_Shape[0] += 11
                    Current_Shape[2] -= 11
                    Current_Shape[3] -= 9
                elif Rotaion_Status == 2:
                    Rotaion_Status = 3
                    Current_Shape[0] += 9
                    Current_Shape[2] -= 9
                    Current_Shape[3] += 11
                elif Rotaion_Status == 3:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] += 11
                    Current_Shape[3] += 9
            if Rotation_Shape == 4:
                if Rotaion_Status == 0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 2
                    Current_Shape[1] -= 9
                    Current_Shape[3] += 9
                elif Rotaion_Status == 1:
                    Rotaion_Status = 2
                    Current_Shape[0] += 20
                    Current_Shape[1] += 11
                    Current_Shape[3] -= 11
                elif Rotaion_Status == 2:
                    Rotaion_Status = 3
                    Current_Shape[0] -= 2
                    Current_Shape[1] += 9
                    Current_Shape[3] -= 9
                elif Rotaion_Status == 3:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 20
                    Current_Shape[1] -= 11
                    Current_Shape[3] += 11
            if Rotation_Shape == 5:
                if Rotaion_Status == 0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 20
                    Current_Shape[1] += 9
                    Current_Shape[3] -= 9
                elif Rotaion_Status == 1:
                    Rotaion_Status = 2
                    Current_Shape[0] -= 2
                    Current_Shape[1] -= 11
                    Current_Shape[3] += 11
                elif Rotaion_Status == 2:
                    Rotaion_Status = 3
                    Current_Shape[0] -= 20
                    Current_Shape[1] -= 9
                    Current_Shape[3] += 9
                elif Rotaion_Status == 3:
                    Rotaion_Status = 0
                    Current_Shape[0] += 2
                    Current_Shape[1] += 11
                    Current_Shape[3] -= 11
            if Rotation_Shape == 6:
                if Rotaion_Status == 0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 11
                    Current_Shape[2] += 9
                    Current_Shape[3] -= 2
                elif Rotaion_Status == 1:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] -= 9
                    Current_Shape[3] += 2
            if Rotation_Shape == 7:
                if Rotaion_Status == 0:
                    Rotaion_Status = 1
                    Current_Shape[0] += 11
                    Current_Shape[2] -= 9
                    Current_Shape[3] -= 20
                elif Rotaion_Status == 1:
                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] += 9
                    Current_Shape[3] += 20
        if (Stop_Current_Shape_Movement == 0 and Block_Grid_Color_Boolean[(Current_Shape[0])] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1])] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2])] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3])] == 0):
            ng = Current_Shape[0]
            x3 = convx(Current_Shape_Display_Grid[(ng)])
            y3 = convy(Current_Shape_Display_Grid[(ng)])
            
            pygame.draw.rect(w, Current_Shape_Color, (Block_Grid_X[(x3)]+bw/20, Block_Grid_Y[(y3)]+bw/20, int(9*bw/10), int(9*bw/10)) ,25*int(bw/40),int(bw/8) )
            ng = Current_Shape[1]
            x3 = convx(Current_Shape_Display_Grid[(ng)])
            y3 = convy(Current_Shape_Display_Grid[(ng)])
            
            pygame.draw.rect(w, Current_Shape_Color, (Block_Grid_X[(x3)]+bw/20, Block_Grid_Y[(y3)]+bw/20, int(9*bw/10), int(9*bw/10)) ,25*int(bw/40),int(bw/8) )
            ng = Current_Shape[2]
            x3 = convx(Current_Shape_Display_Grid[(ng)])
            y3 = convy(Current_Shape_Display_Grid[(ng)])
            
            pygame.draw.rect(w, Current_Shape_Color, (Block_Grid_X[(x3)]+bw/20, Block_Grid_Y[(y3)]+bw/20, int(9*bw/10), int(9*bw/10)) ,25*int(bw/40),int(bw/8) )
            ng = Current_Shape[3]
            x3 = convx(Current_Shape_Display_Grid[(ng)])
            y3 = convy(Current_Shape_Display_Grid[(ng)])
            
            pygame.draw.rect(w, Current_Shape_Color, (Block_Grid_X[(x3)]+bw/20, Block_Grid_Y[(y3)]+bw/20, int(9*bw/10), int(9*bw/10)) ,25*int(bw/40),int(bw/8) )
        if (Stop_Current_Shape_Movement == 0 ):
            ng = Next_Shape[0]
            x3 = math.floor(int(Next_Shape_Display_Grid[ng]/10000))
            y3 = Next_Shape_Display_Grid[ng]%10000
            pygame.draw.rect(w, Next_Shape_Color, (x3 + bw/20, y3+bw/20, int(9*bw/10), int(9*bw/10)),25*int(bw/40),int(bw/8))
            ng = Next_Shape[1]
            x3 = math.floor(int(Next_Shape_Display_Grid[ng] / 10000))
            y3 = Next_Shape_Display_Grid[ng] % 10000
            pygame.draw.rect(w, Next_Shape_Color, (x3 + bw/20, y3+bw/20, int(9*bw/10), int(9*bw/10)),25*int(bw/40),int(bw/8))
            ng = Next_Shape[2]
            x3 = math.floor(int(Next_Shape_Display_Grid[ng] / 10000))
            y3 = Next_Shape_Display_Grid[ng] % 10000
            pygame.draw.rect(w, Next_Shape_Color, (x3 + bw/20, y3+bw/20, int(9*bw/10), int(9*bw/10)),25*int(bw/40),int(bw/8))
            ng = Next_Shape[3]
            x3 = math.floor(int(Next_Shape_Display_Grid[ng] / 10000))
            y3 = Next_Shape_Display_Grid[ng] % 10000
            pygame.draw.rect(w, Next_Shape_Color, (x3 + bw/20, y3+bw/20, int(9*bw/10), int(9*bw/10)),25*int(bw/40),int(bw/8))
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
        text = font.render('    Score:    ', True, (255, 150, 120))
        trex = text.get_rect()
        trex.center = (int(((15+Block_X_No+ 2.1) * bw)), int(0.475 * hg))
        w.blit(text, trex)
        text = font.render(str(Score), True, (255, 150, 120))
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
        if (keypress[pygame.K_SPACE] or TP==1):
            pause = 1
            disp = ""
            clc = 0
            TP=0
            BGM_Game_Playing.fadeout(2)
            SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "pause.wav"))
            if SFX_Settings==1:
                SFX.play()
            BGM_Paused = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "paused.wav"))
            click=0
            spaceb=0
            if Music_Settings!=0:
                BGM_Paused.play(loops=-1)
            while (pause == 1):
                Mouse_Loc = pygame.mouse.get_pos()
                clock.tick(10)
                clc += 1
                if clc==11:
                	spaceb=1
                if clc < 129:
                    disp = "mv (" + str(clc) + ").jpg"
                else:
                    clc = 0
                pygame.draw.rect(w, BGCOLOR, (0, 0, wd, hg))
                image = pygame.image.load(os.path.join("Assets", "Pause", disp))
                w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
                font = pygame.font.Font('freesansbold.ttf', 32)
                text = font.render('    Score:    ', True, (255, 150, 120))
                trex = text.get_rect()
                trex.center = (wd / 2, hg/2 - 49 -13-4)
                w.blit(text, trex)
                text = font.render(str(Score), True, (255, 150, 120))
                trex = text.get_rect()
                trex.center = (wd / 2, hg/2 - 13 -13-4)
                w.blit(text, trex)
                text = font.render('    Press:    ', True, (255, 150, 120))
                trex = text.get_rect()
                trex.center = (wd / 2, hg/2 )
                w.blit(text, trex)
                text = font.render('    Shift - to Continue    ', True, (255, 150, 120))
                trex = text.get_rect()
                trex.center = (wd / 2, hg/2 + 13+13 +4 +2)
                w.blit(text, trex)
                text = font.render('    Escape - to Exit    ', True, (255, 150, 120))
                trex = text.get_rect()
                trex.center = (wd / 2, hg /2 + 49+13 +4 +2)
                if click==1:
                	click=0
                	if Mouse_Loc[1]<hg//7:
                		if Mouse_Loc[0]>wd//2 and Mouse_Loc[0]<wd:
                			run=True
                			pause=0
                			
                		else:
                			run=False
                			pause=0
                w.blit(text, trex)
                keypress = pygame.key.get_pressed()
                pygame.display.update()
                for event in pygame.event.get():
                    if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT :
                        run = False
                        pygame.quit()
                        pause = 0
                    if keypress[pygame.K_SPACE] and spaceb==1 :
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
            if Music_Settings!=0 and run==True:
                BGM_Game_Playing.play(loops=-1)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keypress[pygame.K_ESCAPE]:
                run = False
            if event.type==pygame.MOUSEBUTTONUP:
            	if Mouse_Loc[0]>wd//2 - (Block_X_No/2)*bw and Mouse_Loc[0]<wd//2 +(Block_X_No/2)*bw and Mouse_Loc[1]<hg:
            		TS=1
            	if Mouse_Loc[0]<wd//2 - (Block_X_No/2)*bw and Mouse_Loc[1]<hg:
            		if(Mouse_Loc[1]<hg//7):
            			run=False
            		elif(Mouse_Loc[1]<4* hg//7):
            			TW=1
            		elif (Mouse_Loc[0]<(wd//2 - Block_X_No*bw)/2):
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
    if Score > High_Score:
        doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
        L[4] = str(Score) + "\n"
        nhs = 1
        doc.writelines(L)
        doc.close()
    resetg = 0

    if Music_Settings!=0:
        BGM_Game_Playing.stop()
    
    SFX = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "go.wav"))
    if SFX_Settings==1:
        SFX.play()
    BGM_End_Screen = pygame.mixer.Sound(os.path.join("Assets" , "Music and SFX", "endth.wav"))
    
    if Music_Settings!=0:
        BGM_End_Screen.play(loops=-1)
    disp = ""
    
    clc = 0

    while (run == False):
        Mouse_Loc = pygame.mouse.get_pos()
        clock.tick(60)
        clc += 1
        if clc < 220:
            disp = "mv (" + str(clc) + ").jpg"
        else:
            clc = 0
        pygame.draw.rect(w, BGCOLOR, (0, 0, wd, hg))
        image = pygame.image.load(os.path.join("Assets", "End", disp))
        w.blit(pygame.transform.scale(image, (wd, hg)), (0, 0))
        font = pygame.font.Font('freesansbold.ttf', int(hg/22.5))
        if nhs==1:
            text = font.render('    NEW    ', True, (200, 150, 120))
            trex = text.get_rect()
            trex.center = (wd / 2, int(hg/2 - 4*hg/22.5 -hg/180))
            w.blit(text, trex)
            text = font.render('    High    ', True, (200, 150, 120))
            trex = text.get_rect()
            trex.center = (wd / 2, int(hg / 2 - 3 * hg / 22.5 - hg / 180))
            w.blit(text, trex)
        text = font.render('    Score:    ', True, (200, 150, 120))
        trex = text.get_rect()
        trex.center = (wd / 2, int(hg/2 - 2*hg/22.5 -hg/180))
        w.blit(text, trex)
        text = font.render(str(Score), True, (200, 150, 120))
        trex = text.get_rect()
        trex.center = (wd / 2, int(hg/2 - hg/22.5-hg/180))
        w.blit(text, trex)
        text = font.render('    Press:    ', True, (200, 150, 120))
        trex = text.get_rect()
        trex.center = (wd / 2, int(hg/2) )
        w.blit(text, trex)
        text = font.render('    Space - to Restart    ', True, (200, 150, 120))
        trex = text.get_rect()
        trex.center = (wd / 2, int(hg/2 + hg/22.5 +1.5*hg/180))
        w.blit(text, trex)
        text = font.render('    Escape - to Exit    ', True, (200, 150, 120))
        trex = text.get_rect()
        trex.center = (wd / 2, int(hg /2 + 2*hg/22.5 +1.5*hg/180))
        w.blit(text, trex)
        if click==1:
            click=0
            if Mouse_Loc[1]<hg//7:
                if Mouse_Loc[0]>wd//2 and Mouse_Loc[0]<wd:
                	run=True
                	resetg=1
                else:
                	run=True
        pygame.display.update()
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():
            if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:
                run = True
            if keypress[pygame.K_SPACE]:
                run = True
                resetg = 1
            if event.type==pygame.MOUSEBUTTONUP:
            	click=1
    BGM_End_Screen.stop()
    if resetg == 1:
        main()
    pygame.quit()
Main_Menu()
main()
