import os
import pygame
from random import randint
import math
import cv2

#initializing global variables
doc = open(os.path.join("Assets", "Data", "Variables.txt"), "r")
L = doc.readlines()
height = int((L[6]).rstrip())
width = int((L[7]).rstrip())
doc.close()
block_width = width // 32
block_height = height // 18
BGCOLOR = (20, 30, 40)
esc = 4
Mod_Access_Blocked = 1
First_Run = 1
comp = 1

#window
if width==0 or height==0:
    w=pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    x, y = w.get_size()
    height = y
    width = x
    block_width = width // 32
    block_height = height // 18
else:
    w = pygame.display.set_mode((width, height))

x, y = w.get_size()

#clock
clock = pygame.time.Clock()



def Main_Menu():
    pygame.init()

    global First_Run, width, block_height, height, w, block_width

    video = cv2.VideoCapture("Assets/Main Menu/MainStart.mp4")
    success, video_image = video.read()

    exit_sequence = 0
    New_Player = 0

    color_passive = (0, 0, 84)
    color = color_passive
    active = False

    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "r")
    L = doc.readlines()
    New_Check = int((L[5]).rstrip())
    doc.close()
    if New_Check == 0:
        New_Player = 1
        doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
        L[0] = "Player\n"
        L[1] = "1\n"
        L[2] = "3\n"
        L[3] = "1\n"
        L[4] = "0\n"
        L[5] = "0\n"
        doc.writelines(L)
        doc.close()

    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "r")
    L = doc.readlines()
    Name = (L[0]).rstrip()
    Name_Editor = Name
    FPS_Settings = int((L[1]).rstrip())
    Music_Settings = int((L[2]).rstrip())
    SFX_Settings = int((L[3]).rstrip())
    High_Score = int((L[4]).rstrip())
    doc.close()

    clock = pygame.time.Clock()
    if esc == 3:
        load = 55
        xo = 0
        Loading(load, xo)

    run = True
    pygame.init()
    disp = ""
    Image_No = 0
    conts = 0
    Block_1_Height = 0
    Block_2_Y_Loc = 0
    Block_Width = width

    r = 120
    g = 50
    b = 200
    rp = 1
    bp = 1
    gp = 1

    xc = -height
    xdiff = 0
    ydiff = 0
    cd = 0

    Click = 0
    d_x = int(width * 1.015625)
    d_color = (34, 46, 57)
    dx2 = width - 7 // 4 * block_width + 0.125 * width
    dx3 = width * 1.2
    pau = 0
    pygame.init()
    ml = 1
    Trigger = 0

    BGM_Main_Screen = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "M-m.wav"))
    if Music_Settings != 0:
        BGM_Main_Screen.play(loops=-1)

    while run:

        clock.tick(45)

        if Image_No % 1 == 0:
            success, video_image = video.read(1)
            if success:
                video_surf = pygame.image.frombuffer(
                    video_image.tobytes(), video_image.shape[1::-1], "BGR")
                w.blit(pygame.transform.smoothscale(video_surf, (width, height)), (0, 0))
            else:
                video = cv2.VideoCapture("Assets/Main Menu/Main.mp4")

        if conts == 1:
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            New_Player = 0
            L[5] = "1\n"
            doc.writelines(L)
            doc.close()
        if conts == 0 and xc > -height:
            xc -= block_height
        elif conts == 1 and 0>= xc >=-height:
            xc += block_height
        if conts == 0 and xc > -height:
            xc -= block_height
        elif conts == 1 and 0>= xc >=-height:
            xc += block_height
        if conts == 0 and xc > -height:
            xc -= block_height
        elif conts == 1 and 0>= xc >=-height:
            xc += block_height

        if Trigger == 1:
            pygame.init()
            BGM_Main_Screen = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "M-m.wav"))
            BGM_Main_Screen.play(loops=-1)
            Trigger = 0
        elif Trigger == 2:
            BGM_Main_Screen.stop()
            Trigger = 0

        Mouse_Loc = pygame.mouse.get_pos()

        Image_No += 1
        if Image_No > 1000:
            Image_No = 701

        if Block_1_Height > 0:
            Block_1_Height -= 20
        if Block_2_Y_Loc < height:
            Block_2_Y_Loc += 20

        #New Player attention color
        if r >= 250:
            rp = 0
        elif r <= 0:
            rp = 3
        if g >= 100:
            gp = 0
        elif g <= 0:
            gp = 3
        if b >= 200:
            bp = 0
        elif b <= 100:
            bp = 3
        if rp == 3:
            r += 10
        elif rp == 0:
            r -= 10
        if bp == 3:
            b += 10
        elif bp == 0:
            b -= 10
        if gp == 100:
            g += 10
        elif gp == 0:
            g -= 10

        if xdiff <= 0:
            ydiff = 0
        if xdiff >= 25:
            ydiff = 1
        if ydiff == 0:
            xdiff += 5
        elif ydiff == 1:
            xdiff -= 5

        Text_1_Color = (250, 250, 250)
        Text_3_Color = (r, g, b)

        #Displaying High Score
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "OpenSans-Medium.ttf"), int(height / 18))
        fpss = f'{clock.get_fps():.0f} FPS'
        text = font.render(str(High_Score), True, Text_1_Color)
        trex = text.get_rect()
        trex.center = (2 * width / 21, 5 * height / 9)
        if Image_No > 164:
            w.blit(text, trex)

        #Displaying Player Name
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height / 24))
        text = font.render(Name, True, (150, 150, 200))
        trex = text.get_rect()
        trex.midright = (width - 0.0624 * width, 14 / 16 * block_height)
        if Image_No > 164:
            w.blit(text, trex)

        if ml == 1 and Mouse_Loc[0] < width // 2:
            Click = 0

        font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height / 24))
        if ml == 1 and (width - 0.0547 * width) <= Mouse_Loc[0] <= width - 0.02344 * width and Mouse_Loc[1] <= 7 / 4 * block_height and pau == 15:
            pau = 0
            if Click == 0:
                Click = 1
            else:
                Click = 0

        if New_Player == 1 and Image_No > 164:
            pygame.draw.rect(w, Text_3_Color, (
                int(width // 10 - 11 / 4 * block_width - block_width // 4 - block_width // 16), int(1 / 8 * block_height), int(block_width * 1.45), int(block_height * 1.25)), 5,
                             block_height // 4)

        #Settings Menu
        pygame.draw.rect(w, d_color, (d_x, 0, int(width / 2), height))
        image = pygame.image.load(os.path.join("Assets", "Main Menu", "Back.png"))
        w.blit(pygame.transform.smoothscale(image, (int(block_width), int(block_height))), (dx2 - block_width // 2, 2 / 4 * block_height))

        text = font.render("FPS:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = (dx3, 2 / 5 * height)
        w.blit(text, trex)

        text = font.render("Player Name:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = (dx3, 1 / 7 * height)
        w.blit(text, trex)

        input_rect = pygame.Rect(dx3 - 0.005 * width, 1 / 7 * height + int(height / 24), 0.777 * height, int(height / 20))
        pygame.draw.rect(w, d_color, (dx3 + 0.095 * width, 3 / 5 * height - int(height / 40), 1.6 * block_width, int(height / 24)))

        if ml == 1 and dx3 + 0.095 * width <= Mouse_Loc[0] <= dx3 + 0.095 * width + 1.6 * block_width and 3 / 5 * height - int(height / 40) <= \
                Mouse_Loc[1] <= 3 / 5 * height - int(height / 40 - height / 24) and pau == 15:
            pau = 0
            Trigger = 2
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings = 0
            L[2] = "0\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.178 * width, 3 / 5 * height - int(height / 40), 4 * block_width, int(height / 24)))
        if ml == 1 and dx3 + 0.178 * width <= Mouse_Loc[0] <= dx3 + 0.178 * width + 4 * block_width and 3 / 5 * height - int(height / 40) <= \
                Mouse_Loc[1] <= 3 / 5 * height - int(height / 40 - height / 24) and pau == 15:
            pau = 0
            if Music_Settings == 0:
                Trigger = 1
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings = 1
            L[2] = "1\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.3175 * width, 3 / 5 * height - int(height / 40), 2.8 * block_width, int(height / 24)))
        if ml == 1 and dx3 + 0.3175 * width <= Mouse_Loc[0] <= dx3 + 0.3175 * width + 2.8 * block_width and 3 / 5 * height - int(
                height / 40) <= Mouse_Loc[1] <= 3 / 5 * height - int(height / 40 - height / 24) and pau == 15:
            pau = 0
            if Music_Settings == 0:
                Trigger = 1
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings = 2
            L[2] = "2\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.174 * width, 3.4 / 5 * height - int(height / 40), 4.3 * block_width, int(height / 24)))
        if ml == 1 and dx3 + 0.174 * width <= Mouse_Loc[0] <= dx3 + 0.174 * width + 4.3 * block_width and 3.4 / 5 * height - int(
                height / 40) <= Mouse_Loc[1] <= 3.4 / 5 * height - int(height / 40 - height / 24) and pau == 15:
            pau = 0
            if Music_Settings == 0:
                Trigger = 1
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            Music_Settings = 3
            L[2] = "3\n"
            doc.writelines(L)
            doc.close()
        text = font.render("Music:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = (dx3, 3 / 5 * height)
        w.blit(text, trex)
        if Music_Settings == 0:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("OFF", True, settings_color)
        trex = text.get_rect()
        trex.center = (dx3 + 0.12 * width, 3 / 5 * height)
        w.blit(text, trex)
        if Music_Settings == 1:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("Mordern", True, settings_color)
        trex = text.get_rect()
        trex.center = (dx3 + 0.24 * width, 3 / 5 * height)
        w.blit(text, trex)
        if Music_Settings == 2:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("Retro", True, settings_color)
        trex = text.get_rect()
        trex.center = (dx3 + 0.36 * width, 3 / 5 * height)
        w.blit(text, trex)
        if Music_Settings == 3:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("Randomize", True, settings_color)
        trex = text.get_rect()
        trex.center = (dx3 + 0.24 * width, 3.4 / 5 * height)
        w.blit(text, trex)
        text = font.render("SFX:", True, (150, 150, 200))
        trex = text.get_rect()
        trex.midleft = (dx3, 4.2 / 5 * height)
        w.blit(text, trex)
        pygame.draw.rect(w, d_color, (dx3 + 0.155 * width, 4.2 / 5 * height - int(height / 40), 1.6 * block_width, int(height / 24)))

        if ml == 1 and dx3 + 0.155 * width <= Mouse_Loc[0] <= dx3 + 0.155 * width + 1.6 * block_width and 4.2 / 5 * height - int(
                height / 40) <= Mouse_Loc[1] <= 4.2 / 5 * height - int(height / 40 - height / 24) and pau == 15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            SFX_Settings = 1
            L[3] = "1\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.285 * width, 4.2 / 5 * height - int(height / 40), 1.6 * block_width, int(height / 24)))
        if ml == 1 and dx3 + 0.285 * width <= Mouse_Loc[0] <= dx3 + 0.285 * width + 1.6 * block_width and 4.2 / 5 * height - int(
                height / 40) <= Mouse_Loc[1] <= 4.2 / 5 * height - int(height / 40 - height / 24) and pau == 15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            SFX_Settings = 0
            L[3] = "0\n"
            doc.writelines(L)
            doc.close()
        if SFX_Settings == 1:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("ON", True, settings_color)
        trex = text.get_rect()
        trex.center = (dx3 + 0.18 * width, 4.2 / 5 * height)
        w.blit(text, trex)
        if SFX_Settings == 0:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("OFF", True, settings_color)
        trex = text.get_rect()
        trex.center = (dx3 + 0.31 * width, 4.2 / 5 * height)
        w.blit(text, trex)
        if FPS_Settings == 0:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        pygame.draw.rect(w, d_color, (dx3 + 0.095 * width, 2 / 5 * height - int(height / 40), 1.6 * block_width, int(height / 24)))
        if ml == 1 and dx3 + 0.095 * width <= Mouse_Loc[0] <= dx3 + 0.095 * width + 1.6 * block_width and 2 / 5 * height - int(height / 40) <= \
                Mouse_Loc[1] <= 2 / 5 * height - int(height / 40 - height / 24) and pau == 15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            FPS_Settings = 0
            L[1] = "0\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.215 * width, 2 / 5 * height - int(height / 40), 1.6 * block_width, int(height / 24)))
        if ml == 1 and dx3 + 0.215 * width <= Mouse_Loc[0] <= dx3 + 0.215 * width + 1.6 * block_width and 2 / 5 * height - int(height / 40) <= \
                Mouse_Loc[1] <= 2 / 5 * height - int(height / 40 - height / 24) and pau == 15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            FPS_Settings = 1
            L[1] = "1\n"
            doc.writelines(L)
            doc.close()
        pygame.draw.rect(w, d_color, (dx3 + 0.335 * width, 2 / 5 * height - int(height / 40), 1.6 * block_width, int(height / 24)))
        if ml == 1 and dx3 + 0.335 * width <= Mouse_Loc[0] <= dx3 + 0.335 * width + 1.6 * block_width and 2 / 5 * height - int(height / 40) <= \
                Mouse_Loc[1] <= 2 / 5 * height - int(height / 40 - height / 24) and pau == 15:
            pau = 0
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            FPS_Settings = 2
            L[1] = "2\n"
            doc.writelines(L)
            doc.close()
        text = font.render("30", True, settings_color)
        trex = text.get_rect()
        trex.center = (dx3 + 0.12 * width, 2 / 5 * height)
        w.blit(text, trex)
        if FPS_Settings == 1:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("60", True, settings_color)
        trex = text.get_rect()
        trex.center = (dx3 + 0.24 * width, 2 / 5 * height)
        w.blit(text, trex)
        if FPS_Settings == 2:
            settings_color = (200, 100, 100)
        else:
            settings_color = (150, 150, 200)
        text = font.render("120", True, settings_color)
        trex = text.get_rect()
        trex.center = (dx3 + 0.36 * width, 2 / 5 * height)
        w.blit(text, trex)
        if Name != Name_Editor:
            doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
            L[0] = Name_Editor + "\n"
            Name = Name_Editor
            doc.writelines(L)
            doc.close()
        if active and pau % 5 == 0:
            color = (45, 60, 75)
        elif pau == 15:
            color = (34, 46, 57)
        elif active:
            color = (45, 60, 75)
        pygame.draw.rect(w, color, input_rect)
        text_surface = font.render(Name_Editor, True, (200, 100, 100))
        w.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(100, int(height / 20))


        if conts == 1 or conts == 0:
            pygame.draw.rect(w, d_color,(0 + width // 2 - 2 * width // 5, xc + height // 2 - 5.5 * height // 14, 4 * width // 5, 9.5 * height // 14))
            pygame.draw.rect(w, (235, 80, 78), (width // 2 - 3 * block_width + block_width // 2, xc + height * 2 / 3 - block_height // 2, 5 * block_width, block_height - block_height // 8))

            # ESC
            pygame.draw.rect(w, (235, 80, 78), (0.203 * width, xc + height // 6 + block_height // 2 - block_height // 40, width // 3 - 2 * block_width, block_height // 20))

            # W
            pygame.draw.rect(w, (235, 80, 78), (0.3085 * width, xc + height // 6 + 3 * block_height // 2, block_width // 20, 2 * block_height))
            pygame.draw.rect(w, (235, 80, 78), (0.3085 * width, xc + height // 6 + 3 * block_height // 2, 0.112 * width, block_height // 20))

            # D
            pygame.draw.rect(w, (235, 80, 78), (0.34 * width, xc + height // 6 + 5 * block_height // 2, block_width // 20, 4 * block_height // 2))
            pygame.draw.rect(w, (235, 80, 78), (0.34 * width, xc + height // 6 + 5 * block_height // 2, 0.09375 * width, block_height // 20))

            # S
            pygame.draw.rect(w, (235, 80, 78), (0.3085 * width, xc + height / 3 + block_height + block_height + block_height // 20, block_width // 20, block_height // 2))
            pygame.draw.rect(w, (235, 80, 78), (0.3085 * width, xc + height / 3 + block_height + 3 * block_height // 2 + block_height // 20, 0.0651 * width, block_height // 20))
            pygame.draw.rect(w, (235, 80, 78), (2.5 * width // 8 - block_width // 40 + (width // 3 - 7 * block_width + block_width // 4) // 2, xc + height // 6 + 7 * block_height // 2, block_width // 20, 4 * block_height // 2 + block_height // 10))
            pygame.draw.rect(w, (235, 80, 78), (2.5 * width // 8 - block_width // 40 + (width // 3 - 7 * block_width + block_width // 4) // 2, xc + height // 6 + 7 * block_height // 2, (width // 3 - 7 * block_width + block_width // 8) // 2, block_height // 20))

            # A
            pygame.draw.rect(w, (235, 80, 78), (2.5 * width // 8 - block_width // 40 + (width // 3 - 7 * block_width + block_width // 4) // 2 + block_width, xc + height / 3 + block_height // 2 + block_height + block_height // 20, (width // 3 - 9 * block_width + block_width // 4) // 2, block_height // 20))
            pygame.draw.rect(w, (235, 80, 78), (2.5 * width // 8 - block_width // 40 + (width // 3 - 7 * block_width + block_width // 4) // 2 + block_width, xc + height / 3 + block_height // 2 + block_height + block_height // 20, block_width // 20, 3.5 * block_height // 2 + block_height // 10))
            pygame.draw.rect(w, (235, 80, 78), (0.277 * width, xc + height / 3 + 2 * block_height // 2 + block_height + block_height // 20, block_width // 20, 2.5 * block_height // 2 + block_height // 10))
            pygame.draw.rect(w, (235, 80, 78), (0.277 * width, xc + height / 3 + block_height // 4 + block_height // 2 + block_height + block_height // 20 + 3 * block_height // 2 + block_height // 20, 0.1286 * width, block_height // 20))
            # P
            pygame.draw.rect(w, (235, 80, 78), (0.578 * width, xc + height // 6 + 11 * block_height // 2, 0.1365 * width, block_height // 20))
            pygame.draw.rect(w, (235, 80, 78), (0.7125 * width, xc - 2 * block_height + height // 6 + 11 * block_height // 2, block_width // 20, (height * 2 / 3 - block_height // 2) - (height // 6 + 11 * block_height // 2) - block_height))

            # Hold
            pygame.draw.rect(w, (235, 80, 78), (0.208 * width, 2 * block_height // 3 + xc + height / 3 + block_height // 4 + block_height // 2 + block_height + block_height // 20 + 3 * block_height // 2 + block_height // 20, 0.573 * width, block_height // 20))
            pygame.draw.rect(w, (235, 80, 78), (0.208 * width, xc + height / 3 + 1.62 * block_height + block_height + block_height // 20, block_width // 20, 2.5 * block_height // 2 + block_height // 10))
            pygame.draw.rect(w, (235, 80, 78), (0.208 * width + 0.573 * width - block_width // 20, xc + height / 3 + 1.62 * block_height + block_height + block_height // 20, block_width // 20, 2.5 * block_height // 2 + block_height // 10))
            pygame.draw.rect(w, (235, 80, 78), (width // 2 - block_width // 40, xc + height / 3 + 1.62 * block_height + block_height + block_height // 20 + 2.5 * block_height // 2 - block_height // 8, block_width // 20, block_height // 4))

            # Rot
            pygame.draw.rect(w, (235, 80, 78), (0.38 * width, block_height + 2 * block_height // 3 + xc + height / 3 + block_height // 4 + block_height // 2 + block_height + block_height // 20 + 3 * block_height // 2 + block_height // 20, 0.475 * width, block_height // 20))
            pygame.draw.rect(w, (235, 80, 78), (0.38 * width, block_height + xc + height / 3 + 3 * block_height + block_height + block_height // 20, block_width // 20, 1.5 * block_height // 2 + block_height // 10))
            pygame.draw.rect(w, (235, 80, 78), (0.619 * width, block_height + xc + height / 3 + 3 * block_height + block_height + block_height // 20, block_width // 20, 1.5 * block_height // 2 + block_height // 10))
            pygame.draw.rect(w, (235, 80, 78), (0.38 * width + 0.475 * width - block_width // 20, block_height + xc + height / 3 + 1.62 * block_height + block_height + block_height // 20 - 1.82 * block_height, block_width // 20, 3.17 * block_height))
            pygame.draw.rect(w, (235, 80, 78), (width // 2 - block_width // 40, block_height + xc + height / 3 + 1.62 * block_height + block_height + block_height // 20 + 2.5 * block_height // 2 - block_height // 8, block_width // 20, block_height))
            pygame.draw.rect(w, (235, 80, 78), (0.823 * width, xc + height / 3 + 3 * block_height // 4 + block_height + block_height // 20, (width // 3 - 9 * block_width + block_width // 4) // 2 + 0.0023 * width, block_height // 20))

            text = font.render("QUIT", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (width // 2, xc + height // 6 + block_height // 2)
            w.blit(text, trex)

            text = font.render("INSTANT DOWN", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (width // 2, xc + height // 6 + 3 * block_height // 2)
            w.blit(text, trex)

            text = font.render("MOVE RIGHT", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (width // 2, xc + height // 6 + 5 * block_height // 2)
            w.blit(text, trex)

            text = font.render("MOVE DOWN", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (width // 2, xc + height // 6 + 7 * block_height // 2)
            w.blit(text, trex)

            text = font.render("MOVE LEFT", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (width // 2, xc + height // 6 + 9 * block_height // 2)
            w.blit(text, trex)

            text = font.render("PAUSE/RESUME", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (width // 2, xc + height // 6 + 11 * block_height // 2)
            w.blit(text, trex)

            text = font.render("HOLD", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (width // 2, xc + height // 6 + 13 * block_height // 2)
            w.blit(text, trex)

            text = font.render("ROTATE", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (width // 2, xc + height // 6 + 15 * block_height // 2)
            w.blit(text, trex)

            # L Alt
            pygame.draw.rect(w, (235, 80, 78), (width * 0.40625 - 1.6 * 0.0321 * width, xc + height * 2 / 3 - block_height // 2, 1.6 * block_width, block_height),
                             block_width // 2, int(block_height / 8))
            text = font.render("Alt", True, d_color)
            trex = text.get_rect()
            trex.center = (
                width * 0.40625 - 1.6 * 0.0321 * width + 1.5 * 0.016 * width, xc + height * 2 / 3)
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "OpenSans-Medium.ttf"), int(height / 80))
            text = font.render("CCW", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (
                width * 0.40625 - 1.6 * 0.0321 * width + 1.5 * 0.016 * width + 1.5 * 0.008 * width, xc - 3 * block_height // 5 + height * 2 / 3)
            w.blit(text, trex)

            # R Alt
            pygame.draw.rect(w, (235, 80, 78),
                             (width * 0.40625 + 6 * 0.03153 * width, xc + height * 2 / 3 - block_height // 2, 1.6 * block_width, block_height),
                             block_width // 2, int(block_height / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height / 24))
            text = font.render("Alt", True, d_color)
            trex = text.get_rect()
            trex.center = (
                width * 0.40625 + 6 * 0.03155 * width + 1.5 * 0.016 * width, xc + height * 2 / 3)
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "OpenSans-Medium.ttf"), int(height / 80))
            text = font.render("CCW", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (
                width * 0.40625 + 6 * 0.03155 * width + 1.5 * 0.016 * width - 1.5 * 0.008 * width, xc - 3 * block_height // 5 + height * 2 / 3)
            w.blit(text, trex)

            # spacebar:
            pygame.draw.rect(w, (235, 80, 78), (width * 0.40625, xc + height * 2 / 3 - block_height // 2, 0.1875 * width, block_height), block_height // 2,
                             int(block_height / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "Everson Mono Bold.ttf"), int(height / 10))
            text = font.render("⎵", True, d_color)
            trex = text.get_rect()
            trex.center = (width // 2, xc + height * 2 / 3 - block_height // 8)
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "OpenSans-Medium.ttf"), int(height / 80))
            text = font.render("CW", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (width // 2 + 1.5 * 0.005 * width, xc - 3 * block_height // 5 + height * 2 / 3)
            w.blit(text, trex)

            # Esc
            pygame.draw.rect(w, (235, 80, 78), (0.175 * width, xc + height // 6, block_width, block_height), block_width // 2,
                             int(block_height / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height / 32))
            text = font.render("ESC", True, d_color)
            trex = text.get_rect()
            trex.center = (0 + 2.5 * width // 8 - 4 * block_width + block_width // 10, xc + height // 6 + block_height // 2)
            w.blit(text, trex)

            # W
            pygame.draw.rect(w, (235, 80, 78), (0.175 * width + 3 * 0.032 * width + 0.0221 * width, xc + height / 3 + .367 * block_height, block_width, block_height), block_width // 2, int(block_height / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height // 25))
            text = font.render("W", True, d_color)
            trex = text.get_rect()
            trex.center = (0.175 * width + 3 * 0.032 * width + 0.0221 * width + 0.016 * width, xc + .367 * block_height + height / 3 + block_height // 2 + block_height // 10)
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "seguisym.ttf"), int(block_height // 3))
            text = font.render("▲", True, d_color)
            trex = text.get_rect()
            trex.center = (
                0.175 * width + 3 * 0.032 * width + 0.0221 * width + 0.016 * width, xc + .367 * block_height + height / 3 + block_height // 10)
            w.blit(text, trex)

            # A
            pygame.draw.rect(w, (235, 80, 78),
                             (0.175 * width + 2 * 0.0319 * width + 0.0221 * width, xc + .367 * block_height + height / 3 + block_height + block_height // 20, block_width, block_height),
                             block_width // 2, int(block_height / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height // 25))
            text = font.render("A", True, d_color)
            trex = text.get_rect()
            trex.center = (0.175 * width + 2 * 0.0319 * width + 0.0221 * width + 0.016 * width, xc + .367 * block_height + height / 3 + block_height // 2 + block_height + block_height // 20 - block_height // 10)
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "seguisym.ttf"), int(block_height // 3))
            text = font.render("◀", True, d_color)
            trex = text.get_rect()
            trex.center = (0.175 * width + 2 * 0.0319 * width + 0.0221 * width + 0.016 * width, xc + .367 * block_height + height / 3 + 9 * block_height // 10 + block_height + block_height // 20 - block_height // 10)
            w.blit(text, trex)

            # S
            pygame.draw.rect(w, (235, 80, 78), (0.175 * width + 3 * 0.032 * width + 0.0221 * width, xc + height / 3 + block_height + block_height // 20 + .367 * block_height, block_width, block_height),
                             block_width // 2, int(block_height / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height // 25))
            text = font.render("S", True, d_color)
            trex = text.get_rect()
            trex.center = (0.175 * width + 3 * 0.032 * width + 0.0221 * width + 0.016 * width, xc + .367 * block_height + height / 3 + block_height // 2 + block_height + block_height // 20 - block_height // 10)
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "seguisym.ttf"), int(block_height // 3))
            text = font.render("▼", True, d_color)
            trex = text.get_rect()
            trex.center = (0.175 * width + 3 * 0.032 * width + 0.0221 * width + 0.016 * width, xc + .367 * block_height + height / 3 + 9 * block_height // 10 + block_height + block_height // 20 - block_height // 10)
            w.blit(text, trex)

            # D
            pygame.draw.rect(w, (235, 80, 78),
                             (0.175 * width + 4 * 0.0321 * width + 0.0221 * width, xc + .367 * block_height + height / 3 + block_height + block_height // 20, block_width, block_height),
                             block_width // 2, int(block_height / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height // 25))
            text = font.render("D", True, d_color)
            trex = text.get_rect()
            trex.center = (0.175 * width + 4 * 0.032 * width + 0.0221 * width + 0.016 * width, xc + .367 * block_height + height / 3 + block_height // 2 + block_height + block_height // 20 - block_height // 10)
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "seguisym.ttf"), int(block_height // 3))
            text = font.render("▶", True, d_color)
            trex = text.get_rect()
            trex.center = (0.175 * width + 4 * 0.032 * width + 0.0221 * width + 0.016 * width, xc + .367 * block_height + height / 3 + 9 * block_height // 10 + block_height + block_height // 20 - block_height // 10)
            w.blit(text, trex)

            # P
            pygame.draw.rect(w, (235, 80, 78), (0.7943 * width - 3 * 0.032 * width, xc + .367 * block_height + height / 3, block_width, block_height), block_width // 2,
                             int(block_height / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height // 25))
            text = font.render("P", True, d_color)
            trex = text.get_rect()
            trex.center = (0.7943 * width - 3 * 0.032 * width + 1 * 0.016 * width, xc + .367 * block_height + height / 3 + block_height // 2)
            w.blit(text, trex)

            # Enter
            pygame.draw.rect(w, (235, 80, 78),
                             (0.7943 * width - 1 * 0.032 * width, xc + height / 3 + 1.367 * block_height + block_height // 20, 2 * block_width, block_height), block_height // 2,
                             int(block_height / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height / 25))
            text = font.render("Enter", True, d_color)
            trex = text.get_rect()
            trex.center = (0.7943 * width - 1 * 0.032 * width + 2 * 0.016 * width, xc + 1.367 * block_height + block_height // 20 + height / 3 + block_height // 2)
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "OpenSans-Medium.ttf"), int(height / 80))
            text = font.render("CW", True, (235, 80, 78))
            trex = text.get_rect()
            trex.center = (0.7943 * width + 2.3 * 0.016 * width, xc + 1.367 * block_height + block_height // 20 + height / 3 + block_height // 2 - block_height // 4)
            w.blit(text, trex)

            # R Shift
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height / 25))
            pygame.draw.rect(w, (235, 80, 78), (0.7943 * width - 2 * 0.032 * width, xc + height / 3 + 2 * block_height + block_height // 10 + .367 * block_height, 3 * block_width, block_height), block_height // 2, int(block_height / 8))
            text = font.render("Shift", True, d_color)
            trex = text.get_rect()
            trex.center = (0.7943 * width - 2 * 0.032 * width + 3 * 0.016 * width, xc + .367 * block_height + height / 3 + block_height // 2 + 2 * block_height + block_height // 10)
            w.blit(text, trex)

            # L Shift
            pygame.draw.rect(w, (235, 80, 78), (0.175 * width, xc + height / 3 + 2 * block_height + block_height // 10 + .367 * block_height, 2 * block_width, block_height), block_height // 2, int(block_height / 8))
            text = font.render("Shift", True, d_color)
            trex = text.get_rect()
            trex.center = (0.175 * width + 2 * 0.016 * width, xc + .367 * block_height + height / 3 + block_height // 2 + 2 * block_height + block_height // 10)
            w.blit(text, trex)

        if esc == 4 and 1 == 0:
            pygame.draw.rect(w, (0, 0, 0), (0, 0, Block_Width, Block_1_Height))
            pygame.draw.rect(w, (0, 0, 0), (0, Block_2_Y_Loc, Block_Width, Block_1_Height))

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "MAGNETOB.ttf"), int(height / 25))
            text = font.render("By: Jatan Bhatt", True, Text_1_Color)
            trex = text.get_rect()
            trex.center = (18.7 * width / 21, Block_2_Y_Loc + int(height / 25))
            w.blit(text, trex)

            font = pygame.font.Font(os.path.join("Assets", "Fonts", "PressStart2P-Regular.ttf"), int(height / 25))
            text = font.render("ver 2.0", True, settings_color)
            trex = text.get_rect()
            trex.center = (1 * width / 21, Block_1_Height - int(height / 25))
            w.blit(text, trex)

        if Click == 0:

            if d_x < int(width + 20):

                d_x += 120
                dx2 += 30
                dx3 += 150

        if Click == 1:

            if d_x > 103 * width / 180:

                d_x -= 120
                dx2 -= 30
                dx3 -= 150

        if pau != 15:

            pau += 1

        pygame.display.update()

        if ml == 1:

            ml = 0

        if cd < 100:

            cd += 1

        keypress = pygame.key.get_pressed()

        for event in pygame.event.get():

            if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:

                run = False
                exit_sequence = 1

            if (keypress[pygame.K_LSHIFT] or keypress[pygame.K_RSHIFT]) and cd == 100:

                if keypress[pygame.K_1]:

                    run = False
                    exit_sequence = 4
                    cd = 0
                    height = 720
                    x = 16
                    y = 9
                    width = int(height / y * x)
                    block_width = width // 32
                    block_height = height // 18
                    w = pygame.display.set_mode((width, height))
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                    L[6] = str(height) + "\n"
                    L[7] = str(width) + "\n"
                    doc.writelines(L)
                    doc.close()
                elif keypress[pygame.K_2]:

                    cd = 0
                    run = False
                    exit_sequence = 4
                    height = 1080
                    x = 16
                    y = 9
                    width = int(height / y * x)
                    block_width = width // 32
                    block_height = height // 18
                    w = pygame.display.set_mode((width, height))
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                    L[6] = str(height) + "\n"
                    L[7] = str(width) + "\n"
                    doc.writelines(L)
                    doc.close()
                elif keypress[pygame.K_3]:

                    cd = 0
                    run = False
                    exit_sequence = 4
                    height = 1440
                    x = 16
                    y = 9
                    width = int(height / y * x)
                    block_width = width // 32
                    block_height = height // 18
                    w = pygame.display.set_mode((width, height))
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                    L[6] = str(height) + "\n"
                    L[7] = str(width) + "\n"
                    doc.writelines(L)
                    doc.close()
                elif keypress[pygame.K_4]:

                    run = False
                    exit_sequence = 4
                    cd = 0
                    height = 800
                    x = 16
                    y = 10
                    width = int(height / y * x)
                    block_width = width // 32
                    block_height = height // 18
                    w = pygame.display.set_mode((width, height))
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                    L[6] = str(height) + "\n"
                    L[7] = str(width) + "\n"
                    doc.writelines(L)
                    doc.close()
                elif keypress[pygame.K_5]:

                    run = False
                    exit_sequence = 4
                    cd = 0
                    height = 1200
                    x = 16
                    y = 10
                    width = int(height / y * x)
                    block_width = width // 32
                    block_height = height // 18
                    w = pygame.display.set_mode((width, height))
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                    L[6] = str(height) + "\n"
                    L[7] = str(width) + "\n"
                    doc.writelines(L)
                    doc.close()

                elif keypress[pygame.K_6]:

                    run = False
                    exit_sequence = 4
                    cd = 0
                    height = 1600
                    x = 16
                    y = 10
                    width = int(height / y * x)
                    block_width = width // 32
                    block_height = height // 18
                    w = pygame.display.set_mode((width, height))
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                    L[6] = str(height) + "\n"
                    L[7] = str(width) + "\n"
                    doc.writelines(L)
                    doc.close()

                elif keypress[pygame.K_7]:

                    run = False
                    exit_sequence = 4
                    cd = 0
                    height = 720
                    x = 21
                    y = 9
                    width = int(height / y * x)
                    block_width = width // 32
                    block_height = height // 18
                    w = pygame.display.set_mode((width, height))
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                    L[6] = str(height) + "\n"
                    L[7] = str(width) + "\n"
                    doc.writelines(L)
                    doc.close()

                elif keypress[pygame.K_8]:

                    run = False
                    exit_sequence = 4
                    cd = 0
                    height = 1080
                    x = 21
                    y = 9
                    width = int(height / y * x)
                    block_width = width // 32
                    block_height = height // 18
                    w = pygame.display.set_mode((width, height))
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                    L[6] = str(height) + "\n"
                    L[7] = str(width) + "\n"
                    doc.writelines(L)
                    doc.close()
                elif keypress[pygame.K_9]:

                    run = False
                    exit_sequence = 4
                    cd = 0
                    height = 1440
                    x = 21
                    y = 9
                    width = int(height / y * x)
                    block_width = width // 32
                    block_height = height // 18
                    w = pygame.display.set_mode((width, height))
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                    L[6] = str(height) + "\n"
                    L[7] = str(width) + "\n"
                    doc.writelines(L)
                    doc.close()

                elif keypress[pygame.K_0]:

                    run = False
                    exit_sequence = 4
                    cd = 0
                    doc = open(os.path.join("Assets/Resolution (Read Me).txt"), "r")
                    L = doc.readlines()
                    height = int((L[2]).rstrip())
                    width = int((L[1]).rstrip())
                    doc.close()
                    block_width = width // 32
                    block_height = height // 18
                    w = pygame.display.set_mode((width, height))
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "r")
                    L = doc.readlines()
                    doc.close()
                    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                    L[6] = str(height) + "\n"
                    L[7] = str(width) + "\n"
                    doc.writelines(L)
                    doc.close()

                elif keypress[pygame.K_a]:

                    if keypress[pygame.K_LALT] or keypress[pygame.K_RALT]:

                        run = False
                        exit_sequence = 4
                        cd = 0
                        w = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                        x, y = w.get_size()
                        height = y
                        width = x
                        block_width = width // 32
                        block_height = height // 18
                        doc = open(os.path.join("Assets", "Data", "Variables.txt"), "r")
                        L = doc.readlines()
                        doc.close()
                        doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
                        L[6] = str(0) + "\n"
                        L[7] = str(0) + "\n"
                        doc.writelines(L)
                        doc.close()

            block_width = width // 32
            block_height = height // 18
            if event.type == pygame.MOUSEBUTTONUP:

                if Mouse_Loc[0] >= dx3 and 1 / 7 * height + int(height / 24 + height / 20) >= Mouse_Loc[1] >= 1 / 7 * height + int(height / 24):

                    active = True

                else:

                    active = False

            if event.type == pygame.MOUSEBUTTONUP:

                if 1 == 1:

                    ml = 1

                if 0.01 * width < Mouse_Loc[0] < 0.04 * width and 1 / 4 * block_height < Mouse_Loc[1] < 5 / 4 * block_height:

                    conts = 1

                elif height > Mouse_Loc[1] > 2 * block_height and not active and Click == 0 and conts == 0:

                    run = False

                elif comp == 0 and 0 < Mouse_Loc[0] < 0.08 * width and Mouse_Loc[1] < height and Mouse_Loc[1] < height // 4 and not active and Click == 0 and conts == 0:

                    run = False
                    exit_sequence = 1

                else:

                    conts = 0

            if keypress[pygame.K_SPACE] and not active:

                run = False

            if event.type == pygame.KEYDOWN and active:

                if event.key == pygame.K_BACKSPACE:

                    Name_Editor = Name_Editor[:-1]

                elif event.key != pygame.K_ESCAPE:

                    if (len(Name_Editor)) <= 24:

                        Name_Editor += event.unicode

                    else:

                        pau = 0

    BGM_Main_Screen.stop()

    #Loading/Ending Sreen
    load = 0
    xo = 6 * block_height
    image = pygame.image.load(os.path.join("Assets", "Data", "LOAD.png"))
    w.blit(pygame.transform.smoothscale(image, (width, height)), (0, 0))
    if exit_sequence == 1:

        Ending()

    else:

        Loading(load, xo)

    return exit_sequence

# Convert To X-Axis Co-ordinates
def convx(n):

    x = int((n - (n % 100)) / 100)
    return x

# Convert To Y-Axis Co-ordinates
def convy(n):

    x = n % 100
    return x

def main():

    global BGM_Game_Playing2
    doc = open(os.path.join("Assets", "Data", "Variables.txt"), "r")
    L = doc.readlines()
    FPS_Settings = int((L[1]).rstrip())
    Music_Settings = int((L[2]).rstrip())
    SFX_Settings = int((L[3]).rstrip())
    High_Score = int((L[4]).rstrip())
    doc.close()
    run = True
    INTEp = 1
    pygame.init()
    clock = pygame.time.Clock()

    if FPS_Settings == 0:

        FPS = 30

    elif FPS_Settings == 2:

        FPS = 120

    else:

        FPS = 60

    # Frequency
    Hold_On = 1
    Rotation_Frequency = FPS
    Left_Movement_Clock_Frequency = 2 * FPS // 3
    Right_Movement_Clock_Frequency = 2 * FPS // 3
    Down_Movement_Clock_Frequency = 2 * FPS // 3
    IMD_Movement_Clock_Frequency = FPS * 2
    Vert_Movement_Clock_Frequency = FPS

    # Default Clock Values
    Rotation_Clock = Rotation_Frequency
    IMD_Movement_Clock = IMD_Movement_Clock_Frequency
    Down_Movement_Clock = Down_Movement_Clock_Frequency
    Left_Movement_Clock = Left_Movement_Clock_Frequency
    Right_Movement_Clock = Right_Movement_Clock_Frequency

    # Defauult Variable Values
    exit_sequence = 0
    TA = 0
    TD = 0
    TS = 0
    TW = 0
    TP = 0
    TR = 0
    actfps = math.ceil(FPS / 24)
    endmusicclock = 0
    visi = 0
    Score = 0
    modder = 0
    First_Swap = 0
    Image_No = 0
    Block_Grid_Color = (0, 0, 0)
    disp = ""
    ticker = 0
    Rotaion_Status = 0
    Vert_Movement_Clock = 0
    Stop_Current_Shape_Movement = 0
    Spawn_New_Block = 1
    clicked = 0
    stop = 0
    Buffer = 0
    Rotation_Manager_Boolean = 1
    Anti_Rotation_Manager_Boolean = 1
    Block_X_No = 10
    Block_Y_No = 17

    # Set Grids/Arrays
    Current_Shape = [0] * 4
    Next_Shape = [0] * 4
    Ghost = [0] * 4
    Block_Grid_X = [0] * Block_X_No
    Block_Grid_Y = [0] * Block_Y_No
    Block_Grid_Color_Boolean = [0] * (Block_X_No * (Block_Y_No + 4))
    Current_Shape_Display_Grid = [0] * (Block_X_No * Block_Y_No)
    Next_Shape_Display_Grid = [0] * 12

    # Colors
    Current_Shape_Color = (0, 0, 0)
    Block_Grid_Free_Color = (150, 150, 150)
    Block_Grid_Red = (170, 30, 40)
    Next_Shape_Color = (randint(0, 255), randint(0, 255), randint(0, 255))

    # Shape Randomizer and Color Picker
    Shape_Hold_Number = 0
    Shape_Hold = [0] * 4
    Shape_Hold_Color = (0, 0, 0)
    HLDB = 0
    Bag = [0] * 7
    Current_Shape_Randomizer = randint(1, 7)
    Next_Shape_Randomizer = randint(1, 7)
    while Bag[Next_Shape_Randomizer - 1] == 1:

        Next_Shape_Randomizer = randint(1, 7)

    Bag[Next_Shape_Randomizer - 1] = 1

    def GCD(Next_Shape_Randomizer):

        global Next_Shape_Color
        if Next_Shape_Randomizer == 1:

            Next_Shape_Color = (26 * 0.3, 194 * 0.3, 241 * 0.3)

        elif Next_Shape_Randomizer == 2:

            Next_Shape_Color = (253 * 0.3, 223 * 0.3, 102 * 0.3)

        elif Next_Shape_Randomizer == 3:

            Next_Shape_Color = (151 * 0.3, 59 * 0.3, 152 * 0.3)

        elif Next_Shape_Randomizer == 4:

            Next_Shape_Color = (0 * 0.3, 131 * 0.3, 196 * 0.3)

        elif Next_Shape_Randomizer == 5:

            Next_Shape_Color = (247 * 0.3, 160 * 0.3, 67 * 0.3)

        elif Next_Shape_Randomizer == 6:

            Next_Shape_Color = (148 * 0.3, 202 * 0.3, 100 * 0.3)

        elif Next_Shape_Randomizer == 7:

            Next_Shape_Color = (238 * 0.3, 69 * 0.3, 51 * 0.3)

        return Next_Shape_Color

    def NSC(Next_Shape_Randomizer):

        global Next_Shape_Color

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

        return Next_Shape_Color

    Next_Shape_Color = NSC(Next_Shape_Randomizer)

    # Decide BGM
    if Music_Settings == 3:

        if randint(0, 1) == 0:

            BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm.ogg"))

        else:

            BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm2.ogg"))

    elif Music_Settings == 1:

        BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm2.ogg"))

    elif Music_Settings == 2:

        BGM_Game_Playing = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "main-bgm.ogg"))

    if Music_Settings != 0:

        BGM_Game_Playing2 = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "INTE.ogg"))
        BGM_Game_Playing2.play(loops=-1)
        BGM_End_Screen = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "endth.ogg"))
        BGM_Game_Playing2.set_volume(0)

    # Set Arrays
    i = 0
    while i < Block_X_No:

        Block_Grid_X[i] = int(width / 2 - (Block_X_No / 2) * block_width + i * block_width)
        i += 1

    i = 0
    while i < Block_Y_No:

        Block_Grid_Y[i] = int(height / 2 - block_height / 2 - (Block_Y_No // 2 - i) * block_height)
        i += 1

    yyy = 0
    ng = 0
    while yyy < Block_Y_No:

        xxx = 0
        yyy += 1
        while xxx < Block_X_No:

            Current_Shape_Display_Grid[ng] = (xxx * 100) + yyy - 1
            xxx += 1
            ng += 1

    yyy = 0
    ng3 = 0
    while yyy < 3:

        xxx = 0
        yyy += 1
        while xxx < 4:

            Next_Shape_Display_Grid[ng3] = (((15 + Block_X_No + xxx) * block_width) * 10000) + 100 + ((yyy - 1) * block_height)
            ng3 += 1
            xxx += 1

    if Music_Settings != 0:

        BGM_Game_Playing.play(loops=-1)

    load = 55
    xo = 0
    Loading(load, xo)
    fpsavg = [FPS] * 5
    video1 = cv2.VideoCapture("Assets/Gameplay/Gamee.mp4")
    success1, video_image1 = video1.read()

    def CGrid(Current_Shape_Randomizer, Current_Shape):

        if Current_Shape_Randomizer == 1:

            Current_Shape[0] = 3
            Current_Shape[1] = 4
            Current_Shape[2] = 5
            Current_Shape[3] = 6

        if Current_Shape_Randomizer == 2:

            Current_Shape[0] = 14
            Current_Shape[1] = 15
            Current_Shape[2] = 4
            Current_Shape[3] = 5

        if Current_Shape_Randomizer == 3:

            Current_Shape[0] = 3
            Current_Shape[1] = 4
            Current_Shape[2] = 5
            Current_Shape[3] = 14

        if Current_Shape_Randomizer == 4:

            Current_Shape[0] = 3
            Current_Shape[1] = 13
            Current_Shape[2] = 14
            Current_Shape[3] = 15

        if Current_Shape_Randomizer == 5:

            Current_Shape[0] = 5
            Current_Shape[1] = 15
            Current_Shape[2] = 14
            Current_Shape[3] = 13

        if Current_Shape_Randomizer == 6:

            Current_Shape[0] = 13
            Current_Shape[1] = 14
            Current_Shape[2] = 4
            Current_Shape[3] = 5

        if Current_Shape_Randomizer == 7:

            Current_Shape[0] = 3
            Current_Shape[1] = 4
            Current_Shape[2] = 14
            Current_Shape[3] = 15

        return Current_Shape


    def EGrid(Shape_Hold_Number, Shape_Hold):

        if Shape_Hold_Number == 1:

            Shape_Hold[0] = 4
            Shape_Hold[1] = 5
            Shape_Hold[2] = 6
            Shape_Hold[3] = 7

        if Shape_Hold_Number == 2:

            Shape_Hold[0] = 1
            Shape_Hold[1] = 2
            Shape_Hold[2] = 5
            Shape_Hold[3] = 6

        if Shape_Hold_Number == 3:

            Shape_Hold[0] = 0
            Shape_Hold[1] = 1
            Shape_Hold[2] = 2
            Shape_Hold[3] = 5

        if Shape_Hold_Number == 4:

            Shape_Hold[0] = 0
            Shape_Hold[1] = 4
            Shape_Hold[2] = 5
            Shape_Hold[3] = 6

        if Shape_Hold_Number == 5:

            Shape_Hold[0] = 2
            Shape_Hold[1] = 4
            Shape_Hold[2] = 5
            Shape_Hold[3] = 6

        if Shape_Hold_Number == 6:

            Shape_Hold[0] = 4
            Shape_Hold[1] = 5
            Shape_Hold[2] = 1
            Shape_Hold[3] = 2

        if Shape_Hold_Number == 7:

            Shape_Hold[0] = 0
            Shape_Hold[1] = 1
            Shape_Hold[2] = 5
            Shape_Hold[3] = 6

        return Shape_Hold

    def mvm(ng):

        x3 = width - (4 - (ng % 4)) * block_width - 2.9 * block_width
        if Next_Shape_Randomizer < 3:

            x3 -= block_width // 2

        y3 = (ng // 4) * block_height + 3 * block_height
        pygame.draw.rect(w, Next_Shape_Color, (x3 + block_width / 20, y3 + block_height / 20, int(9 * block_width / 10), int(9 * block_height / 10)),28 * int(block_width / 40), int(block_height / 8))

    def mvm2(ng):

        x3 = (ng % 4) * block_width + 3.93 * block_width
        if Shape_Hold_Number < 3:

            x3 -= block_width // 2

        y3 = height // 2 + (ng // 4) * block_height + 4 * block_height
        pygame.draw.rect(w, Shape_Hold_Color, (x3 + block_width / 20, y3 + block_height / 20, int(9 * block_width / 10), int(9 * block_height / 10)),28 * int(block_width / 40), int(block_height / 8))

    def mvm3(ng):

        x3 = convx(Current_Shape_Display_Grid[ng])
        y3 = convy(Current_Shape_Display_Grid[ng])
        pygame.draw.rect(w, Current_Shape_Color,(Block_Grid_X[x3] + block_width / 20, Block_Grid_Y[y3] + block_height / 20, int(9 * block_width / 10), int(9 * block_height / 10)),28 * int(block_width / 40), int(block_height / 8))

    def mvm4(ng):

        Ghost_col = GCD(Current_Shape_Randomizer)
        x3 = convx(Current_Shape_Display_Grid[ng])
        y3 = convy(Current_Shape_Display_Grid[ng])
        pygame.draw.rect(w, Ghost_col,(Block_Grid_X[x3] + block_width / 20, Block_Grid_Y[y3] + block_height / 20, int(9 * block_width / 10), int(9 * block_height / 10)),28 * int(block_width / 40), int(block_height / 8))

    while run:

        clock.tick(FPS)

        fpsavg[4] = fpsavg[3]
        fpsavg[3] = fpsavg[2]
        fpsavg[2] = fpsavg[1]
        fpsavg[1] = fpsavg[0]
        fpsavg[0] = clock.get_fps()
        fpsav = (fpsavg[0] + fpsavg[1] + fpsavg[2] + fpsavg[3] + fpsavg[4]) / 5
        actfps = math.ceil(fpsav / 30) - 1
        if actfps < 1:

            actfps = 1

        Rotation_Frequency = fpsav
        Left_Movement_Clock_Frequency = 2 * fpsav // 3
        Right_Movement_Clock_Frequency = 2 * fpsav // 3
        Down_Movement_Clock_Frequency = 2 * fpsav // 3
        IMD_Movement_Clock_Frequency = fpsav * 2
        Vert_Movement_Clock_Frequency = fpsav * 2

        if Vert_Movement_Clock_Frequency < 1:

            Vert_Movement_Clock_Frequency = FPS * 2
            Rotation_Frequency = FPS
            Left_Movement_Clock_Frequency = 2 * FPS // 3
            Right_Movement_Clock_Frequency = 2 * FPS // 3
            Down_Movement_Clock_Frequency = 2 * FPS // 3
            IMD_Movement_Clock_Frequency = FPS * 2

        Mouse_Loc = pygame.mouse.get_pos()
        t7 = 0
        inc = 0
        while inc < 7:

            t7 += Bag[inc]
            inc += 1

        if t7 == 7:

            inc = 0
            while inc < 7:

                Bag[inc] = 0
                inc += 1

        if Music_Settings != 0 and INTEp == 1 and Score > 100000:

            BGM_Game_Playing.fadeout(2)
            BGM_Game_Playing2.set_volume(1)
            INTEp = 0

        pygame.draw.rect(w, BGCOLOR, (0, 0, width, height))
        if Image_No == 1000:

            Image_No = 701

        if Image_No % actfps == 0:

            success1, video_image1 = video1.read(1)
            if success1:

                video_surf1 = pygame.image.frombuffer(video_image1.tobytes(), video_image1.shape[1::-1], "BGR")

            else:

                video1 = cv2.VideoCapture("Assets/Gameplay/Gamee.mp4")

        w.blit(pygame.transform.smoothscale(video_surf1, (width, height)), (0, 0))

        Image_No += 1
        lm = 0
        Vert_Movement_Clock += 1 + ((Score / 5000) / 5)
        BGC_Grid_Color_Matcher = 0
        ng = (Block_X_No * Block_Y_No) - 1
        Instantaneous_Block_No = 0
        Instant_Row_Completion_No = 0
        Row_Deletion_Start_Block_No = 0

        if comp == 0:

            pygame.draw.rect(w, (235, 80, 78),((width // 2 - (Block_X_No * block_width) // 2 - block_width // 8) // 4 - block_width, 4 * height // 5 - block_height, 2 * block_width, 2 * block_height),block_width, int(block_height / 8))
            pygame.draw.rect(w, (235, 80, 78),((width // 2 - (Block_X_No * block_width) // 2 - block_width // 8) // 2 - block_width, 2 * height // 5 + block_height, 2 * block_width, 2 * block_height),block_width, int(block_height / 8))
            pygame.draw.rect(w, (235, 80, 78), (3 * (width // 2 - (Block_X_No * block_width) // 2 - block_width // 8) // 4 - block_width, 4 * height // 5 - block_height, 2 * block_width, 2 * block_height), block_width,int(block_height / 8))
            pygame.draw.rect(w, (235, 80, 78), (width // 2 + (width // 2 - (Block_X_No * block_width) // 2 - block_width // 8) - 3 * block_width // 2, 4 * height // 5 - block_height, 2 * block_width, 2 * block_height), block_width,int(block_height / 8))
            pygame.draw.rect(w, (235, 80, 78), (width - 3 * block_width // 2, block_height // 2, block_width, block_height), block_width, int(block_height / 8))
            pygame.draw.rect(w, (235, 80, 78), (block_width // 2, block_height // 2, block_width, block_height), block_width, int(block_height / 8))
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "Everson Mono Bold.ttf"), int(1.5 * block_height))
            text = font.render("△", True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = ((width // 2 - (Block_X_No * block_width) // 2 - block_width // 8) // 2, 2 * height // 5 + block_height + block_height)
            w.blit(text, trex)
            text = font.render("◁", True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = ((width // 2 - (Block_X_No * block_width) // 2 - block_width // 8) // 4, 4 * height // 5 + block_height // 10)
            w.blit(text, trex)
            text = font.render("▷", True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = (3 * (width // 2 - (Block_X_No * block_width) // 2 - block_width // 8) // 4, 4 * height // 5 + block_height // 10)
            w.blit(text, trex)
            text = font.render("⟳", True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = (width // 2 + (width // 2 - (Block_X_No * block_width) // 2 + block_width // 8 - 5 * block_width // 8), 4 * height // 5 + block_height // 10)
            w.blit(text, trex)
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "Everson Mono Bold.ttf"), int(1 * block_height))
            text = font.render("\u23F8", True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = (width - block_width, block_height)
            w.blit(text, trex)
            font = pygame.font.Font(os.path.join("Assets", "Fonts", "Everson Mono Bold.ttf"), int(1 * block_height))
            text = font.render("☓", True, (1, 5, 9))
            trex = text.get_rect()
            trex.center = (block_width, block_height)
            w.blit(text, trex)

        if Buffer == 0:

            if Spawn_New_Block == 1:

                if Score // 1000 - modder // 1000 != 0:

                    modder = Score

                else:

                    modder = Score

                while ng >= 0:

                    if Block_Grid_Color_Boolean[ng] != 0:

                        Instantaneous_Block_No += 1

                    if ng % Block_X_No == 0:

                        if Instantaneous_Block_No == Block_X_No:

                            Instant_Row_Completion_No += 1

                            if Row_Deletion_Start_Block_No == 0:

                                Row_Deletion_Start_Block_No = ng + 9

                        Instantaneous_Block_No = 0
                    ng -= 1
                if 16 > Current_Shape[0] > 2 and 16 > Current_Shape[1] > 2 and 16 > Current_Shape[2] > 2 and 16 > Current_Shape[3] > 2:

                    if Block_Grid_Color_Boolean[(Current_Shape[0] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[1] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[2] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[3] + Block_X_No)] != 0:

                        endmusicclock = 1
                        run = False
                        Spawn_New_Block = 0

            if Instant_Row_Completion_No != 0:

                if Instant_Row_Completion_No == 4:

                    Score += 5000
                    if randint(0, 1) == 0:

                        SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "4l-1.wav"))

                        if SFX_Settings == 1:

                            SFX.play()

                    else:

                        SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "4l-2.wav"))
                        if SFX_Settings == 1:

                            SFX.play()

                elif Instant_Row_Completion_No == 1:

                    Score += 625
                    SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "1l.wav"))
                    if SFX_Settings == 1:

                        SFX.play()
                else:

                    SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "2-3l.wav"))

                    if SFX_Settings == 1:

                        SFX.play()

                    if Instant_Row_Completion_No == 3:

                        Score += 2850

                    else:

                        Score += 1625

                while Row_Deletion_Start_Block_No >= 0:

                    if Instant_Row_Completion_No == 4 and Row_Deletion_Start_Block_No <= 39:

                        Block_Grid_Color_Boolean[Row_Deletion_Start_Block_No] = 0

                    elif Instant_Row_Completion_No == 3 and Row_Deletion_Start_Block_No <= 29:

                        Block_Grid_Color_Boolean[Row_Deletion_Start_Block_No] = 0

                    elif Instant_Row_Completion_No == 2 and Row_Deletion_Start_Block_No <= 19:

                        Block_Grid_Color_Boolean[Row_Deletion_Start_Block_No] = 0

                    elif Instant_Row_Completion_No == 1 and Row_Deletion_Start_Block_No <= 9:

                        Block_Grid_Color_Boolean[Row_Deletion_Start_Block_No] = 0

                    elif Instant_Row_Completion_No == 4:

                        Block_Grid_Color_Boolean[Row_Deletion_Start_Block_No] = Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No - 40)]

                    elif Instant_Row_Completion_No == 3:

                        Block_Grid_Color_Boolean[Row_Deletion_Start_Block_No] = Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No - 30)]

                    elif Instant_Row_Completion_No == 2:

                        Block_Grid_Color_Boolean[Row_Deletion_Start_Block_No] = Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No - 20)]

                    elif Instant_Row_Completion_No == 1:

                        Block_Grid_Color_Boolean[Row_Deletion_Start_Block_No] = Block_Grid_Color_Boolean[(Row_Deletion_Start_Block_No - Block_X_No)]

                    Row_Deletion_Start_Block_No -= 1

            if HLDB == 1 and Shape_Hold_Number == 0:

                Hold_On = 0
                Shape_Hold_Number = Current_Shape_Randomizer
                Spawn_New_Block = 1
                Shape_Hold_Color = Current_Shape_Color
                HLDB = 0
                Rotaion_Status = 0
                First_Swap = 1

            if Spawn_New_Block == 1 and HLDB == 0:

                if First_Swap == 1:

                    First_Swap += 1

                elif First_Swap == 2:

                    Hold_On = 1

                Current_Shape_Randomizer = Next_Shape_Randomizer
                Current_Shape_Color = NSC(Current_Shape_Randomizer)

                if Mod_Access_Blocked == 1:

                    Next_Shape_Randomizer = randint(1, 7)

                    while Bag[Next_Shape_Randomizer - 1] == 1:

                        Next_Shape_Randomizer = randint(1, 7)

                    Bag[Next_Shape_Randomizer - 1] = 1

                Stop_Current_Shape_Movement = 0
                Rotaion_Status = 0
                Next_Shape_Color = NSC(Next_Shape_Randomizer)
                Current_Shape = CGrid(Current_Shape_Randomizer, Current_Shape)
                Spawn_New_Block = 0

            if HLDB == 1 and Shape_Hold_Number != 0:

                HLDB = 0
                Hold_On = 0
                Rotaion_Status = 0
                Temp = Shape_Hold_Number
                Temp2 = Current_Shape_Color
                Current_Shape_Color = Shape_Hold_Color
                Shape_Hold_Color = Temp2
                Shape_Hold_Number = Current_Shape_Randomizer
                Current_Shape_Randomizer = Temp
                Current_Shape = CGrid(Current_Shape_Randomizer, Current_Shape)
                Spawn_New_Block = 0

            Next_Shape = EGrid(Next_Shape_Randomizer, Next_Shape)
            Shape_Hold = EGrid(Shape_Hold_Number, Shape_Hold)

            if Rotation_Clock < Rotation_Frequency:

                Rotation_Clock += 5

            Ghost[0] = Current_Shape[0]
            Ghost[1] = Current_Shape[1]
            Ghost[2] = Current_Shape[2]
            Ghost[3] = Current_Shape[3]
            runner2 = True
            while runner2:

                if (Block_Grid_Color_Boolean[Ghost[0] + 10] != 0 or Block_Grid_Color_Boolean[Ghost[1] + 10] != 0 or Block_Grid_Color_Boolean[Ghost[2] + 10] != 0 or Block_Grid_Color_Boolean[Ghost[3] + 10] != 0) or (Ghost[0] > (Block_X_No * Block_Y_No - Block_X_No - 1) or Ghost[1] > (Block_X_No * Block_Y_No - Block_X_No - 1) or Ghost[2] > (Block_X_No * Block_Y_No - Block_X_No - 1) or Ghost[3] > (Block_X_No * Block_Y_No - Block_X_No - 1)):

                    runner2 = False

                else:

                    Ghost[0] += 10
                    Ghost[1] += 10
                    Ghost[2] += 10
                    Ghost[3] += 10

            if Vert_Movement_Clock >= Vert_Movement_Clock_Frequency:

                ijx = 0
                Vert_Movement_Clock = 0

            else:

                ijx = 5

            keypress = pygame.key.get_pressed()
            if Left_Movement_Clock < Left_Movement_Clock_Frequency:

                Left_Movement_Clock += 5

            if Right_Movement_Clock < Right_Movement_Clock_Frequency:

                Right_Movement_Clock += 5

            if Down_Movement_Clock < Down_Movement_Clock_Frequency:

                Down_Movement_Clock += 5

            if IMD_Movement_Clock < IMD_Movement_Clock_Frequency:

                IMD_Movement_Clock += 5

            if Mod_Access_Blocked == 0:

                if keypress[pygame.K_1]:

                    Next_Shape_Randomizer = 1
                    Spawn_New_Block = 1

                if keypress[pygame.K_2]:

                    Next_Shape_Randomizer = 2
                    Spawn_New_Block = 1

                if keypress[pygame.K_3]:

                    Next_Shape_Randomizer = 3
                    Spawn_New_Block = 1

                if keypress[pygame.K_4]:

                    Next_Shape_Randomizer = 4
                    Spawn_New_Block = 1

                if keypress[pygame.K_5]:

                    Next_Shape_Randomizer = 5
                    Spawn_New_Block = 1

                if keypress[pygame.K_6]:

                    Next_Shape_Randomizer = 6
                    Spawn_New_Block = 1

                if keypress[pygame.K_7]:

                    Next_Shape_Randomizer = 7
                    Spawn_New_Block = 1

            if (keypress[pygame.K_RSHIFT] or keypress[pygame.K_LSHIFT]) and Hold_On == 1:

                HLDB = 1

            if (Current_Shape[0] > 159 and Current_Shape[1] > 159) or (Current_Shape[2] > 159 and Current_Shape[2] > 159) or (Block_Grid_Color_Boolean[(Current_Shape[0] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[1] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[2] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[3] + Block_X_No)] != 0):

                checker = 2

            else:

                checker = 0

            looper = checker + 1
            while looper > 0:

                looper -= 1
                if (keypress[pygame.K_a] or TA == 1 or keypress[pygame.K_LEFT]) and (Left_Movement_Clock >= Left_Movement_Clock_Frequency or checker > 0) and (Current_Shape[0]) % Block_X_No != 0 and (Current_Shape[1]) % Block_X_No != 0 and (Current_Shape[2]) % Block_X_No != 0 and (Current_Shape[3]) % Block_X_No != 0 and Block_Grid_Color_Boolean[(Current_Shape[0] - 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 1)] == 0:

                    ijx = 0
                    TA = 0
                    Left_Movement_Clock = 0
                    SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "move.wav"))
                    if SFX_Settings == 1:

                        SFX.play()

                    while ijx < 4:

                        Current_Shape[ijx] -= 1
                        ijx += 1

                if (keypress[pygame.K_d] or TD == 1 or keypress[pygame.K_RIGHT]) and (Right_Movement_Clock >= Right_Movement_Clock_Frequency or checker > 0) and (Current_Shape[0] - 9) % Block_X_No != 0 and (Current_Shape[1] - 9) % Block_X_No != 0 and (Current_Shape[2] - 9) % Block_X_No != 0 and (Current_Shape[3] - 9) % Block_X_No != 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 1)] == 0:

                    ijx = 0
                    TD = 0
                    Right_Movement_Clock = 0
                    SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "move.wav"))
                    if SFX_Settings == 1:

                        SFX.play()

                    while ijx < 4:

                        Current_Shape[ijx] += 1
                        ijx += 1

            checker = 0
            if (keypress[pygame.K_UP] or TS == 1) and Mod_Access_Blocked == 0 and Down_Movement_Clock >= Down_Movement_Clock_Frequency and Current_Shape[0] < Block_X_No * Block_Y_No - Block_X_No and Current_Shape[1] < Block_X_No * Block_Y_No - Block_X_No and Current_Shape[2] < Block_X_No * Block_Y_No - Block_X_No and Current_Shape[3] < Block_X_No * Block_Y_No - Block_X_No:

                ijx = 0
                TS = 0
                Down_Movement_Clock = 0
                while ijx < 4:

                    Current_Shape[ijx] -= Block_X_No
                    ijx += 1

            if (keypress[pygame.K_s] or keypress[pygame.K_DOWN] or TS == 1) and Down_Movement_Clock >= Down_Movement_Clock_Frequency and Current_Shape[0] < Block_X_No * Block_Y_No - Block_X_No and Current_Shape[1] < Block_X_No * Block_Y_No - Block_X_No and Current_Shape[2] < Block_X_No * Block_Y_No - Block_X_No and Current_Shape[3] < Block_X_No * Block_Y_No - Block_X_No:

                ijx = 0
                TS = 0
                Down_Movement_Clock = 0
                while ijx < 4:

                    Current_Shape[ijx] += Block_X_No
                    ijx += 1

            if Current_Shape[0] > (Block_X_No * Block_Y_No - Block_X_No - 1) or Current_Shape[1] > (Block_X_No * Block_Y_No - Block_X_No - 1) or Current_Shape[2] > (Block_X_No * Block_Y_No - Block_X_No - 1) or Current_Shape[3] > (Block_X_No * Block_Y_No - Block_X_No - 1):

                ijx = 5
                inx = 0
                Stop_Current_Shape_Movement = 1
                Buffer = FPS // 2
                Spawn_New_Block = 1
                while inx < 4:

                    Block_Grid_Color_Boolean[(Current_Shape[inx])] = Current_Shape_Randomizer
                    inx += 1

            elif Block_Grid_Color_Boolean[(Current_Shape[0] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[1] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[2] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[3] + Block_X_No)] != 0:

                ijx = 5
                inx = 0
                Stop_Current_Shape_Movement = 1
                Buffer = FPS // 2
                Spawn_New_Block = 1
                while inx < 4:

                    Block_Grid_Color_Boolean[(Current_Shape[inx])] = Current_Shape_Randomizer
                    inx += 1

            while ijx < 4 and stop == 0:

                Current_Shape[ijx] += Mod_Access_Blocked * Block_X_No
                ijx += 1

            if (keypress[pygame.K_w] or TW == 1 or (keypress[pygame.K_UP] and Mod_Access_Blocked != 0)) and IMD_Movement_Clock >= IMD_Movement_Clock_Frequency and Current_Shape[0] < Block_X_No * Block_Y_No - Block_X_No and Current_Shape[1] < Block_X_No * Block_Y_No - Block_X_No and Current_Shape[2] < Block_X_No * Block_Y_No - Block_X_No:

                ifx = 0
                TW = 0
                IMD_Movement_Clock = 0
                while ifx != 5:

                    ifx = 0
                    if Current_Shape[0] > (Block_X_No * Block_Y_No - Block_X_No - 1) or Current_Shape[1] > (Block_X_No * Block_Y_No - Block_X_No - 1) or Current_Shape[2] > (Block_X_No * Block_Y_No - Block_X_No - 1) or Current_Shape[3] > (Block_X_No * Block_Y_No - Block_X_No - 1):

                        ifx = 5
                        inx = 0
                        Stop_Current_Shape_Movement = 1
                        Spawn_New_Block = 1
                        SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "land.wav"))
                        if SFX_Settings == 1:

                            SFX.play()

                        while inx < 4:

                            Block_Grid_Color_Boolean[(Current_Shape[inx])] = Current_Shape_Randomizer
                            inx += 1

                    elif Block_Grid_Color_Boolean[(Current_Shape[0] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[1] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[2] + Block_X_No)] != 0 or Block_Grid_Color_Boolean[(Current_Shape[3] + Block_X_No)] != 0:

                        ifx = 5
                        inx = 0
                        Stop_Current_Shape_Movement = 1
                        Spawn_New_Block = 1
                        while inx < 4:

                            Block_Grid_Color_Boolean[(Current_Shape[inx])] = Current_Shape_Randomizer
                            inx += 1

                        if Current_Shape[0] > 9 and Current_Shape[1] > 9 and Current_Shape[2] > 9 and Current_Shape[3] > 9:

                            SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "land.wav"))
                            if SFX_Settings == 1:

                                SFX.play()

                    while ifx < 4:

                        Current_Shape[ifx] += Block_X_No
                        ifx += 1

        keypress = pygame.key.get_pressed()
        if (Rotation_Clock >= Rotation_Frequency) and (keypress[pygame.K_SPACE] or keypress[pygame.K_RETURN] or TR == 1):

            TR = 0
            Rotation_Manager_Boolean = 0
            Rotation_Clock = 0

        if Rotation_Clock >= Rotation_Frequency and (keypress[pygame.K_LALT] or keypress[pygame.K_RALT] or TR == 1):

            TR = 0
            Anti_Rotation_Manager_Boolean = 0
            Rotation_Clock = 0

        if Rotation_Manager_Boolean == 0:

            Rotation_Manager_Boolean = 1
            SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "rot.wav"))

            if SFX_Settings == 1:
                SFX.play()

            if Current_Shape_Randomizer == 1:

                if Rotaion_Status == 0 and Current_Shape[0] < 10:

                    Current_Shape[0] += 10
                    Current_Shape[1] += 10
                    Current_Shape[2] += 10
                    Current_Shape[3] += 10

                if Rotaion_Status == 1 and Current_Shape[0] % 10 == 9 and Current_Shape[2] % 10 == 9:

                    Current_Shape[0] -= 1
                    Current_Shape[1] -= 1
                    Current_Shape[2] -= 1
                    Current_Shape[3] -= 1

                if Rotaion_Status == 1 and Current_Shape[0] % 10 == 0 and Current_Shape[2] % 10 == 0:

                    Current_Shape[0] += 2
                    Current_Shape[1] += 2
                    Current_Shape[2] += 2
                    Current_Shape[3] += 2

                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 10)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 10)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 20)] == 0:

                    Current_Shape[0] -= 8
                    Current_Shape[1] += 1
                    Current_Shape[2] += 10
                    Current_Shape[3] += 19
                    Rotaion_Status = 1

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[1] - 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 2)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 1)] == 0:

                    Current_Shape[0] += 8
                    Current_Shape[1] -= 1
                    Current_Shape[2] -= 10
                    Current_Shape[3] -= 19
                    Rotaion_Status = 0

                Current_Shape_Randomizer = 1

            if Current_Shape_Randomizer == 3:

                if Rotaion_Status == 0 and Current_Shape[1] < 10:

                    Current_Shape[0] += 10
                    Current_Shape[1] += 10
                    Current_Shape[2] += 10
                    Current_Shape[3] += 10

                if Rotaion_Status == 1 and Current_Shape[0] % 10 == 9 and Current_Shape[2] % 10 == 9:

                    Current_Shape[0] -= 1
                    Current_Shape[1] -= 1
                    Current_Shape[2] -= 1
                    Current_Shape[3] -= 1

                if Rotaion_Status == 3 and Current_Shape[0] % 10 == 0 and Current_Shape[2] % 10 == 0:

                    Current_Shape[0] += 1
                    Current_Shape[1] += 1
                    Current_Shape[2] += 1
                    Current_Shape[3] += 1

                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 11)] == 0:

                    Rotaion_Status = 1
                    Current_Shape[0] -= 9
                    Current_Shape[2] += 9
                    Current_Shape[3] -= 11

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 9)] == 0:

                    Rotaion_Status = 2
                    Current_Shape[0] += 11
                    Current_Shape[2] -= 11
                    Current_Shape[3] -= 9

                elif Rotaion_Status == 2 and Block_Grid_Color_Boolean[(Current_Shape[0] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 11)] == 0:

                    Rotaion_Status = 3
                    Current_Shape[0] += 9
                    Current_Shape[2] -= 9
                    Current_Shape[3] += 11

                elif Rotaion_Status == 3 and Block_Grid_Color_Boolean[(Current_Shape[0] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 9)] == 0:

                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] += 11
                    Current_Shape[3] += 9

            if Current_Shape_Randomizer == 4:

                if Rotaion_Status == 3 and Current_Shape[1] % 10 == 9 and Current_Shape[3] % 10 == 9:

                    Current_Shape[0] -= 1
                    Current_Shape[1] -= 1
                    Current_Shape[2] -= 1
                    Current_Shape[3] -= 1

                if Rotaion_Status == 1 and Current_Shape[1] % 10 == 0 and Current_Shape[3] % 10 == 0:

                    Current_Shape[0] += 1
                    Current_Shape[1] += 1
                    Current_Shape[2] += 1
                    Current_Shape[3] += 1

                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 2)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 9)] == 0:

                    Rotaion_Status = 1
                    Current_Shape[0] += 2
                    Current_Shape[1] -= 9
                    Current_Shape[3] += 9

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0] + 20)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 11)] == 0:

                    Rotaion_Status = 2
                    Current_Shape[0] += 20
                    Current_Shape[1] += 11
                    Current_Shape[3] -= 11

                elif Rotaion_Status == 2 and Block_Grid_Color_Boolean[(Current_Shape[0] - 2)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 9)] == 0:

                    Rotaion_Status = 3
                    Current_Shape[0] -= 2
                    Current_Shape[1] += 9
                    Current_Shape[3] -= 9

                elif Rotaion_Status == 3 and Block_Grid_Color_Boolean[(Current_Shape[0] - 20)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 11)] == 0:

                    Rotaion_Status = 0
                    Current_Shape[0] -= 20
                    Current_Shape[1] -= 11
                    Current_Shape[3] += 11

            if Current_Shape_Randomizer == 5:

                if Rotaion_Status == 3 and Current_Shape[1] % 10 == 9 and Current_Shape[3] % 10 == 9:

                    Current_Shape[0] -= 1
                    Current_Shape[1] -= 1
                    Current_Shape[2] -= 1
                    Current_Shape[3] -= 1

                if Rotaion_Status == 1 and Current_Shape[1] % 10 == 0 and Current_Shape[3] % 10 == 0:

                    Current_Shape[0] += 1
                    Current_Shape[1] += 1
                    Current_Shape[2] += 1
                    Current_Shape[3] += 1

                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 20)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 9)] == 0:

                    Rotaion_Status = 1
                    Current_Shape[0] += 20
                    Current_Shape[1] += 9
                    Current_Shape[3] -= 9
                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0] - 2)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 11)] == 0:

                    Rotaion_Status = 2
                    Current_Shape[0] -= 2
                    Current_Shape[1] -= 11
                    Current_Shape[3] += 11

                elif Rotaion_Status == 2 and Block_Grid_Color_Boolean[(Current_Shape[0] - 20)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 9)] == 0:

                    Rotaion_Status = 3
                    Current_Shape[0] -= 20
                    Current_Shape[1] -= 9
                    Current_Shape[3] += 9

                elif Rotaion_Status == 3 and Block_Grid_Color_Boolean[(Current_Shape[0] + 2)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 11)] == 0:

                    Rotaion_Status = 0
                    Current_Shape[0] += 2
                    Current_Shape[1] += 11
                    Current_Shape[3] -= 11

            if Current_Shape_Randomizer == 6:

                if Rotaion_Status == 1 and Current_Shape[1] % 10 == 9 and Current_Shape[1] % 10 == 9:

                    Current_Shape[0] -= 1
                    Current_Shape[1] -= 1
                    Current_Shape[2] -= 1
                    Current_Shape[3] -= 1

                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 2)] == 0:

                    Rotaion_Status = 1
                    Current_Shape[0] += 11
                    Current_Shape[2] += 9
                    Current_Shape[3] -= 2

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 2)] == 0:

                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] -= 9
                    Current_Shape[3] += 2

            if Current_Shape_Randomizer == 7:

                if Rotaion_Status == 0 and Current_Shape[1] < 10:

                    Current_Shape[0] += 10
                    Current_Shape[1] += 10
                    Current_Shape[2] += 10
                    Current_Shape[3] += 10

                if Rotaion_Status == 1 and Current_Shape[1] % 10 == 0 and Current_Shape[1] % 10 == 0:

                    Current_Shape[0] += 1
                    Current_Shape[1] += 1
                    Current_Shape[2] += 1
                    Current_Shape[3] += 1

                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 20)] == 0:

                    Rotaion_Status = 1
                    Current_Shape[0] += 11
                    Current_Shape[2] -= 9
                    Current_Shape[3] -= 20

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 20)] == 0:

                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] += 9
                    Current_Shape[3] += 20

        if Anti_Rotation_Manager_Boolean == 0:

            Anti_Rotation_Manager_Boolean = 1
            SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "rot.wav"))
            if SFX_Settings == 1:

                SFX.play()

            if Current_Shape_Randomizer == 1:

                if Rotaion_Status == 0 and Current_Shape[0] < 10:

                    Current_Shape[0] += 10
                    Current_Shape[1] += 10
                    Current_Shape[2] += 10
                    Current_Shape[3] += 10

                if Rotaion_Status == 1 and Current_Shape[0] % 10 == 9 and Current_Shape[2] % 10 == 9:

                    Current_Shape[0] -= 2
                    Current_Shape[1] -= 2
                    Current_Shape[2] -= 2
                    Current_Shape[3] -= 2

                if Rotaion_Status == 1 and Current_Shape[0] % 10 == 0 and Current_Shape[2] % 10 == 0:

                    Current_Shape[0] += 1
                    Current_Shape[1] += 1
                    Current_Shape[2] += 1
                    Current_Shape[3] += 1

                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 10)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 10)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 20)] == 0:

                    Current_Shape[0] -= 9
                    Current_Shape[1] += 0
                    Current_Shape[2] += 9
                    Current_Shape[3] += 18
                    Rotaion_Status = 1

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[1] - 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 2)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 1)] == 0:

                    Current_Shape[0] += 9
                    Current_Shape[1] -= 0
                    Current_Shape[2] -= 9
                    Current_Shape[3] -= 18
                    Rotaion_Status = 0
                Current_Shape_Randomizer = 1

            if Current_Shape_Randomizer == 3:

                if Rotaion_Status == 0 and Current_Shape[1] < 10:

                    Current_Shape[0] += 10
                    Current_Shape[1] += 10
                    Current_Shape[2] += 10
                    Current_Shape[3] += 10

                if Rotaion_Status == 1 and Current_Shape[0] % 10 == 9 and Current_Shape[2] % 10 == 9:

                    Current_Shape[0] -= 1
                    Current_Shape[1] -= 1
                    Current_Shape[2] -= 1
                    Current_Shape[3] -= 1

                if Rotaion_Status == 3 and Current_Shape[0] % 10 == 0 and Current_Shape[2] % 10 == 0:

                    Current_Shape[0] += 1
                    Current_Shape[1] += 1
                    Current_Shape[2] += 1
                    Current_Shape[3] += 1

                if Rotaion_Status == 3 and Block_Grid_Color_Boolean[(Current_Shape[0] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 11)] == 0:

                    Rotaion_Status = 2
                    Current_Shape[0] -= 9
                    Current_Shape[2] += 9
                    Current_Shape[3] -= 11

                elif Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 9)] == 0:

                    Rotaion_Status = 3
                    Current_Shape[0] += 11
                    Current_Shape[2] -= 11
                    Current_Shape[3] -= 9

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 11)] == 0:

                    Rotaion_Status = 0
                    Current_Shape[0] += 9
                    Current_Shape[2] -= 9
                    Current_Shape[3] += 11

                elif Rotaion_Status == 2 and Block_Grid_Color_Boolean[(Current_Shape[0] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 9)] == 0:

                    Rotaion_Status = 1
                    Current_Shape[0] -= 11
                    Current_Shape[2] += 11
                    Current_Shape[3] += 9

            if Current_Shape_Randomizer == 4:

                if Rotaion_Status == 3 and Current_Shape[1] % 10 == 9 and Current_Shape[3] % 10 == 9:

                    Current_Shape[0] -= 1
                    Current_Shape[1] -= 1
                    Current_Shape[2] -= 1
                    Current_Shape[3] -= 1

                if Rotaion_Status == 1 and Current_Shape[1] % 10 == 0 and Current_Shape[3] % 10 == 0:

                    Current_Shape[0] += 1
                    Current_Shape[1] += 1
                    Current_Shape[2] += 1
                    Current_Shape[3] += 1

                if Rotaion_Status == 3 and Block_Grid_Color_Boolean[(Current_Shape[0] + 2)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 9)] == 0:

                    Rotaion_Status = 2
                    Current_Shape[0] += 2
                    Current_Shape[1] -= 9
                    Current_Shape[3] += 9

                elif Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 20)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 11)] == 0:

                    Rotaion_Status = 3
                    Current_Shape[0] += 20
                    Current_Shape[1] += 11
                    Current_Shape[3] -= 11

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0] - 2)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 9)] == 0:

                    Rotaion_Status = 0
                    Current_Shape[0] -= 2
                    Current_Shape[1] += 9
                    Current_Shape[3] -= 9

                elif Rotaion_Status == 2 and Block_Grid_Color_Boolean[(Current_Shape[0] - 20)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 11)] == 0:

                    Rotaion_Status = 1
                    Current_Shape[0] -= 20
                    Current_Shape[1] -= 11
                    Current_Shape[3] += 11

            if Current_Shape_Randomizer == 5:

                if Rotaion_Status == 3 and Current_Shape[1] % 10 == 9 and Current_Shape[3] % 10 == 9:

                    Current_Shape[0] -= 1
                    Current_Shape[1] -= 1
                    Current_Shape[2] -= 1
                    Current_Shape[3] -= 1

                if Rotaion_Status == 1 and Current_Shape[1] % 10 == 0 and Current_Shape[3] % 10 == 0:

                    Current_Shape[0] += 1
                    Current_Shape[1] += 1
                    Current_Shape[2] += 1
                    Current_Shape[3] += 1

                if Rotaion_Status == 3 and Block_Grid_Color_Boolean[(Current_Shape[0] + 20)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 9)] == 0:

                    Rotaion_Status = 2
                    Current_Shape[0] += 20
                    Current_Shape[1] += 9
                    Current_Shape[3] -= 9

                elif Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] - 2)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 11)] == 0:

                    Rotaion_Status = 3
                    Current_Shape[0] -= 2
                    Current_Shape[1] -= 11
                    Current_Shape[3] += 11

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0] - 20)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 9)] == 0:

                    Rotaion_Status = 0
                    Current_Shape[0] -= 20
                    Current_Shape[1] -= 9
                    Current_Shape[3] += 9

                elif Rotaion_Status == 2 and Block_Grid_Color_Boolean[(Current_Shape[0] + 2)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 11)] == 0:

                    Rotaion_Status = 1
                    Current_Shape[0] += 2
                    Current_Shape[1] += 11
                    Current_Shape[3] -= 11

            if Current_Shape_Randomizer == 6:

                if Rotaion_Status == 1 and Current_Shape[1] % 10 == 9 and Current_Shape[1] % 10 == 9:

                    Current_Shape[0] -= 1
                    Current_Shape[1] -= 1
                    Current_Shape[2] -= 1
                    Current_Shape[3] -= 1

                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 2)] == 0:

                    Rotaion_Status = 1
                    Current_Shape[0] += 11
                    Current_Shape[2] += 9
                    Current_Shape[3] -= 2

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 2)] == 0:

                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] -= 9
                    Current_Shape[3] += 2

            if Current_Shape_Randomizer == 7:

                if Rotaion_Status == 0 and Current_Shape[1] < 10:

                    Current_Shape[0] += 10
                    Current_Shape[1] += 10
                    Current_Shape[2] += 10
                    Current_Shape[3] += 10

                if Rotaion_Status == 1 and Current_Shape[1] % 10 == 0 and Current_Shape[1] % 10 == 0:

                    Current_Shape[0] += 1
                    Current_Shape[1] += 1
                    Current_Shape[2] += 1
                    Current_Shape[3] += 1

                if Rotaion_Status == 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 20)] == 0:

                    Rotaion_Status = 1
                    Current_Shape[0] += 11
                    Current_Shape[2] -= 9
                    Current_Shape[3] -= 20

                elif Rotaion_Status == 1 and Block_Grid_Color_Boolean[(Current_Shape[0] - 11)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 9)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 20)] == 0:

                    Rotaion_Status = 0
                    Current_Shape[0] -= 11
                    Current_Shape[2] += 9
                    Current_Shape[3] += 20

        font = pygame.font.Font(os.path.join("Assets", "Fonts", 'OCRAEXT.ttf'), 3 * block_height // 4)
        fpss = f'{clock.get_fps():.0f} FPS'
        text = font.render(str(Score), True, (218, 163, 150))
        trex = text.get_rect()
        trex.center = (int(((16.65 + Block_X_No) * block_width)), int(0.7 * height) + 3 * block_height // 4)
        w.blit(text, trex)

        keypress = pygame.key.get_pressed()
        if (keypress[pygame.K_a] or TA == 1 or keypress[pygame.K_LEFT]) and (Left_Movement_Clock >= Left_Movement_Clock_Frequency or checker > 0) and (Current_Shape[0]) % Block_X_No != 0 and (Current_Shape[1]) % Block_X_No != 0 and (Current_Shape[2]) % Block_X_No != 0 and (Current_Shape[3]) % Block_X_No != 0 and Block_Grid_Color_Boolean[(Current_Shape[0] - 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] - 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] - 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] - 1)] == 0:

            ijx = 0
            TA = 0
            Left_Movement_Clock = 0
            SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "move.wav"))
            if SFX_Settings == 1:

                SFX.play()

            while ijx < 4:

                Current_Shape[ijx] -= 1
                ijx += 1

        if (keypress[pygame.K_d] or TD == 1 or keypress[pygame.K_RIGHT]) and (Right_Movement_Clock >= Right_Movement_Clock_Frequency or checker > 0) and (Current_Shape[0] - 9) % Block_X_No != 0 and (Current_Shape[1] - 9) % Block_X_No != 0 and (Current_Shape[2] - 9) % Block_X_No != 0 and (Current_Shape[3] - 9) % Block_X_No != 0 and Block_Grid_Color_Boolean[(Current_Shape[0] + 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1] + 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2] + 1)] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3] + 1)] == 0:

            ijx = 0
            TD = 0
            Right_Movement_Clock = 0
            SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "move.wav"))
            if SFX_Settings == 1:

                SFX.play()

            while ijx < 4:

                Current_Shape[ijx] += 1
                ijx += 1

        while lm < Block_Y_No:

            j = 0
            lm += 1

            while j < Block_X_No:

                if Block_Grid_Color_Boolean[BGC_Grid_Color_Matcher] != 0 and checker == 0:

                    if (Stop_Current_Shape_Movement != 0 and Block_Grid_Color_Boolean[(Current_Shape[0])] != 0 and Block_Grid_Color_Boolean[(Current_Shape[1])] != 0 and Block_Grid_Color_Boolean[(Current_Shape[2])] != 0 and Block_Grid_Color_Boolean[(Current_Shape[3])] != 0 and ((3 < Current_Shape[0] < 6 or 3 < Current_Shape[1] < 6) or (3 < Current_Shape[2] < 6 or 3 < Current_Shape[3] < 6))):

                        Block_Grid_Color = Block_Grid_Red

                    elif Block_Grid_Color_Boolean[BGC_Grid_Color_Matcher] == 1:

                        Block_Grid_Color = (26, 194, 241)

                    elif Block_Grid_Color_Boolean[BGC_Grid_Color_Matcher] == 2:

                        Block_Grid_Color = (253, 223, 102)

                    elif Block_Grid_Color_Boolean[BGC_Grid_Color_Matcher] == 3:

                       Block_Grid_Color = (151, 59, 152)

                    elif Block_Grid_Color_Boolean[BGC_Grid_Color_Matcher] == 4:

                        Block_Grid_Color = (0, 131, 196)

                    elif Block_Grid_Color_Boolean[BGC_Grid_Color_Matcher] == 5:

                        Block_Grid_Color = (247, 160, 67)

                    elif Block_Grid_Color_Boolean[BGC_Grid_Color_Matcher] == 6:

                        Block_Grid_Color = (148, 202, 100)

                    elif Block_Grid_Color_Boolean[BGC_Grid_Color_Matcher] == 7:

                        Block_Grid_Color = (238, 69, 51)

                    pygame.draw.rect(w, Block_Grid_Free_Color, ((Block_Grid_X[j]), Block_Grid_Y[(lm - 1)], block_width, block_height),int(block_width / 40), int(block_height / 8))
                    pygame.draw.rect(w, Block_Grid_Color, ((Block_Grid_X[j]) + int(block_width / 20), Block_Grid_Y[(lm - 1)] + int(block_height / 20), int(9 * block_width / 10),int(9 * block_height / 10)), 28 * int(block_width / 40), int(block_height / 8))

                j += 1
                BGC_Grid_Color_Matcher += 1

        if Stop_Current_Shape_Movement == 0:

            ng = Ghost[0]
            mvm4(ng)
            ng = Ghost[1]
            mvm4(ng)
            ng = Ghost[2]
            mvm4(ng)
            ng = Ghost[3]
            mvm4(ng)

        if (Stop_Current_Shape_Movement == 0 or Buffer != 0) and Block_Grid_Color_Boolean[(Current_Shape[0])] == 0 and Block_Grid_Color_Boolean[(Current_Shape[1])] == 0 and Block_Grid_Color_Boolean[(Current_Shape[2])] == 0 and Block_Grid_Color_Boolean[(Current_Shape[3])] == 0:

            ng = Current_Shape[0]
            mvm3(ng)
            ng = Current_Shape[1]
            mvm3(ng)
            ng = Current_Shape[2]
            mvm3(ng)
            ng = Current_Shape[3]
            mvm3(ng)

        if Shape_Hold_Number != 0:

            ng = Shape_Hold[0]
            mvm2(ng)
            ng = Shape_Hold[1]
            mvm2(ng)
            ng = Shape_Hold[2]
            mvm2(ng)
            ng = Shape_Hold[3]
            mvm2(ng)

        if Stop_Current_Shape_Movement == 0 or Buffer != 0:

            ng = Next_Shape[0]
            mvm(ng)
            ng = Next_Shape[1]
            mvm(ng)
            ng = Next_Shape[2]
            mvm(ng)
            ng = Next_Shape[3]
            mvm(ng)
        if Buffer != 0:

            Buffer -= 1
            Rotation_Clock = Rotation_Frequency
            IMD_Movement_Clock = IMD_Movement_Clock_Frequency
            Down_Movement_Clock = Down_Movement_Clock_Frequency
            Left_Movement_Clock = Left_Movement_Clock_Frequency
            Right_Movement_Clock = Right_Movement_Clock_Frequency

        if Buffer == 1:

            SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "land.wav"))
            if SFX_Settings == 1:

                SFX.play()

        if keypress[pygame.K_p] or TP == 1:

            pause = 1
            disp = ""
            TP = 0
            run = False
            video = cv2.VideoCapture("Assets/Pause Screen/Pause Start.mp4")
            success, video_image = video.read()
            if Music_Settings != 0 and BGM_Game_Playing2.get_volume() == 0:

                BGM_Game_Playing.set_volume(0)

            elif Music_Settings != 0 and BGM_Game_Playing2.get_volume() != 0:

                BGM_Game_Playing2.set_volume(0)

            SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "pause.wav"))
            if SFX_Settings == 1:

                SFX.play()

            BGM_Paused = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "paused.wav"))
            click = 0
            spaceb = 0
            dec = 0
            tnx = 0
            Space_Bar_Timer = 0
            Image_No2 = 30
            if Music_Settings != 0:

                BGM_Paused.play(loops=-1)

            while pause == 1:

                Mouse_Loc = pygame.mouse.get_pos()
                clock.tick(60)
                Space_Bar_Timer += 1
                Image_No2 += 1
                if Image_No2 == 1000:

                    Image_No2 = 701

                if Space_Bar_Timer == 11:

                    spaceb = 1

                if tnx < FPS + 1:

                    tnx += 1

                if tnx > FPS:

                    tnx = 0

                success, video_image = video.read(1)
                if success:

                    video_surf = pygame.image.frombuffer(video_image.tobytes(), video_image.shape[1::-1], "BGR")

                else:

                    video = cv2.VideoCapture("Assets/Pause Screen/Pause.mp4")

                if not run:

                    w.blit(pygame.transform.smoothscale(video_surf, (width, height)), (0, 0))

                font = pygame.font.Font(os.path.join("Assets", "Fonts", 'OCRAEXT.ttf'), block_height)
                text = font.render(str(Score), True, (209, 174, 238))
                trex = text.get_rect()
                if Image_No2 >= 520:

                    trex.center = (22.624 * block_width, height // 3 + block_height // 10)
                    w.blit(text, trex)

                if visi == 1:

                    pygame.draw.rect(w, (44, 46, 106), ((width // 2 - width // 17 - 3.5 * block_width), (height // 2 - height // 6), 2 * width // 17 + 7 * block_width, height // 3), 3 * block_height, int(block_height // 4))
                    pygame.draw.rect(w, (209, 174, 238), ((width // 2 + width // 25), (4 * height // 7), 3 * block_width, block_height), block_height // 2, int(block_height // 4))
                    pygame.draw.rect(w, (209, 174, 238), (int(width // 2 + width // 25 + 0.1 * block_width), (401 * height // 700), int(2.3 * block_height), 9 * block_height // 10))
                    pygame.draw.rect(w, (209, 174, 238), ((width // 2 - width // 25 - 3 * block_width), (4 * height // 7), 3 * block_width, block_height), block_height // 2, int(block_height / 4))
                    pygame.draw.rect(w, (209, 174, 238), (int(width // 2 - width // 25 - 2.8 * block_width), (401 * height // 700), int(2.3 * block_height), 9 * block_height // 10))
                    pygame.draw.rect(w, (44, 46, 106), ((width // 2 - 3 * block_width), (height // 2 - height // 8), 6 * block_height, height // 6), 3 * block_height, int(block_height))
                    font = pygame.font.Font('freesansbold.ttf', 7 * block_height // 10)
                    text = font.render('Are You Sure', True, (209, 174, 238))
                    trex = text.get_rect()
                    trex.center = (width // 2, 3 * height // 7)
                    w.blit(text, trex)
                    text = font.render('You Want to Exit?', True, (209, 174, 238))
                    trex = text.get_rect()
                    trex.center = (width // 2, 3 * height // 7 + block_height)
                    w.blit(text, trex)
                    font = pygame.font.Font('freesansbold.ttf', 4 * block_height // 10)
                    text = font.render('All Unsaved Data Will Be Lost', True, (231, 101, 106))
                    trex = text.get_rect()
                    trex.center = (width // 2, 3 * height // 7 + 19 * block_height // 10)
                    w.blit(text, trex)
                    font = pygame.font.Font('freesansbold.ttf', 6 * block_height // 10)
                    text = font.render('   NO', True, (44, 46, 106))
                    trex = text.get_rect()
                    trex.topleft = (width // 2 + width // 17 - block_width // 35, 4 * height // 7 + block_height // 5)
                    w.blit(text, trex)
                    text = font.render('YES', True, (44, 46, 106))
                    trex = text.get_rect()
                    trex.topright = (width // 2 - width // 16 - block_width // 5, 4 * height // 7 + block_height // 5)
                    w.blit(text, trex)
                    if click == 1:

                        click = 0

                        if 4 * height // 7 < Mouse_Loc[1] < 4 * height // 7 + 9 * block_height // 10:

                            if int(width // 2 + width // 25) < Mouse_Loc[0] < int(width // 2 + width // 25) + 3 * block_width:

                                visi = 0

                            elif (width // 2 - width // 25 - 3 * block_width) < Mouse_Loc[0] < (width // 2 - width // 25 - 3 * block_width) + 3 * block_width:

                                visi = 0
                                dec = 1

                    if dec == 1:

                        run = False
                        pause = 0
                        exit_sequence = 1

                if visi == 2:
                    pygame.draw.rect(w, (44, 46, 106), ((width // 2 - width // 17 - 3.5 * block_width), (height // 2 - height // 6), 2 * width // 17 + 7 * block_width, height // 3), 3 * block_height, int(block_height // 4))
                    pygame.draw.rect(w, (209, 174, 238), ((width // 2 + width // 25), (4 * height // 7), 3 * block_width, block_height), block_height // 2, int(block_height // 4))
                    pygame.draw.rect(w, (209, 174, 238), (int(width // 2 + width // 25 + 0.1 * block_width), (401 * height // 700), int(2.3 * block_height), 9 * block_height // 10))
                    pygame.draw.rect(w, (209, 174, 238), ((width // 2 - width // 25 - 3 * block_width), (4 * height // 7), 3 * block_width, block_height), block_height // 2, int(block_height / 4))
                    pygame.draw.rect(w, (209, 174, 238), (int(width // 2 - width // 25 - 0.1 * block_width - int(2.7 * block_width)), (401 * height // 700), int(2.3 * block_height), 9 * block_height // 10))
                    pygame.draw.rect(w, (44, 46, 106), ((width // 2 - 3 * block_width), (height // 2 - height // 8), 6 * block_height, height // 6), 3 * block_height, int(block_height // 4))
                    font = pygame.font.Font('freesansbold.ttf', 7 * block_height // 10)
                    text = font.render('Return to', True, (209, 174, 238))
                    trex = text.get_rect()
                    trex.center = (width // 2, 3 * height // 7)
                    w.blit(text, trex)
                    text = font.render('the Main Menu?', True, (209, 174, 238))
                    trex = text.get_rect()
                    trex.center = (width // 2, 3 * height // 7 + block_height)
                    w.blit(text, trex)
                    font = pygame.font.Font('freesansbold.ttf', 4 * block_height // 10)
                    text = font.render('All Unsaved Data Will Be Lost', True, (231, 101, 106))
                    trex = text.get_rect()
                    trex.center = (width // 2, 3 * height // 7 + 19 * block_height // 10)
                    w.blit(text, trex)
                    font = pygame.font.Font('freesansbold.ttf', 6 * block_height // 10)
                    text = font.render('   NO', True, (44, 46, 106))
                    trex = text.get_rect()
                    trex.topleft = (width // 2 + width // 17 - block_width // 35, 4 * height // 7 + block_height // 5)
                    w.blit(text, trex)
                    text = font.render('YES', True, (44, 46, 106))
                    trex = text.get_rect()
                    trex.topright = (width // 2 - width // 16 - block_width // 5, 4 * height // 7 + block_height // 5)
                    w.blit(text, trex)
                    if click == 1:

                        click = 0
                        if 4 * height // 7 < Mouse_Loc[1] < 4 * height // 7 + 9 * block_height // 10:

                            if int(width // 2 + width // 25) < Mouse_Loc[0] < int(width // 2 + width // 25) + 3 * block_width:

                                visi = 0

                            elif (width // 2 - width // 25 - 3 * block_width) < Mouse_Loc[0] < (width // 2 - width // 25 - 3 * block_width) + 3 * block_width:

                                visi = 0
                                dec = 1

                    if dec == 1:

                        run = False
                        pause = 0
                        exit_sequence = 3

                if height // block_height < Mouse_Loc[1] < block_height + block_height // 5 and 0.333 * block_width < Mouse_Loc[0] < block_width + block_width // 5 and click == 1:

                    visi = 1

                keypress = pygame.key.get_pressed()
                pygame.display.update()
                if click == 1:

                    click = 0
                    if 13.6 * block_height < Mouse_Loc[1] < 15.25 * block_height:

                        if 25.3 * block_width < Mouse_Loc[0] < 29.5 * block_width:

                            run = True
                            pause = 0

                        elif (15.75 * block_width) < Mouse_Loc[0] < 19.92 * block_width:

                            visi = 2

                for event in pygame.event.get():

                    if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:

                        visi = 1

                    if keypress[pygame.K_p] and spaceb == 1:

                        run = True
                        pause = 0

                    if event.type == pygame.MOUSEBUTTONUP and event:

                        click = 1

            pygame.init()
            BGM_Paused.fadeout(1)
            Image_No = 1
            SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "pause.wav"))
            if SFX_Settings == 1:

                SFX.play()

            if Music_Settings != 0 and Score < 100000:

                BGM_Game_Playing.set_volume(1)

            elif Score > 100000 and Music_Settings != 0:

                BGM_Game_Playing2.set_volume(1)

        pygame.display.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT or keypress[pygame.K_ESCAPE]:

                TP = 1
                visi = 1

            if event.type == pygame.MOUSEBUTTONUP and comp == 0:

                if width // 2 - (Block_X_No / 2) * block_width < Mouse_Loc[0] < width // 2 + (Block_X_No / 2) * block_width and Mouse_Loc[1] < height:

                    TS = 1

                if Mouse_Loc[0] < width // 2 - (Block_X_No / 2) * block_width and Mouse_Loc[1] < height:

                    if Mouse_Loc[1] < height // 7:

                        run = False
                        exit_sequence = 1

                    elif Mouse_Loc[1] < 4 * height // 7:

                        TW = 1

                    elif Mouse_Loc[0] < (width // 2 - Block_X_No // 2 * block_width) / 2:

                        TA = 1

                    else:

                        TD = 1

                elif width > Mouse_Loc[0] > width // 2 + (Block_X_No / 2) * block_width and Mouse_Loc[1] < height:

                    if Mouse_Loc[1] < height // 7:

                        TP = 1

                    else:

                        TR = 1
    click = 0

    if Score >= High_Score and exit_sequence != 1:

        doc = open(os.path.join("Assets", "Data", "Variables.txt"), "w+")
        L[4] = str(Score) + "\n"
        doc.writelines(L)
        doc.close()

    resetg = 0
    if Music_Settings != 0:

        BGM_Game_Playing.set_volume(0)
        BGM_Game_Playing2.set_volume(0)

    if Music_Settings != 0:

        BGM_Game_Playing.stop()
        BGM_Game_Playing2.stop()

    if exit_sequence == 3:

        resetg = 1
        load = 0
        xo = 6 * block_height
        Loading(load, xo)

    if exit_sequence == 1:

        resetg = 1
        Ending()

    if endmusicclock == 1:

        SFX = pygame.mixer.Sound(os.path.join("Assets", "Music and SFX", "go.wav"))
        if SFX_Settings == 1:

            SFX.play()

        while endmusicclock < 4:

            clock.tick(1)
            endmusicclock += 1

    if Music_Settings != 0:

        BGM_End_Screen.play(loops=-1)

    disp = ""
    Image_No = 0
    tsk = 0

    if exit_sequence != 0:

        run = True

    video = cv2.VideoCapture("Assets/End Screen/End Start.mp4")
    success, video_image = video.read()
    while not run:

        Mouse_Loc = pygame.mouse.get_pos()
        clock.tick(40)
        Image_No += 1 + randint(0, 1)
        success, video_image = video.read(1)
        if success:

            video_surf = pygame.image.frombuffer(video_image.tobytes(), video_image.shape[1::-1], "BGR")
        else:

            video = cv2.VideoCapture("Assets/End Screen/End.mp4")

        w.blit(pygame.transform.smoothscale(video_surf, (width, height)), (0, 0))
        font = pygame.font.Font(os.path.join("Assets", "Fonts", 'OCRAEXT.ttf'), block_height + block_height // 2)
        text = font.render(str(Score), True, (183, 79, 69))
        trex = text.get_rect()
        trex.center = (width // 2, 8 * block_height)
        w.blit(text, trex)
        if 0.416 * block_height < Mouse_Loc[1] < 1.25 * block_height and 0.416 * block_width < Mouse_Loc[0] < 1.25 * block_width and click == 1:

            run = True
            exit_sequence = 1

        if click == 1:

            click = 0
            if 13.17 * block_height < Mouse_Loc[1] < 15.33 * block_height:

                if 8.66 * block_width < Mouse_Loc[0] < 14 * block_width:

                    run = True
                    exit_sequence = 3

                elif height < Mouse_Loc[0] < 23.34 * block_width:
                    run = True
                    exit_sequence = 2

        pygame.display.update()
        keypress = pygame.key.get_pressed()
        for event in pygame.event.get():

            if keypress[pygame.K_ESCAPE] or event.type == pygame.QUIT:

                run = True
                exit_sequence = 1

            if keypress[pygame.K_p]:

                run = True
                exit_sequence = 2

            if event.type == pygame.MOUSEBUTTONUP:

                click = 1

    if Music_Settings != 0:

        BGM_End_Screen.set_volume(0)

    if Music_Settings != 0:

        BGM_End_Screen.stop()

    if (exit_sequence == 3 or exit_sequence == 2) and resetg == 0:

        load = 0
        xo = 6 * block_height
        Loading(load, xo)

    if exit_sequence == 1 and resetg == 0:

        Ending()

    return exit_sequence


def Loading(load, xo):

    image = pygame.image.load(os.path.join("Assets", "Data", "LOAD.png"))
    w.blit(pygame.transform.smoothscale(image, (width, height)), (0, 0))
    while load < 61 and Mod_Access_Blocked == 1:

        load += 1
        clock.tick(60)
        w.blit(pygame.transform.smoothscale(image, (width, height)), (0, 0))
        if xo > block_height // 8:

            xo = 6 * block_height - int(load / 5 * (6 * block_height // 12))

        pygame.draw.rect(w, (255, 255, 255),(width // 2 - 3 * block_height - block_height // 8, 2 * height // 5 - block_height // 8, 6 * block_height + block_height // 4, block_height + block_height // 4), 2,block_height // 8)
        pygame.draw.rect(w, (255, 255, 255), (width // 2 - 3 * block_height, 2 * height // 5, 6 * block_height - xo, block_height))
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height / 25))

        if load % 9 <= 2:

            text = font.render("LOADING.", True, (255, 255, 255))

        elif load % 9 <= 5:

            text = font.render("LOADING..", True, (255, 255, 255))

        else:

            text = font.render("LOADING...", True, (255, 255, 255))

        trex = text.get_rect()
        trex.midleft = (width // 2 - 2 * block_height + block_height // 2, 2 * height // 5 + block_height + height // 20)
        w.blit(text, trex)
        pygame.display.update()


def Ending():

    load = 0
    xo = 6 * block_height
    image = pygame.image.load(os.path.join("Assets", "Data", "LOAD2.png"))
    w.blit(pygame.transform.smoothscale(image, (width, height)), (0, 0))
    while load < 59 and Mod_Access_Blocked == 1:

        load += 1
        clock.tick(55)
        w.blit(pygame.transform.smoothscale(image, (width, height)), (0, 0))
        if xo >= 0:

            xo = 6 * block_height - int(load / 5 * (6 * block_height // 12)) - 5

        pygame.draw.rect(w, (255, 255, 255),(width // 2 - 3 * block_height - block_height // 8, 2 * height // 5 - block_height // 8, 6 * block_height + block_height // 4, block_height + block_height // 4), 2,block_height // 8)
        pygame.draw.rect(w, (255, 255, 255), (width // 2 - 3 * block_height, 2 * height // 5, 6 * block_height - xo, block_height))
        font = pygame.font.Font(os.path.join("Assets", "Fonts", "BAUHS93.ttf"), int(height / 25))
        if load <= 20:

            text = font.render("ENDING BACKGROUD PROCESSES", True, (255, 255, 255))

        elif load <= 40:

            text = font.render("CLOSING APPLICATION", True, (255, 255, 255))

        else:

            text = font.render("THANK YOU FOR PLAYING", True, (255, 255, 255))

        trex = text.get_rect()
        trex.center = (width // 2, 2 * height // 5 + block_height + height // 20)
        w.blit(text, trex)
        pygame.display.update()

    pygame.quit()

while esc != 1:

    if esc == 3 or esc == 4:

        esc = Main_Menu()

    if esc == 2 or esc == 0:

        esc = main()

pygame.quit()
