
#pygame.mouse.get_rel() смещение курсора относительно прел. позиции
#pygame.mouse.get_pos() позиция курсора в пространстве поля игры
import pygame
import math
from settings import *
from classes import Player
from classes import Zombie


def signum(x):
    return 1 if (x > 0) else -1 if (x < 0) else 0

pygame.init()
sc = pygame.display.set_mode((Screen_height, Screen_widht), pygame.DOUBLEBUF | pygame.HWSURFACE)
pygame.display.set_caption(" Shooter ")

pygame.mixer.music.load("Hell on Earth.mp3")
pygame.mixer.music.play(-1)

clock = pygame.time.Clock()

player = Player()

wall_1 = pygame.image.load("block.jpg")
wall_1_rect = wall_1.get_rect(center = (200, 200))
    
wall_2 = pygame.image.load("block.jpg")
wall_2_rect = wall_2.get_rect(center = (1000, 200))

wall_3 = pygame.image.load("block.jpg")
wall_3_rect = wall_3.get_rect(center = (200, 600))

wall_4 = pygame.image.load("block.jpg")
wall_4_rect = wall_3.get_rect(center = (1000, 600))

wall_5 = pygame.image.load("block.jpg")
wall_5_rect = wall_3.get_rect(center = (600, 400))

bullets = []

zomb_spawn = (((0,1366), (-800,-400)),
              ((0,1366), (1200,1600)),
              ((-800,-400), (0,800)),
              ((1766,2166), (0,800)))
zomb_spawn_sec = random.randint(0, 3)
zombies = [Zombie(random.randint(zomb_spawn[zomb_spawn_sec][0][0], zomb_spawn[zomb_spawn_sec][0][1]),
                  random.randint(zomb_spawn[zomb_spawn_sec][1][0], zomb_spawn[zomb_spawn_sec][1][1]),
                  zombie_speed) for i in range(zombie_count)]


while Running_flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Running_flag = False

    sc.fill("darkgrey")
    
    sold_surf = pygame.image.load("soldier.png")
    sold_rect = sold_surf.get_rect(center=player.pos)
    sold_surf = pygame.transform.rotate(sold_surf, player.sold_angle)

    sc.blit(wall_1, wall_1_rect)
    sc.blit(wall_2, wall_2_rect)
    sc.blit(wall_3, wall_3_rect)
    sc.blit(wall_4, wall_4_rect)
    sc.blit(wall_5, wall_5_rect)
    sc.blit(sold_surf, sold_rect)
    # sc.blit(zomb_surf, zomb_rect)
    for zomb in zombies:
        rot = pygame.transform.rotate(zomb.zomb_surf, math.degrees(zomb.angle))
        sc.blit(rot, zomb.zomb_rect)
    #pygame.draw.circle(sc, "green" ,player.pos, 16)
    #pygame.draw.line(sc, "green", player.pos, (player.x + height * math.cos(player.angle),
                                                                           # player.y + height* math.sin(player.angle)))

    for bullet in bullets:
        bullet.update()
    for bullet in bullets:
        bullet.draw(sc)
    for bullet in bullets:
        if bullet.rect.centerx < 0 or bullet.rect.centerx > 1366 or \
                bullet.rect.centery < 0 or bullet.rect.centery > 768:
            bullets.remove(bullet)
        if wall_1_rect.colliderect(bullet.rect):
            bullets.remove(bullet)
        if wall_2_rect.colliderect(bullet.rect):
            bullets.remove(bullet)
        if wall_3_rect.colliderect(bullet.rect):
            bullets.remove(bullet)
        if wall_4_rect.colliderect(bullet.rect):
            bullets.remove(bullet)
        if wall_5_rect.colliderect(bullet.rect):
            bullets.remove(bullet)
            

    for zomb in zombies:
        for bullet in bullets:
            if zomb.zomb_rect.colliderect(bullet.rect):
                bullets.remove(bullet)

                zomb.health = zomb.health - b_damage
                print(zomb.health)
                if zomb.health <= 0:
                    print("zombie killed")
                    killed_zombies+=1
                    zombies.remove(zomb)
                    break
    
    for zomb in zombies:
        if zomb.zomb_rect.colliderect(sold_rect):
            soldier_hp= soldier_hp-zombie_aim
            print (soldier_hp)
            if soldier_hp <=0 :
                print("YOU WAS KILLED, TRY AGAIN")
                Running_flag = False
                break
    
    for zomb in zombies :
        zomb.zomb_update(player.pos)
        print(zomb.angle, math.degrees(zomb.angle))

    f = pygame.font.SysFont(None, 24)
    sc_text= f.render("HP: ", 1, "red")
    sc_text_rect= sc_text.get_rect(center=(Screen_height//2, 10))
    sc.blit(sc_text, sc_text_rect)
    
    
    f1 = pygame.font.SysFont(None, 24)
    sc_text1= f1.render(str(int(soldier_hp)), 1, "red")
    sc_text_rect1= sc_text1.get_rect(center=(Screen_height//2+27, 10))
    sc.blit(sc_text1, sc_text_rect1)


    f2 = pygame.font.SysFont(None, 24)
    sc_text2= f2.render("Killled zombies:", 1, "blue")
    sc_text_rect2= sc_text2.get_rect(center=(Screen_height//2, 760))
    sc.blit(sc_text2, sc_text_rect2)
    
    f3 = pygame.font.SysFont(None, 24)
    sc_text3= f3.render(str(killed_zombies), 1, "blue")
    sc_text_rect3= sc_text3.get_rect(center=(Screen_height//2+78, 760))
    sc.blit(sc_text3, sc_text_rect3)
    # debug
    #pygame.draw.circle(sc, (0, 255, 0), (sold_rect.centerx, sold_rect.centery), 1)
    #pygame.draw.circle(sc, (0, 255, 0), (wall_1_rect.centerx, wall_1_rect.centery), 1)
    #pygame.draw.line(sc, (0, 255, 0),
    #                 (sold_rect.centerx, sold_rect.centery),
    #                 (wall_1_rect.centerx, wall_1_rect.centery), 2)
    #pygame.draw.line(sc, (0, 0, 255),
    #                 (sold_rect.centerx, sold_rect.centery - signum(sold_rect.centery - wall_1_rect.centery) * sold_rect.height / 2),
    #                 (wall_1_rect.centerx, wall_1_rect.centery), 2)
    #pygame.draw.line(sc, (0, 0, 255),
    #                 (sold_rect.centerx - signum(sold_rect.centerx - wall_1_rect.centerx) * sold_rect.width / 2, sold_rect.centery),
    #                 (wall_1_rect.centerx, wall_1_rect.centery), 2)
    ##

    if len(zombies) == 0:
        if player.delay > 3:
            player.delay -= 1
        if zombie_speed <= 4:
            zombie_speed += 1
        if zombie_count <= 50:
            zombie_count += 4
        zomb_spawn_sec = random.randint(0, 3)
        zombies = [Zombie(random.randint(zomb_spawn[zomb_spawn_sec][0][0], zomb_spawn[zomb_spawn_sec][0][1]),
                          random.randint(zomb_spawn[zomb_spawn_sec][1][0], zomb_spawn[zomb_spawn_sec][1][1]),
                          zombie_speed) for i in range(zombie_count)]


    for zomb in zombies:
        if wall_1_rect.colliderect(zomb.zomb_rect):
            pos = [zomb.zomb_rect.centerx - wall_1_rect.centerx, zomb.zomb_rect.centery - wall_1_rect.centery]

            if (abs(pos[0]) / (wall_1_rect.width / 2)) > (abs(pos[1]) / (wall_1_rect.height / 2)):
                pos[0] = signum(pos[0])
                pos[1] = 0
                zomb.pos[0] += zombie_speed * pos[0]

            if (abs(pos[0]) / (wall_1_rect.width / 2)) < (abs(pos[1]) / (wall_1_rect.height / 2)):
                pos[1] = signum(pos[1])
                pos[0] = 0
                zomb.pos[1] += zombie_speed * pos[1]

        if wall_2_rect.colliderect(zomb.zomb_rect):
            pos = [zomb.zomb_rect.centerx - wall_2_rect.centerx, zomb.zomb_rect.centery - wall_2_rect.centery]

            if (abs(pos[0]) / (wall_2_rect.width / 2)) > (abs(pos[1]) / (wall_2_rect.height / 2)):
                pos[0] = signum(pos[0])
                pos[1] = 0
                zomb.pos[0] += zombie_speed * pos[0]

            if (abs(pos[0]) / (wall_2_rect.width / 2)) < (abs(pos[1]) / (wall_2_rect.height / 2)):
                pos[1] = signum(pos[1])
                pos[0] = 0
                zomb.pos[1] += zombie_speed * pos[1]

        if wall_3_rect.colliderect(zomb.zomb_rect):
            pos = [zomb.zomb_rect.centerx - wall_3_rect.centerx, zomb.zomb_rect.centery - wall_3_rect.centery]

            if (abs(pos[0]) / (wall_3_rect.width / 2)) > (abs(pos[1]) / (wall_3_rect.height / 2)):
                pos[0] = signum(pos[0])
                pos[1] = 0
                zomb.pos[0] += zombie_speed * pos[0]

            if (abs(pos[0]) / (wall_3_rect.width / 2)) < (abs(pos[1]) / (wall_3_rect.height / 2)):
                pos[1] = signum(pos[1])
                pos[0] = 0
                zomb.pos[1] += zombie_speed * pos[1]

        if wall_4_rect.colliderect(zomb.zomb_rect):
            pos = [zomb.zomb_rect.centerx - wall_4_rect.centerx, zomb.zomb_rect.centery - wall_4_rect.centery]

            if (abs(pos[0]) / (wall_4_rect.width / 2)) > (abs(pos[1]) / (wall_4_rect.height / 2)):
                pos[0] = signum(pos[0])
                pos[1] = 0
                zomb.pos[0] += zombie_speed * pos[0]

            if (abs(pos[0]) / (wall_4_rect.width / 2)) < (abs(pos[1]) / (wall_4_rect.height / 2)):
                pos[1] = signum(pos[1])
                pos[0] = 0
                zomb.pos[1] += zombie_speed * pos[1]

        if wall_5_rect.colliderect(zomb.zomb_rect):
            pos = [zomb.zomb_rect.centerx - wall_5_rect.centerx, zomb.zomb_rect.centery - wall_5_rect.centery]

            if (abs(pos[0]) / (wall_5_rect.width / 2)) > (abs(pos[1]) / (wall_5_rect.height / 2)):
                pos[0] = signum(pos[0])
                pos[1] = 0
                zomb.pos[0] += zombie_speed * pos[0]

            if (abs(pos[0]) / (wall_5_rect.width / 2)) < (abs(pos[1]) / (wall_5_rect.height / 2)):
                pos[1] = signum(pos[1])
                pos[0] = 0
                zomb.pos[1] += zombie_speed * pos[1]





    if wall_1_rect.colliderect(sold_rect):
        temp_pos = [sold_rect.centerx - wall_1_rect.centerx, sold_rect.centery - wall_1_rect.centery]

        if (abs(temp_pos[0]) / (wall_1_rect.width / 2)) > (abs(temp_pos[1]) / (wall_1_rect.height / 2)):
            temp_pos[0] = signum(temp_pos[0])
            temp_pos[1] = 0
            player.x += player_speed * temp_pos[0]

        if (abs(temp_pos[0]) / (wall_1_rect.width / 2)) < (abs(temp_pos[1]) / (wall_1_rect.height / 2)):
            temp_pos[1] = signum(temp_pos[1])
            temp_pos[0] = 0
            player.y += player_speed * temp_pos[1]

    if wall_2_rect.colliderect(sold_rect):
        temp_pos = [sold_rect.centerx - wall_2_rect.centerx, sold_rect.centery - wall_2_rect.centery]

        if (abs(temp_pos[0]) / (wall_2_rect.width / 2)) > (abs(temp_pos[1]) / (wall_2_rect.height / 2)):
            temp_pos[0] = signum(temp_pos[0])
            temp_pos[1] = 0
            player.x += player_speed * temp_pos[0]

        if (abs(temp_pos[0]) / (wall_2_rect.width / 2)) < (abs(temp_pos[1]) / (wall_2_rect.height / 2)):
            temp_pos[1] = signum(temp_pos[1])
            temp_pos[0] = 0
            player.y += player_speed * temp_pos[1]
    
    if wall_3_rect.colliderect(sold_rect):
        temp_pos = [sold_rect.centerx - wall_3_rect.centerx, sold_rect.centery - wall_3_rect.centery]

        if (abs(temp_pos[0]) / (wall_3_rect.width / 2)) > (abs(temp_pos[1]) / (wall_3_rect.height / 2)):
            temp_pos[0] = signum(temp_pos[0])
            temp_pos[1] = 0
            player.x += player_speed * temp_pos[0]

        if (abs(temp_pos[0]) / (wall_3_rect.width / 2)) < (abs(temp_pos[1]) / (wall_3_rect.height / 2)):
            temp_pos[1] = signum(temp_pos[1])
            temp_pos[0] = 0
            player.y += player_speed * temp_pos[1]

    if wall_4_rect.colliderect(sold_rect):
        temp_pos = [sold_rect.centerx - wall_4_rect.centerx, sold_rect.centery - wall_4_rect.centery]

        if (abs(temp_pos[0]) / (wall_4_rect.width / 2)) > (abs(temp_pos[1]) / (wall_4_rect.height / 2)):
            temp_pos[0] = signum(temp_pos[0])
            temp_pos[1] = 0
            player.x += player_speed * temp_pos[0]

        if (abs(temp_pos[0]) / (wall_4_rect.width / 2)) < (abs(temp_pos[1]) / (wall_4_rect.height / 2)):
            temp_pos[1] = signum(temp_pos[1])
            temp_pos[0] = 0
            player.y += player_speed * temp_pos[1]

    if wall_5_rect.colliderect(sold_rect):
        temp_pos = [sold_rect.centerx - wall_5_rect.centerx, sold_rect.centery - wall_5_rect.centery]

        if (abs(temp_pos[0]) / (wall_5_rect.width / 2)) > (abs(temp_pos[1]) / (wall_5_rect.height / 2)):
            temp_pos[0] = signum(temp_pos[0])
            temp_pos[1] = 0
            player.x += player_speed * temp_pos[0]

        if (abs(temp_pos[0]) / (wall_5_rect.width / 2)) < (abs(temp_pos[1]) / (wall_5_rect.height / 2)):
            temp_pos[1] = signum(temp_pos[1])
            temp_pos[0] = 0
            player.y += player_speed * temp_pos[1]


    player.movement(bullets)

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
