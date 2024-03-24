import pygame
import pgzrun
import random
import time
WIDTH = 1920
HEIGHT = 1080
TITLE = "Run_Gun"
FPS = 60
blocks=[]
timer_y = 925
timer_x = 450
for i in range(30):
    block = "block_"+str(i+1)
    blocks.append(block)
screen_mode = Actor("animation_mode_screen",(960,-2994))
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
level_1 = Actor("level_button_1",(605,185))
level_2 = Actor("level_button_2",(805,185))
level_3 = Actor("level_button_2",(1005,185))
level_4 = Actor("level_button_2",(1205,185))
level_5 = Actor("level_button_2",(605,385))
level_6 = Actor("level_button_2",(805,385))
level_7 = Actor("level_button_2",(1005,385))
level_8 = Actor("level_button_2",(1205,385))
level_9 = Actor("level_button_2",(605,585))
level_10 = Actor("level_button_2",(805,585))
level_11 = Actor("level_button_2",(1005,585))
level_12 = Actor("level_button_2",(1205,585))
level_13 = Actor("level_button_2",(605,785))
level_14 = Actor("level_button_2",(805,785))
level_15 = Actor("level_button_2",(1005,785))
level_16 = Actor("level_button_2",(1205,785))
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
player = Actor("fur_skin_0_sprite_1",(480,540))
shirt_player = Actor("shirt_0",(480,540))
hair_player = Actor("hair_0",(480,412))
pj = Actor("fur_play_0_1_pos_1",(300,540))
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
bg_level = Actor("bg_level",(960,540))
pj_menu = Actor("player_menu_1",(15,596))
tree = Actor("tree_2",(15,596))
heart_1 = Actor("heart",(960,140))
heart_2 = Actor("heart-",(960,240))
heart_3 = Actor("heart--",(960,340))
energy_1 = Actor("energy",(960,440))
energy_2 = Actor("energy-",(960,540))
energy_3 = Actor("energy--",(960,640))
timer = Actor("timer",(timer_x,timer_y))
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
direction_pj = True
move_pj = False
speed_pj = 1
animation_mode = 0
gravity = True
oh = pj.y
uh = 100
bush = 1
grove = 2
enemies = []
my_map = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1, 1, 3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [ 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3,-1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,17, 2, 2,18,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
          [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]]
my_map_noclip = [[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1, 5, 7,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [-1,-1,-1,-1,-1,-1,-1, 5, 7,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [ 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1, 1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                 [ 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7,-1, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
                 [ 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6,20, 6, 6,21, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6],
                 [ 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 7,-1, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]]
my_map_to_draw = []
def map_generator_draw_noclip():
    for i in range(len(my_map_noclip)):
        for j in range(len(my_map_noclip[0])):
            if my_map_noclip[i][j] == 1:
                new_block = Actor(blocks[0])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 2:
                new_block = Actor(blocks[1])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 3:
                new_block = Actor(blocks[2])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 4:
                new_block = Actor(blocks[3])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 5:
                new_block = Actor(blocks[4])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 6:
                new_block = Actor(blocks[5])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 7:
                new_block = Actor(blocks[6])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 8:
                new_block = Actor(blocks[7])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 9:
                new_block = Actor(blocks[8])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 10:
                new_block = Actor(blocks[9])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 11:
                new_block = Actor(blocks[10])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 12:
                new_block = Actor(blocks[11])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 13:
                new_block = Actor(blocks[12])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 14:
                new_block = Actor(blocks[13])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 15:
                new_block = Actor(blocks[14])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 16:
                new_block = Actor(blocks[15])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 17:
                new_block = Actor(blocks[16])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 18:
                new_block = Actor(blocks[17])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 19:
                new_block = Actor(blocks[18])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 20:
                new_block = Actor(blocks[19])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 21:
                new_block = Actor(blocks[20])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 22:
                new_block = Actor(blocks[21])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 23:
                new_block = Actor(blocks[22])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 24:
                new_block = Actor(blocks[23])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 25:
                new_block = Actor(blocks[24])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 26:
                new_block = Actor(blocks[25])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 27:
                new_block = Actor(blocks[26])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 28:
                new_block = Actor(blocks[27])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 29:
                new_block = Actor(blocks[28])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
            elif my_map_noclip[i][j] == 30:
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_block.draw()
def map_generator_draw():
    for i in range(len(my_map)):
        new_row=[]
        for j in range(len(my_map[0])):
            if my_map[i][j] == 1:
                new_block = Actor(blocks[0])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 2:
                new_block = Actor(blocks[1])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 3:
                new_block = Actor(blocks[2])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 4:
                new_block = Actor(blocks[3])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 5:
                new_block = Actor(blocks[4])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 6:
                new_block = Actor(blocks[5])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 7:
                new_block = Actor(blocks[6])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 8:
                new_block = Actor(blocks[7])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 9:
                new_block = Actor(blocks[8])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 10:
                new_block = Actor(blocks[9])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 11:
                new_block = Actor(blocks[10])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 12:
                new_block = Actor(blocks[11])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 13:
                new_block = Actor(blocks[12])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 14:
                new_block = Actor(blocks[13])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 15:
                new_block = Actor(blocks[14])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 16:
                new_block = Actor(blocks[15])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 17:
                new_block = Actor(blocks[16])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 18:
                new_block = Actor(blocks[17])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 19:
                new_block = Actor(blocks[18])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 20:
                new_block = Actor(blocks[19])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 21:
                new_block = Actor(blocks[20])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 22:
                new_block = Actor(blocks[21])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 23:
                new_block = Actor(blocks[22])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 24:
                new_block = Actor(blocks[23])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 25:
                new_block = Actor(blocks[24])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 26:
                new_block = Actor(blocks[25])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 27:
                new_block = Actor(blocks[26])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 28:
                new_block = Actor(blocks[27])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 29:
                new_block = Actor(blocks[28])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
            elif my_map[i][j] == 30:
                new_block = Actor(blocks[29])
                new_block.left = new_block.width*j
                new_block.top = new_block.height*i
                new_row.append(new_block)
        my_map_to_draw.append(new_row)
map_generator_draw()
def draw():
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player,time_pj
    if time_pj == 0:
        clock.schedule_interval(animation_pj,0.3)
        clock.schedule_interval(for_charge,0.5)
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
    screen_mode.draw()
    if mode == "entry":
        charge_im.draw()
        pointer.draw()
    if mode == "menu":
        if mini_mode == "" or mini_mode == "quit":
            screen_mode.draw()
            infinite_click.draw()
            tree.draw()
            play.draw()
            furs.draw()
            missions.draw()
            achievements.draw()
            settings.draw()
            stats.draw()
            cross.draw()
            pointer.draw()
            screen_mode.draw()
            pj_menu.draw()
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
                player.draw()
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
                hair_player.draw()
            fur_select.draw()
            hair_select.draw()
            coin.draw()
            screen.draw.text(str(count),center=(400,920),color="white",fontsize=200)
            rope.draw()
            back_button.draw()
        pointer.draw()
        screen_mode.draw()
    if mode == "game":
        map_generator_draw_noclip()
        for i in range(len(my_map_to_draw)):
            for j in range(len(my_map_to_draw[i])):
                my_map_to_draw[i][j].draw()
        pj.draw()
        heart_1.draw()
        heart_2.draw()
        heart_3.draw()
        energy_1.draw()
        energy_2.draw()
        energy_3.draw()
        timer.draw()
    if mode == "pos_game":
        bg_level.draw()
        level_1.draw()
        level_2.draw()
        level_3.draw()
        level_4.draw()
        level_5.draw()
        level_6.draw()
        level_7.draw()
        level_8.draw()
        level_9.draw()
        level_10.draw()
        level_11.draw()
        level_12.draw()
        level_13.draw()
        level_14.draw()
        level_15.draw()
        level_16.draw()
        back_button.draw()
        pointer.draw()
        screen_mode.draw()
    if mode == "missions":
        bg_shop.draw()
        missions_text.draw()
        coming_soon.draw()
        mini_back_button.draw()
        pointer.draw()
        screen_mode.draw()
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
        screen_mode.draw()
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
        screen_mode.draw()
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
        screen_mode.draw()
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
        how_to_play_text.draw()
        mini_back_button.draw()
        pointer.draw()
    if mini_mode == "graphics":
        bg_shop.draw()
        graphics_text.draw()
        coming_soon.draw()
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
    if screen_mode.y == -2994:
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
                if mode == "pos_game":
                    if back_button.collidepoint(pos):
                        back_button.image = "back_button-"
                    if level_1.collidepoint(pos):
                        level_1.image = "level_button_1-"
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
            if mode == "missions":
                if mini_back_button.collidepoint(pos):
                    mini_back_button.image = "back_button-"
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
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player,how_to_play_page,animation_mode
    if screen_mode.y == -2994:
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
            level_1.image = "level_button_1"
            level_2.image = "level_button_2"
            animate(rope,tween="linear",duration=0.2,y=115)
            if check_screen.image == "select_button-":
                check_screen.image = "select_button"
            if fur_select.image == "fur_select-":
                fur_select.image = "fur_select"
            if hair_select.image == "hair_select-":
                hair_select.image = "hair_select"
            if mini_mode == "":
                if mode == "menu":
                    if cross.collidepoint(pos):
                        mini_mode = "quit"
                    if furs.collidepoint(pos):
                        animation_mode = 1
                        animate(screen_mode,tween="linear",duration=2,y=4074)
                        if counter == 1:
                            clock.schedule_interval(for_coin,0.2)
                            counter = 2
                    if play.collidepoint(pos):
                        animation_mode = 2
                        animate(screen_mode,tween="linear",duration=2,y=4074)
                    if missions.collidepoint(pos):
                        animation_mode = 3
                        animate(screen_mode,tween="linear",duration=2,y=4074)
                        if counter == 1:
                            clock.schedule_interval(for_coin,0.2)
                            counter = 2
                    if achievements.collidepoint(pos):
                        mini_mode = "achievements"
                    if settings.collidepoint(pos):
                        mini_mode = "settings"
                    if stats.collidepoint(pos):
                        mini_mode = "stats"
                if mode == "pos_game":
                    if back_button.collidepoint(pos):
                        animation_mode = 0
                        animate(screen_mode,tween="linear",duration=2,y=4074)
                    if level_1.collidepoint(pos):
                        mode = "game"
                if mode == "missions":
                    if mini_back_button.collidepoint(pos):
                        animation_mode = 0
                        animate(screen_mode,tween="linear",duration=2,y=4074)
                if mode == "skins":
                    if back_button.collidepoint(pos):
                        animation_mode = 0
                        animate(screen_mode,tween="linear",duration=2,y=4074)
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
                    mode = "shop"
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
    if mode == "pos_game":
        if button == mouse.MIDDLE:
            bit_map.y += 5
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
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player,player,my_map
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
    if key == keys.W:
        for i in range(len(my_map_to_draw)):
            for j in range(len(my_map_to_draw[i])):
                if not (my_map_to_draw[i][j].colliderect(pj) or (my_map_to_draw[i][j].image == "block1" or  my_map_to_draw[i][j].image == "block2" or  my_map_to_draw[i][j].image == "block3" or my_map_to_draw[i][j].image == "block4")):
                    animate(pj,tween="decelerate",duration=0.2,y=jump)
def on_key_up(key):
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player
    if key == keys.RETURN:
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
    global mode,mini_mode,state_click,count,click,skin_page,lang,point_s,point_c,number_1,number_2,y_number,x_number,config,counter,charge,locked_col,bon_1,bon_2,bon_3,for_player,old_x,old_y,gravity,jump,direction_pj,move_pj,bush,grove,orchad
    old_x = pj.x
    old_y = pj.y
    if mode == "game":
        pj.x = old_x
        pj.y = old_y
        jump = oh - uh
        if gravity:
            pj.y += 10
        for i in range(len(my_map_to_draw)):
            for j in range(len(my_map_to_draw[i])):
                if not (my_map_to_draw[i][j].colliderect(pj) or (my_map_to_draw[i][j].image == "block1" or  my_map_to_draw[i][j].image == "block2" or  my_map_to_draw[i][j].image == "block3" or my_map_to_draw[i][j].image == "block4")):
                    gravity = True
                else:
                    pj.x = old_x
                    pj.y = old_y
                    gravity = False
    if keyboard.D:
        if mode == "game":
            for i in range(len(my_map_to_draw)):
                for j in range(len(my_map_to_draw[i])):
                    if not (my_map_to_draw[i][j].colliderect(pj) or (my_map_to_draw[i][j].image == "block1" or  my_map_to_draw[i][j].image == "block2" or  my_map_to_draw[i][j].image == "block3" or my_map_to_draw[i][j].image == "block4")):
                        pj.x += 5
                        direction_pj = True
                        move_pj = True
    if keyboard.A:
        if mode == "game":
            if pj.x >= 10:
                pj.x -= 5
                direction_pj = False
                move_pj = True
    if screen_mode.y >= 4074:
        screen_mode. y = -2994
    if animation_mode == 0:
        if screen_mode.y >= 1080:
            mode = "menu"
    if animation_mode == 1:
        if screen_mode.y >= 1080:
            mode = "skins"
    if animation_mode == 2:
        if screen_mode.y >= 1080:
            mode = "pos_game"
    if animation_mode == 3:
        if screen_mode.y >= 1080:
            mode = "missions"
    if mode != "entry":
        bg2.x += 1
        bg3.x += 2
        bg4.x += 3
        bg2x2.x += 1
        bg3x2.x += 2
        bg4x2.x += 3
        floor.x += 10
        floorx2.x += 10
        tree.x += grove
    if grove == 0:
        orchad = 5
    if grove == 1:
        orchad = 10
    if grove == 2:
        orchad = 20
    if grove == 3:
        orchad = 30
    if grove == 4:
        orchad = 40
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
    if tree.x >= 2100:
        bush = random.randint(1,4)
        tree.x = -100
        if mode == "menu":
            grove = random.randint(0,4)
        else:
            grove = 1
    if bush == 1:
        tree.image = "tree_1"
        tree.y = 596
    if bush == 2:
        tree.image = "tree_2"
        tree.y = 636
    if bush == 3:
        tree.image = "tree_3"
        tree.y = 616
    if bush == 4:
        tree.image = "tree_4"
        tree.y = 644
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
    global charge,mode,bush
    charge += 1
    if charge == 0:
        charge_im.image = "charge_bar_0"
    if charge == 1:
        charge_im.image = "charge_bar_1"
    if charge == 2:
        charge_im.image = "charge_bar_2"
    if charge == 3:
        charge_im.image = "charge_bar_3"
    if charge == 4:
        charge_im.image = "charge_bar_4"
    if charge == 5:
        mode = "menu"
        tree.x = random.randint(-100,2000)
        bush = random.randint(1,4)
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
def pj_random():
    global skin,mode,mini_mode,time_pj,direction_pj,move_pj,speed_pj
    
def animation_pj():
    global skin,mode,mini_mode,time_pj,direction_pj,move_pj,speed_pj
    time_pj += 1
    if skin == 1:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_0_sprite_1"
                pj.image = "fur_play_0_1_pos_1"
            elif time_pj == 2:
                player.image = "fur_skin_0_sprite_2"
                pj.image = "fur_play_0_2_pos_1"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_0_sprite_3"
                pj.image = "fur_play_0_3_pos_1"
            elif time_pj == 4:
                player.image = "fur_skin_0_sprite_4"
                pj.image = "fur_play_0_4_pos_1"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_0_sprite_1"
                pj.image = "fur_play_0_1_pos_1"
                time_pj = 1
        if not direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_0_sprite_1"
                pj.image = "fur_play_0_1_pos_2"
            elif time_pj == 2:
                player.image = "fur_skin_0_sprite_2"
                pj.image = "fur_play_0_2_pos_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_0_sprite_3"
                pj.image = "fur_play_0_3_pos_2"
            elif time_pj == 4:
                player.image = "fur_skin_0_sprite_4"
                pj.image = "fur_play_0_4_pos_2"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_0_sprite_1"
                pj.image = "fur_play_0_1_pos_2"
                time_pj = 1
    if skin == 2:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_1_sprite_1"
                pj.image = "fur_play_1_1_pos_1"
            elif time_pj == 2:
                player.image = "fur_skin_1_sprite_2"
                pj.image = "fur_play_1_2_pos_1"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_1_sprite_3"
                pj.image = "fur_play_1_3_pos_1"
            elif time_pj == 4:
                player.image = "fur_skin_1_sprite_4"
                pj.image = "fur_play_1_4_pos_1"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_1_sprite_1"
                pj.image = "fur_play_1_1_pos_1"
                time_pj = 1
    if skin == 3:
        if direction_pj and move_pj:
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
        if direction_pj and move_pj:
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
        if direction_pj and move_pj:
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
    if skin == 6:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_5_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_5_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_5_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_5_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_5_sprite_1"
                time_pj = 1
    if skin == 7:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_6_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_6_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_6_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_6_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_6_sprite_1"
                time_pj = 1
    if skin == 8:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_7_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_7_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_7_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_7_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_7_sprite_1"
                time_pj = 1
    if skin == 9:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_8_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_8_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_8_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_8_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_8_sprite_1"
                time_pj = 1
    if skin == 10:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_9_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_9_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_9_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_9_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_9_sprite_1"
                time_pj = 1
    if skin == 11:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_10_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_10_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_10_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_10_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_10_sprite_1"
                time_pj = 1
    if skin == 12:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_11_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_11_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_11_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_11_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_11_sprite_1"
                time_pj = 1
    if skin == 13:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_12_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_12_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_12_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_12_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_12_sprite_1"
                time_pj = 1
    if skin == 14:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_13_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_13_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_13_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_13_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_13_sprite_1"
                time_pj = 1
    if skin == 15:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_14_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_14_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_14_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_14_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_14_sprite_1"
                time_pj = 1
    if skin == 16:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_15_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_15_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_15_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_15_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_15_sprite_1"
                time_pj = 1
    if skin == 17:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_16_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_16_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_16_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_16_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_16_sprite_1"
                time_pj = 1
    if skin == 18:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_17_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_17_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_17_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_17_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_17_sprite_1"
                time_pj = 1
    if skin == 19:
        if direction_pj and move_pj:
            if time_pj == 1:
                player.image = "fur_skin_18_sprite_1"
            elif time_pj == 2:
                player.image = "fur_skin_18_sprite_2"
                hair_player.y += 32
            elif time_pj == 3:
                player.image = "fur_skin_18_sprite_3"
            elif time_pj == 4:
                player.image = "fur_skin_18_sprite_4"
                hair_player.y -= 32
            elif time_pj >= 5:
                player.image = "fur_skin_18_sprite_1"
                time_pj = 1
#    (\_/)    te extrañámos acá :'(
#    (o,<)    <3 te amamos :'(
#   (")_(")   Fran forever
pgzrun.go()