import math
import random



Running_flag = True

FPS=60
Screen_height = 1366
Screen_widht = 768


#player position

player_x =  700
player_y =  700
player_speed = 4
player_angle = 0
height = 30

# bullet
bullet_speed = 10
scatter = random.random()*(0.1745329252+0.1745329252)-0.1745329252

#soldier
sol_angle = 0
soldier_hp=100
zombie_aim=0.03
player_delay=6

#ZOMBIE
zombie_start_pos= (400, 400)
b_damage=50
zombie_angle=0
zombie_health=100
killed_zombies=0
zombie_speed=2
zombie_count=10


