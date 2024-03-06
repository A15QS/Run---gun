import pygame
import pgzrun
import random
import time
WIDTH = 1920
HEIGHT = 1080
TITLE = "Infinite Click"
FPS = 60
#block_1 = Actor("block_1")
#block_2 = Actor("block_2")
#block_3 = Actor("block_3")
#block_4 = Actor("block_4")
#block_5 = Actor("block_5")
#block_6 = Actor("block_6")
#block_7 = Actor("block_7")
#block_8 = Actor("block_8")
#block_9 = Actor("block_9")
#block_10 = Actor("block_10")
#block_11 = Actor("block_11")
#block_12 = Actor("block_12")
#block_13 = Actor("block_13")
#block_14 = Actor("block_14")
#block_15 = Actor("block_15")
#block_16 = Actor("block_16")
blocks=[]
for i in range(16):
    block = Actor("block_"+str(i+1))
    blocks.append(block)
infinite_click = Actor("game_text",(960,150))
quit_game_text = Actor("quit_game_text",(960,410))
quit_text = Actor("quit_text",(960,520))
bg_black = Actor("bg_black")
bg2 = Actor("background_2",(960,540))
bg3 = Actor("background_3",(960,540))
bg4 = Actor("background_4",(960,540))
bg2x2 = Actor("background_2",(-960,540))
bg3x2 = Actor("background_3",(-960,540))
bg4x2 = Actor("background_4",(-960,540))
floor = Actor("floor",(960,540))
floorx2 = Actor("floor",(-960,540))
fur1 = Actor("col_fur_0",(1350,100))
fur2 = Actor("col_fur_1",(1500,100))
fur3 = Actor("col_fur_2",(1650,100))
fur4 = Actor("col_fur_3",(1350,250))
fur5 = Actor("col_fur_4",(1500,250))
fur6 = Actor("col_fur_5",(1650,250))
fur7 = Actor("col_fur_6",(1350,400))
fur8 = Actor("col_fur_7",(1500,400))
fur9 = Actor("col_fur_8",(1650,400))
fur10 = Actor("col_fur_9",(1350,550))
fur11 = Actor("col_fur_10",(1500,550))
fur12 = Actor("col_fur_11",(1650,550))
fur13 = Actor("col_fur_12",(1350,700))
fur14 = Actor("col_fur_13",(1500,700))
fur15 = Actor("col_fur_14",(1650,700))
fur16 = Actor("col_fur_15",(1350,850))
fur17 = Actor("col_fur_16",(1500,850))
fur18 = Actor("col_fur_17",(1650,850))
fur19 = Actor("col_fur_18",(1500,1000))
fur2_locked = Actor("locked_select",(1500,100))
fur3_locked = Actor("locked_select",(1650,100))
fur4_locked = Actor("locked_select",(1350,250))
fur5_locked = Actor("locked_select",(1500,250))
fur6_locked = Actor("locked_select",(1650,250))
fur7_locked = Actor("locked_select",(1350,400))
fur8_locked = Actor("locked_select",(1500,400))
fur9_locked = Actor("locked_select",(1650,400))
fur10_locked = Actor("locked_select",(1350,550))
fur11_locked = Actor("locked_select",(1500,550))
fur12_locked = Actor("locked_select",(1650,550))
fur13_locked = Actor("locked_select",(1350,700))
fur14_locked = Actor("locked_select",(1500,700))
fur15_locked = Actor("locked_select",(1650,700))
fur16_locked = Actor("locked_select",(1350,850))
fur17_locked = Actor("locked_select",(1500,850))
fur18_locked = Actor("locked_select",(1650,850))
fur19_locked = Actor("locked_select",(1500,1000))
hair1 = Actor("col_hair_0",(1350,100))
hair2 = Actor("col_hair_1",(1500,100))
hair3 = Actor("col_hair_2",(1650,100))
hair4 = Actor("col_hair_3",(1350,250))
hair5 = Actor("col_hair_4",(1500,250))
hair6 = Actor("col_hair_5",(1650,250))
hair7 = Actor("col_hair_6",(1350,400))
hair8 = Actor("col_hair_7",(1500,400))
hair9 = Actor("col_hair_8",(1650,400))
hair10 = Actor("col_hair_9",(1350,550))
hair11 = Actor("col_hair_10",(1500,550))
hair12 = Actor("col_hair_11",(1650,550))
hair13 = Actor("col_hair_12",(1350,700))
hair14 = Actor("col_hair_13",(1500,700))
hair15 = Actor("col_hair_14",(1650,700))
hair16 = Actor("col_hair_15",(1350,850))
hair17 = Actor("col_hair_16",(1500,850))
hair18 = Actor("col_hair_17",(1650,850))
hair19 = Actor("col_hair_18",(1350,1000))
hair20 = Actor("col_hair_19",(1500,1000))
hair21 = Actor("col_hair_20",(1650,1000))
hair2_locked = Actor("locked_select",(1500,100))
hair3_locked = Actor("locked_select",(1650,100))
hair4_locked = Actor("locked_select",(1350,250))
hair5_locked = Actor("locked_select",(1500,250))
hair6_locked = Actor("locked_select",(1650,250))
hair7_locked = Actor("locked_select",(1350,400))
hair8_locked = Actor("locked_select",(1500,400))
hair9_locked = Actor("locked_select",(1650,400))
hair10_locked = Actor("locked_select",(1350,550))
hair11_locked = Actor("locked_select",(1500,550))
hair12_locked = Actor("locked_select",(1650,550))
hair13_locked = Actor("locked_select",(1350,700))
hair14_locked = Actor("locked_select",(1500,700))
hair15_locked = Actor("locked_select",(1650,700))
hair16_locked = Actor("locked_select",(1350,850))
hair17_locked = Actor("locked_select",(1500,850))
hair18_locked = Actor("locked_select",(1650,850))
hair19_locked = Actor("locked_select",(1350,1000))
hair20_locked = Actor("locked_select",(1500,1000))
hair21_locked = Actor("locked_select",(1650,1000))
frame_fur = Actor("frame_select_fur",(1350,100))
frame_hair = Actor("frame_select_hair",(1350,100))
frame_hair_col = Actor("frame_select_hair_col",(3350,100))
fur_select = Actor("fur_select_selected",(330,100))
hair_select = Actor("hair_select",(480,100))
play = Actor("button_play",(960,500))
furs = Actor("skins_button",(600,500))
missions = Actor("missions_button",(1320,500))
bonus_1 = Actor("bonus_red",(1500,200))
bonus_2 = Actor("bonus_red",(1500,540))
bonus_3 = Actor("bonus_blue",(1500,880))
bg_missions = Actor("missions_bg",(960,540))
achievements = Actor("achievements_button",(760,980))
settings = Actor("settings_button",(960,980))
stats = Actor("stats_button",(1160,980))
coin = Actor("coin1",(150,920))
cross = Actor("cross",(50,50))
bg_color = Actor("bg_select-color",(1500,540))
#skins
player = Actor("fur_skin_0_sprite_1",(480,540))
sweater_player = Actor("sweater_0_1",(480,540))
pants_player = Actor("pants_0",(480,540))
sneakers_player = Actor("sneakers_0",(480,540))
hair_player = Actor("hair_0",(480,412))
#player
pj = Actor("fur_play_0_1",(300,540))
mr_riv = Actor("mr_riv1",(700,540))
pointer = Actor("pointer",(300,300))
screen_quit = Actor("screen_quit",(960,540))
settings_bg = Actor("settings_bg",(960,-540))
screen_color = Actor("screen_color",(960,540))
back_button = Actor("back_button",(50,50))
mini_back_button = Actor("back_button",(150,140))
cancel_exit = Actor("button_exit_2",(840,650))
yes_quit = Actor("button_exit",(1130,650))
select_missions = Actor("bonus_red",(960,240))
select_missions2 = Actor("bonus_red",(960,540))
select_missions3 = Actor("bonus_blue",(960,840))
locked_secret = Actor("padlock_locked",(1770,140))
locked_secret_cyl = Actor("padlock_cylinder",(1770,140))
charge_im = Actor("charge_bar_0",(960,680))
rope = Actor("rope_shop",(900,115))
coin_shop_1 = Actor("coin_shop",(960,680))
object_shop_1 = Actor("col_fur_1",(210,300))
object_shop_2 = Actor("col_fur_2",(360,300))
object_shop_3 = Actor("col_fur_3",(510,300))
object_shop_4 = Actor("col_fur_5",(660,300))
object_shop_5 = Actor("col_fur_6",(210,450))
object_shop_6 = Actor("col_fur_7",(360,450))
object_shop_7 = Actor("col_fur_8",(510,450))
object_shop_8 = Actor("col_fur_9",(660,450))
object_shop_9 = Actor("col_fur_10",(210,600))
object_shop_10 = Actor("col_fur_11",(360,600))
object_shop_11 = Actor("col_fur_12",(510,600))
object_shop_12 = Actor("col_fur_13",(660,600))
object_shop_13 = Actor("col_fur_14",(210,750))
object_shop_14 = Actor("col_fur_15",(360,750))
object_shop_15 = Actor("col_fur_16",(510,750))
object_shop_16 = Actor("col_fur_17",(660,750))
object_shop_17 = Actor("col_fur_18",(210,900))
object_shop_18 = Actor("col_hair_1",(1260,300))
object_shop_19 = Actor("col_hair_2",(1410,300))
object_shop_20 = Actor("col_hair_3",(1560,300))
object_shop_21 = Actor("col_hair_4",(1710,300))
object_shop_22 = Actor("col_hair_5",(1260,450))
object_shop_23 = Actor("col_hair_6",(1410,450))
object_shop_24 = Actor("col_hair_7",(1560,450))
object_shop_25 = Actor("col_hair_8",(1710,450))
object_shop_26 = Actor("col_hair_9",(1260,600))
object_shop_27 = Actor("col_hair_10",(1410,600))
object_shop_28 = Actor("col_hair_11",(1560,600))
object_shop_29 = Actor("col_hair_12",(1710,600))
object_shop_30 = Actor("col_hair_13",(1260,750))
object_shop_31 = Actor("col_hair_14",(1410,750))
object_shop_32 = Actor("col_hair_15",(1560,750))
object_shop_33 = Actor("col_hair_16",(1710,750))
object_shop_34 = Actor("col_hair_17",(1260,900))
object_shop_35 = Actor("col_hair_18",(1410,900))
object_shop_36 = Actor("col_hair_19",(1560,900))
object_shop_37 = Actor("col_hair_20",(1710,900))
bg_shop = Actor("bg_shop",(960,540))
shop_text = Actor("shop_text",(960,150))
missions_text = Actor("missions_text",(960,150))
coming_soon = Actor("coming_soon",(960,550))
achievements_text = Actor("achievements_text",(960,150))
settings_text = Actor("settings_text",(960,150))
stats_text = Actor("stats_text",(960,150))
how_to_play = Actor("button_settings_how_to_play",(600,400))
graphics = Actor("button_settings_graphics",(1320,400))
opcions = Actor("button_settings_opcions",(960,775))
how_to_play_example = Actor("fur_skin_0_sprite_1",(500,540))
check_screen = Actor("select_button",(960,775))
larrow_button = Actor("larrow",(200,540))
rarrow_button = Actor("rarrow",(1720,540))
how_to_play_text = Actor("how_to_play_text",(960,150))
graphics_text = Actor("graphics_text",(960,150))
opcions_text = Actor("opcions_text",(960,150))
mode = "entry"
mini_mode = ""
state_click = "no"
count = 11400
click = 1
skin_page = 1
lang = "english"
point_s = 0
point_c = 1
number_1 = 1
number_2 = 1
y_number = 510
x_number = 1050
y_numberx2 = 570
x_numberx2 = 1050
y_numberx3 = 540
x_numberx3 = 1050
config = 0
bon_1 = 0
bon_2 = 0
bon_3 = 0
game_time = 0
coins_image = 1
counter = 1
charge = 0
locked_col = 1
text = 0
for_player = 360
mode_of_key = 0
how_to_play_page = 1
how = 360
game = 1
skin = 1
time_pj = 0
direction_pj = 1
move_pj = 0
speed_pj = 1
pj_sweater = 1
old_x = pj.x
old_y = pj.x
enemies = []
my_map = [[ 5, 5, 5, 5, 6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [ 5, 5, 5, 5, 6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [ 5, 5, 5, 5, 6,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [ 9, 9, 9, 9,10,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [ 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3,-1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
          [ 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6,-1, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],
          [ 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6,-1, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],
          [ 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6,-1, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6],
          [ 8, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,10,-1, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 6]]
my_map_to_draw = []
def map_generator_draw():
    for i in range(len(my_map)):
        for j in range(len(my_map)):
            if my_map[i][j] == 0:
                blocks[0]
                blocks[0].left = blocks[0].width*j
                blocks[0].top = blocks[0].height*i
                my_map_to_draw.append(blocks[0])
            if my_map[i][j] == 1:
                blocks[1].left = blocks[1].width*j
                blocks[1].top = blocks[1].height*i
                my_map_to_draw.append(blocks[1])
            if my_map[i][j] == 2:
                blocks[2].left = blocks[2].width*j
                blocks[2].top = blocks[2].height*i
                my_map_to_draw.append(blocks[2])
            if my_map[i][j] == 3:
                blocks[3].left = blocks[3].width*j
                blocks[3].top = blocks[3].height*i
                my_map_to_draw.append(blocks[3])
            if my_map[i][j] == 4:
                blocks[4].left = blocks[4].width*j
                blocks[4].top = blocks[4].height*i
                my_map_to_draw.append(blocks[4])
            if my_map[i][j] == 5:
                blocks[5].left = blocks[5].width*j
                blocks[5].top = blocks[5].height*i
                my_map_to_draw.append(blocks[5])
            if my_map[i][j] == 6:
                blocks[6].left = blocks[6].width*j
                blocks[6].top = blocks[6].height*i
                my_map_to_draw.append(blocks[6])
            if my_map[i][j] == 7:
                blocks[7].left = blocks[7].width*j
                blocks[7].top = blocks[7].height*i
                my_map_to_draw.append(blocks[7])
            if my_map[i][j] == 8:
                blocks[8].left = blocks[8].width*j
                blocks[8].top = blocks[8].height*i
                my_map_to_draw.append(blocks[8])
            if my_map[i][j] == 9:
                blocks[9].left = blocks[9].width*j
                blocks[9].top = blocks[9].height*i
                my_map_to_draw.append(blocks[9])
            if my_map[i][j] == 10:
                blocks[10].left = blocks[10].width*j
                blocks[10].top = blocks[10].height*i
                my_map_to_draw.append(blocks[10])
            if my_map[i][j] == 11:
                blocks[11].left = blocks[11].width*j
                blocks[11].top = blocks[11].height*i
                my_map_to_draw.append(blocks[11])
            if my_map[i][j] == 12:
                blocks[12].left = blocks[12].width*j
                blocks[12].top = blocks[12].height*i
                my_map_to_draw.append(blocks[12])
            if my_map[i][j] == 13:
                blocks[13].left = blocks[13].width*j
                blocks[13].top = blocks[13].height*i
                my_map_to_draw.append(blocks[13])
            if my_map[i][j] == 14:
                blocks[14].left = blocks[14].width*j
                blocks[14].top = blocks[14].height*i
                my_map_to_draw.append(blocks[14])
            if my_map[i][j] == 15:
                blocks[15].left = blocks[15].width*j
                blocks[15].top = blocks[15].height*i
                my_map_to_draw.append(blocks[15])
map_generator_draw()
def draw():
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player,time_pj
    if time_pj == 0:
        clock.schedule_interval(animation_pj,0.3)
        #clock.schedule_interval(gravity,0.000000001)
        time_pj = 1
    if config == 0:
        screen.surface=pygame.display.set_mode((WIDTH,HEIGHT),pygame.FULLSCREEN)
        config = 1
    if config == 2:
        screen.surface=pygame.display.set_mode((WIDTH,HEIGHT))
        config = 3
    screen.fill("#91ccff")
    bg2.draw()
    bg2x2.draw()
    bg3.draw()
    bg3x2.draw()
    bg4.draw()
    bg4x2.draw()
    if mode != "game":
        floor.draw()
        floorx2.draw()
    if mode == "entry":
        charge_im.draw()
        pointer.draw()
    if mode == "menu":
        if mini_mode == "" or mini_mode == "quit":
            infinite_click.draw()
            play.draw()
            furs.draw()
            missions.draw()
            achievements.draw()
            settings.draw()
            stats.draw()
            cross.draw()
            pointer.draw()
    if mode == "skins":
        if mini_mode != "shop":
            bg_color.draw()
            if skin_page == 1:
                fur1.draw()
                fur2.draw()
                fur3.draw()
                fur4.draw()
                fur5.draw()
                fur6.draw()
                fur7.draw()
                fur8.draw()
                fur9.draw()
                fur10.draw()
                fur11.draw()
                fur12.draw()
                fur13.draw()
                fur14.draw()
                fur15.draw()
                fur16.draw()
                fur17.draw()
                fur18.draw()
                fur19.draw()
                fur2_locked.draw()
                fur3_locked.draw()
                fur4_locked.draw()
                fur5_locked.draw()
                fur6_locked.draw()
                fur7_locked.draw()
                fur8_locked.draw()
                fur9_locked.draw()
                fur10_locked.draw()
                fur11_locked.draw()
                fur12_locked.draw()
                fur13_locked.draw()
                fur14_locked.draw()
                fur15_locked.draw()
                fur16_locked.draw()
                fur17_locked.draw()
                fur18_locked.draw()
                fur19_locked.draw()
                frame_fur.draw()
            if skin_page == 2:
                hair1.draw()
                hair2.draw()
                hair3.draw()
                hair4.draw()
                hair5.draw()
                hair6.draw()
                hair7.draw()
                hair8.draw()
                hair9.draw()
                hair10.draw()
                hair11.draw()
                hair12.draw()
                hair13.draw()
                hair14.draw()
                hair15.draw()
                hair16.draw()
                hair17.draw()
                hair18.draw()
                hair19.draw()
                hair20.draw()
                hair21.draw()
                hair2_locked.draw()
                hair3_locked.draw()
                hair4_locked.draw()
                hair5_locked.draw()
                hair6_locked.draw()
                hair7_locked.draw()
                hair8_locked.draw()
                hair9_locked.draw()
                hair10_locked.draw()
                hair11_locked.draw()
                hair12_locked.draw()
                hair13_locked.draw()
                hair14_locked.draw()
                hair15_locked.draw()
                hair16_locked.draw()
                hair17_locked.draw()
                hair18_locked.draw()
                hair19_locked.draw()
                hair20_locked.draw()
                hair21_locked.draw()
                frame_hair.draw()
            player.draw()
            sweater_player.draw()
            pants_player.draw()
            sneakers_player.draw()
            hair_player.draw()
            fur_select.draw()
            hair_select.draw()
            coin.draw()
            screen.draw.text(str(count),center=(400,920),color="white",fontsize=200,fontname="pusab")
            rope.draw()
            back_button.draw()
        pointer.draw()
    if mode == "game":
        for i in range(len(my_map_to_draw)):
            my_map_to_draw[i].draw()
        pj.draw()
    if mode == "missions":
        bg_shop.draw()
        missions_text.draw()
        coming_soon.draw()
        #bg_missions.draw()
        #select_missions.draw()
        #creen.draw.text("conseguir",center=(960,200),color="white",fontsize=100)
        #screen.draw.text("100 puntos",center=(960,280),color="white",fontsize=100)
        #select_missions2.draw()
        #screen.draw.text("conseguir",center=(960,500),color="white",fontsize=100)
        #screen.draw.text("100 monedas",center=(960,580),color="white",fontsize=100)
        #select_missions3.draw()
        #screen.draw.text("conseguir",center=(960,800),color="white",fontsize=100)
        #screen.draw.text("100 puntos",center=(960,880),color="white",fontsize=100)
        #coin.draw()
        mini_back_button.draw()
        pointer.draw()
    if mode == "":
        bg_black.draw()
    if mini_mode == "quit":
        bg_black.draw()
        screen_quit.draw()
        cancel_exit.draw()
        yes_quit.draw()
        quit_game_text.draw()
        quit_text.draw()
        pointer.draw()
    if mini_mode == "achievements":
        bg_shop.draw()
        achievements_text.draw()
        coming_soon.draw()
        larrow_button.draw()
        rarrow_button.draw()
        mini_back_button.draw()
        pointer.draw()
    if mini_mode == "settings":
        bg_shop.draw()
        locked_secret.draw()
        locked_secret_cyl.draw()
        opcions.draw()
        how_to_play.draw()
        graphics.draw()
        mini_back_button.draw()
        settings_text.draw()
        pointer.draw()
    if mini_mode == "stats":
        bg_shop.draw()
        stats_text.draw()
        coming_soon.draw()
        mini_back_button.draw()
        pointer.draw()
    if mini_mode == "color":
        bg_black.draw()
        screen_color.draw()
        if locked_col == 1:
            mr_riv.draw()
            mr_riv.image = "mr_riv1"
            screen.draw.text("color not available",center=(1075,540),color="white",fontsize=90)
        if locked_col == 2:
            mr_riv.draw()
            mr_riv.image = "mr_riv2"
            screen.draw.text("Not available",center=(1050,540),color="white",fontsize=90)
        if locked_col == 3:
            mr_riv.draw()
            mr_riv.image = "mr_riv3"
            screen.draw.text("WHICH IS NOT",center=(x_number,y_number),color="white",fontsize=90)
            screen.draw.text("AVAILABLE!!!",center=(x_numberx2,y_numberx2),color="white",fontsize=90)
        if locked_col == 4:
            mr_riv.draw()
            mr_riv.image = "mr_riv4"
            screen.draw.text("Well, since you insist so much,",center=(1050,460),color="white",fontsize=70)
            screen.draw.text("then I'll have to give it to you,",center=(1050,540),color="white",fontsize=70)
            screen.draw.text("just don't tell anyone.",center=(1050,620),color="white",fontsize=70)
        if locked_col == 5:
            mr_riv.draw()
            mr_riv.image = "mr_riv2"
            screen.draw.text("OKAY!!",center=(x_numberx3,y_numberx3),color="white",fontsize=90)
        pointer.draw()
    if mini_mode == "color_2":
        bg_black.draw()
        screen_color.draw()
        mr_riv.draw()
        mr_riv.image = "mr_riv1"
    if mode == "shop":
        bg_shop.draw()
        object_shop_1.draw()
        object_shop_2.draw()
        object_shop_3.draw()
        object_shop_4.draw()
        object_shop_5.draw()
        object_shop_6.draw()
        object_shop_7.draw()
        object_shop_8.draw()
        object_shop_9.draw()
        object_shop_10.draw()
        object_shop_11.draw()
        object_shop_12.draw()
        object_shop_13.draw()
        object_shop_14.draw()
        object_shop_15.draw()
        object_shop_16.draw()
        object_shop_17.draw()
        object_shop_11.draw()
        object_shop_12.draw()
        object_shop_13.draw()
        object_shop_14.draw()
        object_shop_15.draw()
        object_shop_16.draw()
        object_shop_17.draw()
        object_shop_18.draw()
        object_shop_19.draw()
        object_shop_20.draw()
        object_shop_21.draw()
        object_shop_22.draw()
        object_shop_23.draw()
        object_shop_24.draw()
        object_shop_25.draw()
        object_shop_26.draw()
        object_shop_27.draw()
        object_shop_28.draw()
        object_shop_29.draw()
        object_shop_30.draw()
        object_shop_31.draw()
        object_shop_32.draw()
        object_shop_33.draw()
        object_shop_34.draw()
        object_shop_35.draw()
        object_shop_36.draw()
        object_shop_37.draw()
        shop_text.draw()
        mini_back_button.draw()
        pointer.draw()
    if mini_mode == "how_to_play":
        bg_shop.draw()
        if how_to_play_page != 1:
            larrow_button.draw()
        if how_to_play_page != 5:
            rarrow_button.draw()
        if how_to_play_page == 1:
            how_to_play_example.draw()
            clock.schedule_interval(for_how_to_play,1)
            screen.draw.text("Tap",center=(940,490),color="green",fontsize=150)
            screen.draw.text("       to player",center=(1179,490),color="white",fontsize=150)
            screen.draw.text("to get a coin",center=(1175,590),color="white",fontsize=150)
        if how_to_play_page >= 2:
            coming_soon.draw()
            #screen.draw.text("Click on the player",center=(1175,490),color="white",fontsize=150)
            #screen.draw.text("to get a coin",center=(1175,590),color="white",fontsize=150)
        how_to_play_text.draw()
        mini_back_button.draw()
        pointer.draw()
    if mini_mode == "graphics":
        bg_shop.draw()
        graphics_text.draw()
        coming_soon.draw()
        #check_screen.draw()
        mini_back_button.draw()
        pointer.draw()
    if mini_mode == "opcions":
        bg_shop.draw()
        opcions_text.draw()
        coming_soon.draw()
        mini_back_button.draw()
        pointer.draw()
    if mini_mode == "don't_have_money":
        bg_black.draw()
        screen_color.draw()
        mr_riv.draw()
        mr_riv.image = "mr_riv1"
        screen.draw.text("You don't have",center=(1075,510),color="white",fontsize=90)
        screen.draw.text("enough coins",center=(1075,570),color="white",fontsize=90)
        pointer.draw()
    if mini_mode == "not_color":
        bg_black.draw()
        screen_color.draw()
        mr_riv.draw()
        mr_riv.image = "mr_riv1"
        screen.draw.text("color not available",center=(1075,540),color="white",fontsize=90)
        pointer.draw()
def on_mouse_down(button,pos):
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player,how_to_play_page,skin
    if button == mouse.LEFT:
        if mode == "skins":
            if rope.collidepoint(pos):
                animate(rope,tween="linear",duration=0.2,y=120)
            if locked_col != 4:
                if mini_mode == "color":
                    mini_mode = ""
                    locked_col += 1
            if locked_col == 4:
                if mini_mode == "color":
                    locked_col += 1
                    fur5_locked.y = 1200
            if mini_mode == "not_color":
                mini_mode = ""
        if mini_mode == "":
            if mode == "menu":
                if cross.collidepoint(pos):
                    cross.image = "cross-"
                if play.collidepoint(pos):
                    play.image = "button_play-"
                if furs.collidepoint(pos):
                    furs.image = "skins_button-"
                if missions.collidepoint(pos):
                    missions.image = "missions_button-"
                if achievements.collidepoint(pos):
                    achievements.image = "achievements_button-"
                if settings.collidepoint(pos):
                    settings.image = "settings_button-"
                if stats.collidepoint(pos):
                    stats.image = "stats_button-"
            if mode == "game":
                if back_button.collidepoint(pos):
                    back_button.image = "back_button-"
                if player.collidepoint(pos):
                    #player.y = 300
                    #hair_player.y = 284
                    #animate(player,tween="bounce_end",duration=0.5,y=600)
                    #animate(hair_player,tween="bounce_end",duration=0.55,y=584)
                    animate(player,tween="linear",duration=0.5,angle=for_player)
                    animate(hair_player,tween="linear",duration=0.5,angle=for_player)
                    for_player += 360
                    count += click
                if bonus_1.collidepoint(pos):
                    bonus_1.image = "bonus_red-"
                if bonus_2.collidepoint(pos):
                    bonus_2.image = "bonus_red-"
                if bonus_3.collidepoint(pos):
                    bonus_3.image = "bonus_blue-"
            if mode == "skins":
                if fur_select.collidepoint(pos):
                    if fur_select.image == "fur_select":
                        fur_select.image = "fur_select-"
                if hair_select.collidepoint(pos):
                    if hair_select.image == "hair_select":
                        hair_select.image = "hair_select-"
                if back_button.collidepoint(pos):
                    back_button.image = "back_button-"
                if skin_page == 1:
                    if fur1.collidepoint(pos):
                        frame_fur.pos = fur1.pos
                        skin = 1
                    if fur2.collidepoint(pos):
                        if fur2_locked.y == 1200:
                            frame_fur.pos = fur2.pos
                            skin = 2
                        else:
                            mini_mode = "not_color"
                    if fur3.collidepoint(pos):
                        if fur3_locked.y == 1200:
                            frame_fur.pos = fur3.pos
                            skin = 3
                        else:
                            mini_mode = "not_color"
                    if fur4.collidepoint(pos):
                        if fur4_locked.y == 1200:
                            frame_fur.pos = fur4.pos
                            skin = 4
                        else:
                            mini_mode = "not_color"
                    if fur5.collidepoint(pos):
                        if fur5_locked.y < 1200:
                            mini_mode = "color"
                        if fur5_locked.y == 1200:
                            frame_fur.pos = fur5.pos
                            skin = 5
                    if fur6.collidepoint(pos):
                        if fur6_locked.y == 1200:
                            frame_fur.pos = fur6.pos
                            skin = 6
                        else:
                            mini_mode = "not_color"
                    if fur7.collidepoint(pos):
                        if fur7_locked.y == 1200:
                            frame_fur.pos = fur7.pos
                            skin = 7
                        else:
                            mini_mode = "not_color"
                    if fur8.collidepoint(pos):
                        if fur8_locked.y == 1200:
                            frame_fur.pos = fur8.pos
                            skin = 8
                        else:
                            mini_mode = "not_color"
                    if fur9.collidepoint(pos):
                        if fur9_locked.y == 1200:
                            frame_fur.pos = fur9.pos
                            skin = 9
                        else:
                            mini_mode = "not_color"
                    if fur10.collidepoint(pos):
                        if fur10_locked.y == 1200:
                            frame_fur.pos = fur10.pos
                            skin = 10
                        else:
                            mini_mode = "not_color"
                    if fur11.collidepoint(pos):
                        if fur11_locked.y == 1200:
                            frame_fur.pos = fur11.pos
                            skin = 11
                        else:
                            mini_mode = "not_color"
                    if fur12.collidepoint(pos):
                        if fur12_locked.y == 1200:
                            frame_fur.pos = fur12.pos
                            skin = 12
                        else:
                            mini_mode = "not_color"
                    if fur13.collidepoint(pos):
                        if fur13_locked.y == 1200:
                            frame_fur.pos = fur13.pos
                            skin = 13
                        else:
                            mini_mode = "not_color"
                    if fur14.collidepoint(pos):
                        if fur14_locked.y == 1200:
                            frame_fur.pos = fur14.pos
                            skin = 14
                        else:
                            mini_mode = "not_color"
                    if fur15.collidepoint(pos):
                        if fur15_locked.y == 1200:
                            frame_fur.pos = fur15.pos
                            skin = 15
                        else:
                            mini_mode = "not_color"
                    if fur16.collidepoint(pos):
                        if fur16_locked.y == 1200:
                            frame_fur.pos = fur16.pos
                            skin = 16
                        else:
                            mini_mode = "not_color"
                    if fur17.collidepoint(pos):
                        if fur17_locked.y == 1200:
                            frame_fur.pos = fur17.pos
                            skin = 17
                        else:
                            mini_mode = "not_color"
                    if fur18.collidepoint(pos):
                        if fur18_locked.y == 1200:
                            frame_fur.pos = fur18.pos
                            skin = 18
                        else:
                            mini_mode = "not_color"
                    if fur19.collidepoint(pos):
                        if fur19_locked.y == 1200:
                            frame_fur.pos = fur19.pos
                            skin = 19
                        else:
                            mini_mode = "not_color"
                if skin_page == 2:
                    if hair1.collidepoint(pos):    
                        frame_hair.pos = hair1.pos
                        hair_player.image = "hair_0"
                    if hair2.collidepoint(pos):
                        if hair2_locked.y == 1200:
                            frame_hair.pos = hair2.pos
                            hair_player.image = "hair_1"
                        else:
                            mini_mode = "not_color"
                    if hair3.collidepoint(pos):
                        if hair3_locked.y == 1200:
                            frame_hair.pos = hair3.pos
                            hair_player.image = "hair_2"
                        else:
                            mini_mode = "not_color"
                    if hair4.collidepoint(pos):
                        if hair4_locked.y == 1200:
                            frame_hair.pos = hair4.pos
                            hair_player.image = "hair_3"
                        else:
                            mini_mode = "not_color"
                    if hair5.collidepoint(pos):
                        if hair5_locked.y == 1200:
                            frame_hair.pos = hair5.pos
                            hair_player.image = "hair_4"
                        else:
                            mini_mode = "not_color"
                    if hair6.collidepoint(pos):
                        if hair6_locked.y == 1200:
                            frame_hair.pos = hair6.pos
                            hair_player.image = "hair_5"
                        else:
                            mini_mode = "not_color"
                    if hair7.collidepoint(pos):
                        if hair7_locked.y == 1200:
                            frame_hair.pos = hair7.pos
                            hair_player.image = "hair_6"
                        else:
                            mini_mode = "not_color"
                    if hair8.collidepoint(pos):
                        if hair8_locked.y == 1200:
                            frame_hair.pos = hair8.pos
                            hair_player.image = "hair_7"
                        else:
                            mini_mode = "not_color"
                    if hair9.collidepoint(pos):
                        if hair9_locked.y == 1200:
                            frame_hair.pos = hair9.pos
                            hair_player.image = "hair_8"
                        else:
                            mini_mode = "not_color"
                    if hair10.collidepoint(pos):
                        if hair10_locked.y == 1200:
                            frame_hair.pos = hair10.pos
                            hair_player.image = "hair_9"
                        else:
                            mini_mode = "not_color"
                    if hair11.collidepoint(pos):
                        if hair11_locked.y == 1200:
                            frame_hair.pos = hair11.pos
                            hair_player.image = "hair_10"
                        else:
                            mini_mode = "not_color"
                    if hair12.collidepoint(pos):
                        if hair12_locked.y == 1200:
                            frame_hair.pos = hair12.pos
                            hair_player.image = "hair_11"
                        else:
                            mini_mode = "not_color"
                    if hair13.collidepoint(pos):
                        if hair13_locked.y == 1200:
                            frame_hair.pos = hair13.pos
                            hair_player.image = "hair_12"
                        else:
                            mini_mode = "not_color"
                    if hair14.collidepoint(pos):
                        if hair14_locked.y == 1200:
                            frame_hair.pos = hair14.pos
                            hair_player.image = "hair_13"
                        else:
                            mini_mode = "not_color"
                    if hair15.collidepoint(pos):
                        if hair15_locked.y == 1200:
                            frame_hair.pos = hair15.pos
                            hair_player.image = "hair_14"
                        else:
                            mini_mode = "not_color"
                    if hair16.collidepoint(pos):
                        if hair16_locked.y == 1200:
                            frame_hair.pos = hair16.pos
                            hair_player.image = "hair_15"
                        else:
                            mini_mode = "not_color"
                    if hair17.collidepoint(pos):
                        if hair17_locked.y == 1200:
                            frame_hair.pos = hair17.pos
                            hair_player.image = "hair_16"
                        else:
                            mini_mode = "not_color"
                    if hair18.collidepoint(pos):
                        if hair18_locked.y == 1200:
                            frame_hair.pos = hair18.pos
                            hair_player.image = "hair_17"
                        else:
                            mini_mode = "not_color"
                    if hair19.collidepoint(pos):
                        if hair19_locked.y == 1200:
                            frame_hair.pos = hair19.pos
                            hair_player.image = "hair_18"
                        else:
                            mini_mode = "not_color"
                    if hair20.collidepoint(pos):
                        if hair20_locked.y == 1200:
                            frame_hair.pos = hair20.pos
                            hair_player.image = "hair_19"
                        else:
                            mini_mode = "not_color"
                    if hair21.collidepoint(pos):
                        if hair21_locked.y == 1200:
                            frame_hair.pos = hair21.pos
                            hair_player.image = "hair_20"
                        else:
                            mini_mode = "not_color"
        if mini_mode == "quit":
            if cancel_exit.collidepoint(pos):
                cancel_exit.image = "button_exit_2-"
            if yes_quit.collidepoint(pos):
                yes_quit.image = "button_exit-"
        if mini_mode == "settings":
            if mini_back_button.collidepoint(pos):
                mini_back_button.image = "back_button-"
            if how_to_play.collidepoint(pos):
                how_to_play.image = "button_settings_how_to_play-"
            if graphics.collidepoint(pos):
                graphics.image = "button_settings_graphics-"
            if opcions.collidepoint(pos):
                opcions.image = "button_settings_opcions-"
        if mini_mode == "how_to_play":
            if mini_back_button.collidepoint(pos):
                mini_back_button.image = "back_button-"
            if rarrow_button.collidepoint(pos):
                rarrow_button.image = "rarrow-"
            if larrow_button.collidepoint(pos):
                larrow_button.image = "larrow-"
        if mini_mode == "graphics":
            if mini_back_button.collidepoint(pos):
                mini_back_button.image = "back_button-"
            if check_screen.collidepoint(pos):
                check_screen.image = "select_button-"
        if mini_mode == "opcions":
            if mini_back_button.collidepoint(pos):
                mini_back_button.image = "back_button-"
            if larrow_button.collidepoint(pos):
                larrow_button.image = "select_button-"
        if mode == "shop":
            if mini_back_button.collidepoint(pos):
                mini_back_button.image = "back_button-"
            if mini_mode == "don't_have_money":
                mini_mode = ""
            elif object_shop_1.collidepoint(pos):
                if count >= 300:
                    object_shop_1.image = "col_unlock"
                    fur2_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_2.collidepoint(pos):
                if count >= 300:
                    object_shop_2.image = "col_unlock"
                    fur3_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_3.collidepoint(pos):
                if count >= 300:
                    object_shop_3.image = "col_unlock"
                    fur4_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_4.collidepoint(pos):
                if count >= 300:
                    object_shop_4.image = "col_unlock"
                    fur6_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_5.collidepoint(pos):
                if count >= 300:
                    object_shop_5.image = "col_unlock"
                    fur7_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_6.collidepoint(pos):
                if count >= 300:
                    object_shop_6.image = "col_unlock"
                    fur8_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_7.collidepoint(pos):
                if count >= 300:
                    object_shop_7.image = "col_unlock"
                    fur9_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_8.collidepoint(pos):
                if count >= 300:
                    object_shop_8.image = "col_unlock"
                    fur10_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_9.collidepoint(pos):
                if count >= 300:
                    object_shop_9.image = "col_unlock"
                    fur11_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_10.collidepoint(pos):
                if count >= 300:
                    object_shop_10.image = "col_unlock"
                    fur12_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_11.collidepoint(pos):
                if count >= 300:
                    object_shop_11.image = "col_unlock"
                    fur13_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_12.collidepoint(pos):
                if count >= 300:
                    object_shop_12.image = "col_unlock"
                    fur14_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_13.collidepoint(pos):
                if count >= 300:
                    object_shop_13.image = "col_unlock"
                    fur15_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_14.collidepoint(pos):
                if count >= 300:
                    object_shop_14.image = "col_unlock"
                    fur16_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_15.collidepoint(pos):
                if count >= 300:
                    object_shop_15.image = "col_unlock"
                    fur17_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_16.collidepoint(pos):
                if count >= 300:
                    object_shop_16.image = "col_unlock"
                    fur18_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_17.collidepoint(pos):
                if count >= 300:
                    object_shop_17.image = "col_unlock"
                    fur19_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_18.collidepoint(pos):
                if count >= 300:
                    object_shop_18.image = "col_unlock"
                    hair2_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_19.collidepoint(pos):
                if count >= 300:
                    object_shop_19.image = "col_unlock"
                    hair3_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_20.collidepoint(pos):
                if count >= 300:
                    object_shop_20.image = "col_unlock"
                    hair4_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_21.collidepoint(pos):
                if count >= 300:
                    object_shop_21.image = "col_unlock"
                    hair5_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_22.collidepoint(pos):
                if count >= 300:
                    object_shop_22.image = "col_unlock"
                    hair6_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_23.collidepoint(pos):
                if count >= 300:
                    object_shop_23.image = "col_unlock"
                    hair7_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_24.collidepoint(pos):
                if count >= 300:
                    object_shop_24.image = "col_unlock"
                    hair8_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_25.collidepoint(pos):
                if count >= 300:
                    object_shop_25.image = "col_unlock"
                    hair9_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_26.collidepoint(pos):
                if count >= 300:
                    object_shop_26.image = "col_unlock"
                    hair10_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_27.collidepoint(pos):
                if count >= 300:
                    object_shop_27.image = "col_unlock"
                    hair11_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_28.collidepoint(pos):
                if count >= 300:
                    object_shop_28.image = "col_unlock"
                    hair12_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_29.collidepoint(pos):
                if count >= 300:
                    object_shop_29.image = "col_unlock"
                    hair13_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_30.collidepoint(pos):
                if count >= 300:
                    object_shop_30.image = "col_unlock"
                    hair14_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_31.collidepoint(pos):
                if count >= 300:
                    object_shop_31.image = "col_unlock"
                    hair15_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_32.collidepoint(pos):
                if count >= 300:
                    object_shop_32.image = "col_unlock"
                    hair16_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_33.collidepoint(pos):
                if count >= 300:
                    object_shop_33.image = "col_unlock"
                    hair17_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_34.collidepoint(pos):
                if count >= 300:
                    object_shop_34.image = "col_unlock"
                    hair18_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_35.collidepoint(pos):
                if count >= 300:
                    object_shop_35.image = "col_unlock"
                    hair19_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_36.collidepoint(pos):
                if count >= 300:
                    object_shop_36.image = "col_unlock"
                    hair20_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
            elif object_shop_37.collidepoint(pos):
                if count >= 300:
                    object_shop_37.image = "col_unlock"
                    hair21_locked.y = 1200
                    count -= 300
                else:
                    mini_mode = "don't_have_money"
def on_mouse_up(button,pos):
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player,how_to_play_page,screen
    if button == mouse.LEFT:
        cross.image = "cross"
        back_button.image = "back_button"
        yes_quit.image = "button_exit"
        cancel_exit.image = "button_exit_2"
        furs.image = "skins_button"
        play.image = "button_play"
        missions.image = "missions_button"
        achievements.image = "achievements_button"
        settings.image = "settings_button"
        stats.image = "stats_button"
        select_missions.image = "bonus_red"
        select_missions2.image = "bonus_red"
        select_missions3.image = "bonus_blue"
        bonus_1.image = "bonus_red"
        bonus_2.image = "bonus_red"
        bonus_3.image = "bonus_blue"
        mini_back_button.image = "back_button"
        how_to_play.image = "button_settings_how_to_play"
        graphics.image = "button_settings_graphics"
        opcions.image = "button_settings_opcions"
        larrow_button.image = "larrow"
        rarrow_button.image = "rarrow"
        animate(rope,tween="linear",duration=0.2,y=115)
        if check_screen.image == "select_button-":
            check_screen.image = "select_button"
        if fur_select.image == "fur_select-":
            fur_select.image = "fur_select"
        if hair_select.image == "hair_select-":
            hair_select.image = "hair_select"
        if mini_mode == "":
            if mode == "entry":
                mode = "menu"
            if mode == "menu":
                if cross.collidepoint(pos):
                    mini_mode = "quit"
                if furs.collidepoint(pos):
                    mode = "skins"
                    if counter == 1:
                        clock.schedule_interval(for_coin,0.2)
                        counter = 2
                if play.collidepoint(pos):
                    mode = "game"
                if missions.collidepoint(pos):
                    mode = "missions"
                    if counter == 1:
                        clock.schedule_interval(for_coin,0.2)
                        counter = 2
                if achievements.collidepoint(pos):
                    mini_mode = "achievements"
                if settings.collidepoint(pos):
                    mini_mode = "settings"
                if stats.collidepoint(pos):
                    mini_mode = "stats"
            if mode == "game":
                if back_button.collidepoint(pos):
                    mode = "menu"
                if bonus_1.collidepoint(pos):
                    if count >= 50:
                        click += 1
                        count -= 50
                        bon_1 += 1
                if bonus_2.collidepoint(pos):
                    if count >= 125:
                        clock.schedule_interval(for_bonus2,1)
                        count -= 125
                        bon_2 += 1
                if bonus_3.collidepoint(pos):
                    if count >= 500:
                        clock.schedule_interval(for_bonus3,1)
                        count -= 500
                        bon_3 += 1
            if mode == "missions":
                if mini_back_button.collidepoint(pos):
                    mode = "menu"
            if mode == "skins":
                if back_button.collidepoint(pos):
                    mode = "menu"
                if fur_select.collidepoint(pos):
                    time.sleep(0.3)
                    skin_page = 1
                    fur_select.image = "fur_select_selected"
                    hair_select.image = "hair_select"
                if hair_select.collidepoint(pos):
                    time.sleep(0.3)
                    skin_page = 2
                    hair_select.image = "hair_select_selected"
                    fur_select.image = "fur_select"
                if rope.collidepoint(pos):
                    mode = "shop"
        if mini_mode == "quit":
            if cancel_exit.collidepoint(pos):
                cancel_exit.image = "button_exit_2"
                mini_mode = ""
            if yes_quit.collidepoint(pos):
                yes_quit.image = "button_exit"
                mini_mode = ""
                mode = ""
                time.sleep(0.5)
                exit()
        if mode == "shop":
            if mini_back_button.collidepoint(pos):
                mode = "skins"
        if mini_mode == "settings":
            if mini_back_button.collidepoint(pos):
                mini_mode = ""
            if how_to_play.collidepoint(pos):
                mini_mode = "how_to_play"
            if graphics.collidepoint(pos):
                mini_mode = "graphics"
            if opcions.collidepoint(pos):
                mini_mode = "opcions"
        if mini_mode == "stats":
            if mini_back_button.collidepoint(pos):
                mini_mode = ""
        if mini_mode == "achievements":
            if mini_back_button.collidepoint(pos):
                mini_mode = ""
        if mini_mode == "how_to_play":
            if mini_back_button.collidepoint(pos):
                mini_mode = "settings"
            if how_to_play_page != 1:
                if larrow_button.collidepoint(pos):
                    how_to_play_page -= 1
            if how_to_play_page != 5:
                if rarrow_button.collidepoint(pos):
                    how_to_play_page += 1
        if mini_mode == "graphics":
            if mini_back_button.collidepoint(pos):
                mini_mode = "settings"
        if mini_mode == "opcions":
            if mini_back_button.collidepoint(pos):
                mini_mode = "settings"
def on_mouse_move(pos):
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player,mode_of_key
    pointer.pos = pos
    if mini_mode == "":
        if furs.collidepoint(pos):
            mode_of_key = 1
        elif play.collidepoint(pos):
            mode_of_key = 2
        elif missions.collidepoint(pos):
            mode_of_key = 3
        else:
            mode_of_key = 0
def on_key_down(key):
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player,player,my_map,block_13,block_14,block_15
    if key == keys.RETURN: #or key == keys.RETURN or key == keys.ESCAPE or key == keys.BACKSPACE
        if mini_mode == "":
            if mode == "menu":
                if mode_of_key == 1:
                    furs.image = "skins_button-"
                if mode_of_key == 2:
                    play.image = "button_play-"
                if mode_of_key == 3:
                    missions.image = "missions_button-"
                if mode_of_key == 4:
                    mode = "menu" 
def on_key_up(key):
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player
    if key == keys.RETURN: #or key == keys.RETURN or key == keys.ESCAPE or key == keys.BACKSPACE
        cross.image = "cross"
        back_button.image = "back_button"
        yes_quit.image = "button_exit"
        cancel_exit.image = "button_exit_2"
        furs.image = "skins_button"
        play.image = "button_play"
        missions.image = "missions_button"
        achievements.image = "achievements_button"
        settings.image = "settings_button"
        stats.image = "stats_button"
        select_missions.image = "bonus_red"
        select_missions2.image = "bonus_red"
        select_missions3.image = "bonus_blue"
        bonus_1.image = "bonus_red"
        bonus_2.image = "bonus_red"
        bonus_3.image = "bonus_blue"
        mini_back_button.image = "back_button"
        animate(rope,tween="linear",duration=0.2,y=115)
        if mode == "menu":
            if mode_of_key == 1:
                mode = "skins"
            if mode_of_key == 2:
                mode = "game"
            if mode_of_key == 3:
                mode = "missions"
            if mode_of_key == 4:
                mode = "menu"
    if key == keys.ESCAPE:
        if mode != "menu":
            if mini_mode == "":
                mode = "menu"
        if mini_mode != "":
            mini_mode = ""
def update(dt):
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player
    if mode != "entry":
        bg2.x += 1
        bg3.x += 2
        bg4.x += 3
        bg2x2.x += 1
        bg3x2.x += 2
        bg4x2.x += 3
        floor.x += 10
        floorx2.x += 10
    if bg2.x >= 2880:
        bg2.x = -960
    if bg2x2.x >= 2880:
        bg2x2.x = -960
    if bg3.x >= 2880:
        bg3.x = -960
    if bg3x2.x >= 2880:
        bg3x2.x = -960
    if bg4.x >= 2880:
        bg4.x = -960
    if bg4x2.x >= 2880:
        bg4x2.x = -960
    if floor.x >= 2880:
        floor.x = -960
    if floorx2.x >= 2880:
        floorx2.x = -960
    if count < 50:
        bonus_1.image = "bonus_red_locked"
    if count < 125:
        bonus_2.image = "bonus_red_locked"
    if count < 500:
        bonus_3.image = "bonus_blue_locked"
    if coins_image == 0:
        coin.image = "coin1"
    if coins_image == 1:
        coin.image = "coin2"
    if coins_image == 2:
        coin.image = "coin3"
    if coins_image == 3:
        coin.image = "coin4"
    if coins_image == 4:
        coin.image = "coin5"
    if coins_image == 5:
        coin.image = "coin6"
    if coins_image == 6:
        coin.image = "coin1"
    if mode == "entry":
        floor.y = 650
        floorx2.y = 650
    if mode == "menu":
        floor.y = 540
        floorx2.y = 540
    if mode == "missions":
        coin.x = 1500
        coin.y = 240
    if mode == "skins":
        coin.x = 150
        coin.y = 920
    if player.y == 100:
        animate(player,tween="linear",duration=0.5,y=540)
        animate(hair_player,tween="linear",duration=0.5,y=412)
def for_bonus2():
    global count
    count += 1
def for_bonus3():
    global count
    count += 5
def for_time():
    global game_time
    game_time += 1
def for_text():
    global y_number,x_number,y_numberx2,x_numberx2,x_numberx3,y_numberx3
    x_number = random.randint(1050,1060)
    y_number = random.randint(510,520)
    x_numberx2 = random.randint(1050,1060)
    y_numberx2 = random.randint(570,580)
    x_numberx3 = random.randint(1050,1060)
    y_numberx3 = random.randint(540,550)
def for_coin():
    global coins_image
    coins_image += 1
    if coins_image >= 6:
        coins_image = 0
def for_charge():
    global charge,mode
    if charge == 0:
        charge_im.image = "charge_bar_0"
        charge += 1
    if charge == 1:
        charge_im.image = "charge_bar_1"
        charge += 1
    if charge == 2:
        charge_im.image = "charge_bar_2"
        charge += 1
    if charge == 3:
        charge_im.image = "charge_bar_3"
        charge += 1
    if charge == 4:
        charge_im.image = "charge_bar_4"
        charge += 1
def for_how_to_play():
    global how,game
    if mini_mode == "how_to_play":
        if game == 1:
            animate(how_to_play_example,tween="linear",duration=0.5,angle=how)
            how += 0
            game += 1
        if game == 2:
            clock.schedule_interval(for_how,1)
def for_how():
    global how,game
    if mini_mode == "how_to_play":
        if game == 2:
            game -= 1
            how = 360
def sweater_pj():
    global pj,mode,mini_mode,time_pj,direction_pj,move_pj,speed_pj
    if pj_sweater == 1:
        if direction_pj == 1:
            if time_pj == 1:
                sweater_player.image = "sweater_0_1"
            elif time_pj == 2:
                sweater_player.image = "sweater_0_2"
            elif time_pj == 3:
                sweater_player.image = "sweater_0_3"
            elif time_pj == 4:
                sweater_player.image = "sweater_0_4"
            elif time_pj >= 5:
                sweater_player.image = "sweater_0_1"
                time_pj = 1
def animation_pj():
    global skin,mode,mini_mode,time_pj,direction_pj,move_pj,speed_pj
    time_pj += 1
    if skin == 1:
        if (direction_pj == 1 and move_pj == 0):
            if time_pj == 1:
                player.image = "fur_skin_0_sprite_1"
                pj.image = "fur_play_0_1"
            elif time_pj == 2:
                player.image = "fur_skin_0_sprite_2"
                pj.image = "fur_play_0_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_0_sprite_3"
                pj.image = "fur_play_0_3"
            elif time_pj == 4:
                player.image = "fur_skin_0_sprite_4"
                pj.image = "fur_play_0_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_0_sprite_1"
                pj.image = "fur_play_0_1"
                time_pj = 1
    if skin == 2:
        if (direction_pj == 1 and move_pj == 0):
            if time_pj == 1:
                player.image = "fur_skin_1_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_1_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_1_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_1_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_1_sprite_1"
                time_pj = 1
    if skin == 3:
        if (direction_pj == 1 and move_pj == 0):
            if time_pj == 1:
                player.image = "fur_skin_2_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_2_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_2_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_2_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_2_sprite_1"
                time_pj = 1
    if skin == 4:
        if (direction_pj == 1 and move_pj == 0):
            if time_pj == 1:
                player.image = "fur_skin_3_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_3_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_3_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_3_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_3_sprite_1"
                time_pj = 1
    if skin == 5:
        if (direction_pj == 1 and move_pj == 0):
            if time_pj == 1:
                player.image = "fur_skin_4_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_4_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_4_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_4_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_4_sprite_1"
                time_pj = 1
def gravity():
    pj.y += 8
pgzrun.go()