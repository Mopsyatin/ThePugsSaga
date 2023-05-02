import pgzero, pgzrun, pygame, random
#pygame sounds
pygame.mixer.init()
victory_sound = pygame.mixer.Sound('victory.mp3')
door_open_sound = pygame.mixer.Sound('dooropensound.mp3')
buysound = pygame.mixer.Sound('buysound.wav')
buttonsound = pygame.mixer.Sound('buttonsound.wav')
flayersound = pygame.mixer.Sound('flayersound.wav')
skinsound = pygame.mixer.Sound('skinchoosesound.wav')
losesound = pygame.mixer.Sound('losesound.wav')
damagesound = pygame.mixer.Sound('damagesound.mp3')
crushsound = pygame.mixer.Sound('spikecrushsound.wav')
eatsound = pygame.mixer.Sound('eatsound.wav')
pygame.mixer.music.load('forest.wav')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(5)
buttonsound.set_volume(1)
buysound.set_volume(3)
door_open_sound.set_volume(3)
skinsound.set_volume(3)
flayersound.set_volume(3)
damagesound.set_volume(3)
crushsound.set_volume(3)
eatsound.set_volume(3)
victory_sound.set_volume(4)
losesound.set_volume(4)
#Variables
TITLE = "The pug's saga"
WIDTH = 1000
HEIGHT = 590
FPS = 120
mode = 'menu'
#names
count = 0

pug_rotation = "right"
collection_mode = "shop"
end_mode = "win"
trophy_now = "pancake"
trophi = "burger"

persec = 3240
hprange = 351
i = 0

index = 0
lvl = 1
what_room = 1
count_levels = 10
reward_show = 0

room_number_x_1 = 250
room_number_x_2 = 500
room_number_x_3 = 750

index_skin = 0
index_trophy = 0

speed = 6
jump = 100
reward = 100
speed_water = 4

#lists
trophey_collection = []
rooms = []

fishes = []
sharkes = []

fish_colors = ["orangefish", "redfish", "greenfish", "yellowfish", "bluefish"]

variable_rooms_trophy_water = ["trophyroom_water", "trophyroom1_water", "trophyroom2_water","trophyroom3_water", "trophyroom4_water", "trophyroom5_water"]
variable_rooms_trophy = ["trophyroom", "trophyroom1", "trophyroom2", "trophyroom3", "trophyroom4","trophyroom5", "trophyroom6"]

variable_rooms_water = ["room_water", "room1_water", "room2_water", "room3_water", "room4_water","room5_water", "room6_water", "room7_water", "room8_water"]
variable_rooms = ["room", "room1", "room2", "room3", "room4", "room5", "room6", "room7", "room8"]

trophey_game_water = [ "pancake_water", "ramen_water", "taco_water", "donut_water", "nyancat_water", "burger_water" ]
trophey_game = ["pancake", "ramen", "taco", "donut", "nyancat", "burger"]

#dictionaries

types_rooms = [{"max_doors": 1, "room": "random", "rooms_variable_spisok": variable_rooms_trophy},
                  {"max_doors": 1, "room": "random", "rooms_variable_spisok": variable_rooms},
                  {"max_doors": 3, "room": "random", "chance": 50, "rooms_variable_spisok": variable_rooms},
                  {"max_doors": 3, "room": "random", "chance": 40, "rooms_variable_spisok": variable_rooms},
                  {"max_doors": 3, "room": "random", "chance": 10, "rooms_variable_spisok": variable_rooms}
                  ]

types_rooms_water = [{"max_doors": 1, "room": "random", "rooms_variable_spisok": variable_rooms_trophy_water},
                  {"max_doors": 1, "room": "random", "rooms_variable_spisok": variable_rooms_water},
                  {"max_doors": 3, "room": "random", "chance": 50, "rooms_variable_spisok": variable_rooms_water}
                  ]

skins_collection = [{"right":"pugr", "left": "pugl", "price": 0, "bonus_type": "nothing", "bonus": 0, "bonus_text": "default", "y": 457, "right_run": "movingpugr", "left_run": "movingpugl", "left_water": "pugl_water", "right_water": "pugr_water", "right_run_water": "movingpugr_water", "left_run_water": "movingpugl_water"},
                    {"right":"gentlemanpugr", "left": "gentlemanpugl", "price": 2500, "bonus_type": "reward", "bonus": 100, "bonus_text": "reward + ", "y": 446, "right_run":"runninggentlemanpugr", "left_run": "runninggentlemanpugl", "left_water": "gentlemanpugl_water", "right_water": "gentlemanpugr_water", "right_run_water":"runninggentlemanpugr_water", "left_run_water": "runninggentlemanpugl_water"},
                    {"right":"fishpugr", "left": "fishpugl", "price": 2500, "bonus_type": "speed_water", "bonus": 6, "bonus_text": "speed in water +", "y": 457, "right_run":"runningfishpugr", "left_run": "runningfishpugl", "left_water": "swimmingfishpugl", "right_water": "swimmingfishpugr", "right_run_water":"swimmingfishpugr", "left_run_water": "swimmingfishpugl"},
                    {"right":"frogpugr", "left": "frogpugl", "price": 3500, "bonus_type": "jump", "bonus": 50, "bonus_text": "jump + ", "y": 457, "right_run":"runningfrogpugr", "left_run": "runningfrogpugl", "left_water": "frogpugl_water", "right_water": "frogpugr_water", "right_run_water":"runningfrogpugr_water", "left_run_water": "runningfrogpugl_water" },
                    {"right":"flushpugr", "left": "flushpugl", "price": 5000, "bonus_type": "speed", "bonus": 5, "bonus_text": "speed +", "y": 457, "right_run":"runningflushpugr", "left_run": "runningflushpugl", "left_water": "flushpugl_water", "right_water": "flushpugr_water", "right_run_water":"runningflushpugr_water", "left_run_water": "runningflushpugl_water"},
                    {"right":"stupidpugr", "left": "stupidpugl", "price": 10000, "bonus_type": "stupid", "bonus": 0, "bonus_text": "._.", "y": 457,"right_run":"stupidpugr", "left_run": "stupidpugl", "left_water": "stupidpugl_water", "right_water": "stupidpugr_water", "right_run_water":"stupidpugr_water", "left_run_water": "stupidpugl_water" }
                    ]

skin_now = skins_collection[0]


#funktions
def croos_use():
    global mode, persec, i
    mode = 'menu'
    persec = 3240
    pygame.mixer.music.load('forest.wav')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    i = 0

def arrow_use(arrow):
    global index_skin, index_trophy
    arrow.y -= 20
    animate(arrow, tween='bounce_end', duration=0.5, y=300)
    if arrow == right:
        if collection_mode == "shop":
            index_skin += 1
        elif collection_mode == "collection":
            index_trophy += 1
    if arrow == left:
        if collection_mode == "shop":
            index_skin -= 1
        elif collection_mode == "collection":
            index_trophy -= 1
    buttonsound.stop()
    buttonsound.play()

def skin_buy():
    global skin_now, count, jump, speed_water, speed, reward
    if count >= skins_collection[index_skin]["price"]:
        count -= skins_collection[index_skin]["price"]
        speed = 6
        jump = 100
        reward = 100
        speed_water = 4
        pug.image = skins_collection[index_skin]["right"]
        skin_now = skins_collection[index_skin]
        if skins_collection[index_skin]["bonus_type"] == "reward":
            reward += skins_collection[index_skin]["bonus"]
        elif skins_collection[index_skin]["bonus_type"] == "jump":
            jump += skins_collection[index_skin]["bonus"]
        elif skins_collection[index_skin]["bonus_type"] == "speed":
            speed += skins_collection[index_skin]["bonus"]
        elif skins_collection[index_skin]["bonus_type"] == "speed_water":
            speed_water += skins_collection[index_skin]["bonus"]
        elif index_skin == 3:
            speed_water += 2
        if skins_collection[index_skin]['price'] != 0:
            buysound.stop()
            buysound.play()
        elif skins_collection[index_skin]['price'] == 0:
            skinsound.stop()
            skinsound.play()
        skins_collection[index_skin]["price"] = 0
        pug.angle = 0

def collection_flayer_use(_mode):
    global collection_mode
    collection_mode = _mode
    flayersound.stop()
    flayersound.play()

def music_use():
    if musicreg.image == 'musicon':
        musicreg.image = 'musicoff'
        pygame.mixer.music.set_volume(0)
    elif musicreg.image == 'musicoff':
        musicreg.image = 'musicon'
        pygame.mixer.music.set_volume(5)
    buttonsound.stop()
    buttonsound.play()

def but_menu_use():
    global persec, i, mode
    persec = 6000
    pygame.mixer.music.load('fonmusic.mp3')
    pygame.mixer.music.stop()
    pygame.mixer.music.play()
    i = 0
    buttonsound.stop()
    buttonsound.play()
    if what_room == 1:
        pug.image = skin_now["right"]
    elif what_room == 2:
        pug.image = skin_now["right_water"]
    pug.y = skin_now["y"]
    pug.angle = 0
    mode = 'game'
    
def playbut_use():
    global persec, i, reward_show, index, count_levels, lvl, mode
    pug.hp = 100
    reward_show = 0
    index = 0
    count_levels = 10
    lvl = 1

def trophey_use():
    global mode, end_mode, reward_show, count, trophi
    victory_sound.play()
    pygame.mixer.music.stop()
    trophi = trophey_game.pop(trophy_now)
    trophey_game_water.pop(trophy_now)
    trophey_collection.append(trophi)
    rooms.clear()
    reward_show += lvl * reward
    count += lvl * 100
    end_mode = "win"
    mode = "end"
    pug.image = skin_now["right"]

def dominant_door_use():
    global index, reward_show, lvl, count, count_levels
    pug.y = skin_now["y"]
    door_open_sound.play()
    reward_show += lvl * reward
    count += lvl * reward
    count_levels += 10
    lvl += 1
    index = 0

def door_use(door):
    global index
    door_open_sound.play()
    pug.pos = (250, skin_now["y"])
    index = rooms[index][door]
    if what_room == 1:
        item7.y = 20
        item8.y = 20

def fish_eat():
    for i in range(len(rooms[index]["fish"])):
        if pug.colliderect(rooms[index]["fish"][i]) and keyboard.e:
            if pug.hp != 100:
                pug.hp += 5
                eatsound.play()
            if pug.hp > 94:
                pug.hp = 100
                eatsound.play()
            rooms[index]["fish"][i].x = -100

def fish_update():
    for i in range(len(rooms[index]["fish"])):
        rooms[index]["fish"][i].x -= rooms[index]["fish"][i].speed
        if rooms[index]["fish"][i].x <= -20:
            rooms[index]["fish"][i].pos = (random.randint(1000, 1500), random.randint(20, 500))
            rooms[index]["fish"][i].image = fish_colors[random.randint(0,len(fish_colors) - 1)]
            rooms[index]["fish"][i].speed = random.randint(2, 6)

def shark_update():
    for i in range(len(rooms[index]["sharks"])):
        rooms[index]["sharks"][i].x -= rooms[index]["sharks"][i].speed
        if rooms[index]["sharks"][i].x <= -20:
            rooms[index]["sharks"][i].pos = (random.randint(1000, 1500), random.randint(20, 500))
            rooms[index]["sharks"][i].speed = random.randint(2, 6)
            if rooms[index]["sharks"][i].image == "shark_instasamka":
                rooms[index]["sharks"][i].image = "shark"
        if pug.colliderect(rooms[index]["sharks"][i]) and rooms[index]["sharks"][i].image != "shark_instasamka":
            if skin_now["bonus_type"] == "stupid":
                rooms[index]["sharks"][i].x += 100
                rooms[index]["sharks"][i].image = "shark_instasamka"
                crushsound.play()
            else:
                if pug.hp > 20:
                    damagesound.play()
                pug.hp -= 20
                pug.x -= 20
                if pug.y <= 250:
                    pug.y += 100
                else:
                    pug.y -= 100

def flowers_update():
    if rooms[index]["flowers_number"] == 1 or rooms[index]["flowers_number"] == 3:
        item7.y += 7
        if item7.y >= 500:
            item7.y = 20
        if pug.colliderect(item7):
            item7.y = 20
            pug.hp -= 20
            if pug.hp > 20:
                damagesound.play()
    if rooms[index]["flowers_number"] == 2 or rooms[index]["flowers_number"] == 3:
        item8.y += 7
        if item8.y >= 500:
            item8.y = 20
        if pug.colliderect(item8):
            item8.y = 20
            pug.hp -= 20
            if pug.hp > 20:
                damagesound.play()

def spikes_colliderect():
    if pug.colliderect(item1) and (rooms[index]["item_number"] == 1 or rooms[index]["item_number"] == 3):
        if skin_now["bonus_type"] != "stupid":
            if pug.image == skin_now["right"] or  pug.image == skin_now["right_run"]:
                pug.x -= 70
            else:
                pug.x += 70
            pug.hp -= 10
            if pug.hp > 0:
                damagesound.play()
        else:
            if rooms[index]["item_number"] == 3:
                rooms[index]["item_number"] = 2
            else:
                rooms[index]["type"] = 2
            crushsound.play()
    if pug.colliderect(item2) and (rooms[index]["item_number"] == 2 or rooms[index]["item_number"] == 3):
        if skin_now["bonus_type"] != "stupid":
            if pug.image == skin_now["right"] or  pug.image == skin_now["right_run"]:
                pug.x -= 70
            else:
                pug.x += 70
            pug.hp -= 10
            if pug.hp > 0:
                damagesound.play()
        else:
            if rooms[index]["item_number"] == 3:
                rooms[index]["item_number"] = 1
            else:
                rooms[index]["type"] = 2
            crushsound.play()

def door_open():
    global room_number_x_1, room_number_x_2, room_number_x_3
    if what_room == 1:
        if pug.colliderect(door1):
            door1.image = "openeddoor"
            room_number_x_1 = 275
        else:
            door1.image = "door1"
            room_number_x_1 = 250
        if pug.colliderect(door2):
            door2.image = "openeddoor"
            room_number_x_2 = 525
        else:
            door2.image = "door1"
            room_number_x_2 = 500
        if pug.colliderect(door3):
            door3.image = "openeddoor"
            room_number_x_3 = 775
        else:
            door3.image = "door1"
            room_number_x_3 = 750
        if pug.colliderect(dominant_door):
            dominant_door.image = "openeddominantdoor"
        else:
            dominant_door.image = "dominantdoor"
    elif what_room == 2:
        if pug.colliderect(door1):
            door1.image = "openeddoor_water"
            room_number_x_1 = 275
        else:
            door1.image = "door1_water"
            room_number_x_1 = 250
        if pug.colliderect(door2):
            door2.image = "openeddoor_water"
            room_number_x_2 = 525
        else:
            door2.image = "door1_water"
            room_number_x_2 = 500
        if pug.colliderect(door3):
            door3.image = "openeddoor_water"
            room_number_x_3 = 775
        else:
            door3.image = "door1_water"
            room_number_x_3 = 750
        if pug.colliderect(dominant_door):
            dominant_door.image = "openeddominantdoor_water"
        else:
            dominant_door.image = "dominantdoor_water"

def items_draw(number, item_1, item_2):
    if rooms[index][number] == 1:
        item_1.draw()
    elif rooms[index][number] == 2:
        item_2.draw()
    elif rooms[index][number] == 3:
        item_1.draw()
        item_2.draw()

def hp_draw():
    if pug.hp >= 91:
        for i in range(10):
            hpstripe[i].draw()
    if pug.hp >= 81:
        for i in range(9):
            hpstripe[i].draw()
    elif pug.hp >= 71:
        for i in range(8):
            hpstripe[i].draw()
    elif pug.hp >= 61:
        for i in range(7):
            hpstripe[i].draw()
    elif pug.hp >= 51:
        for i in range(6):
            hpstripe[i].draw()
    elif pug.hp >= 41:
        for i in range(5):
            hpstripe[i].draw()
    elif pug.hp >= 31:
        for i in range(4):
            hpstripe[i].draw()
    elif pug.hp >= 21:
        for i in range(3):
            hpstripe[i].draw()
    elif pug.hp >= 11:
        for i in range(2):
            hpstripe[i].draw()
    elif pug.hp >= 1:
        for i in range(1):
            hpstripe[i].draw()
    elif pug.hp == 0:
        for i in range(0):
            hpstripe[i].draw()
    hpline.draw()
    screen.draw.text(str(pug.hp),center=(400, 565),color='white',fontsize=40)

def door_draw():
    if int(rooms[index]["amount_door"]) == 1:
        door1.draw()
        screen.draw.text(str(rooms[index]["door_1"]),
                         center=(room_number_x_1, 367),
                         color='black',
                         fontsize=38)
    elif int(rooms[index]["amount_door"]) == 2:
        door1.draw()
        screen.draw.text(str(rooms[index]["door_1"]),
                         center=(room_number_x_1, 367),
                         color='black',
                         fontsize=38)
        door2.draw()
        screen.draw.text(str(rooms[index]["door_2"]),
                         center=(room_number_x_2, 367),
                         color='black',
                         fontsize=38)
    elif int(rooms[index]["amount_door"]) == 3:
        door1.draw()
        screen.draw.text(str(rooms[index]["door_1"]),
                         center=(room_number_x_1, 367),
                         color='black',
                         fontsize=38)
        door2.draw()
        screen.draw.text(str(rooms[index]["door_2"]),
                         center=(room_number_x_2, 367),
                         color='black',
                         fontsize=38)
        door3.draw()
        screen.draw.text(str(rooms[index]["door_3"]),
                         center=(room_number_x_3, 367),
                         color='black',
                         fontsize=38)
    if rooms[index]["type"] == 1:
        dominant_door.draw()

def generic():
    global rooms, trophy_now, trophy_end, what_room, fishes, sharkes
    pug.pos = (150, skin_now["y"])
    what_room = random.randint(1, 2)
    rooms = [{"type": 2, "amount_door": 0, "index": 0}]
    for i in range(count_levels):
        now = i + 1
        how = random.randint(0, len(rooms) - 1)
        while len(rooms[how].keys()) - 3 >= types_rooms[rooms[how]
                                                        ["type"]]["max_doors"]:
            how = random.randint(0, len(rooms) - 1)
        rooms.append({"amount_door": 0, "index": now})
        if now == count_levels:
            if lvl == 5 and len(trophey_game) > 0:
                rooms[now]["type"] = 0
                trophy_now = random.randint(0, len(trophey_game) - 1)
                if what_room == 1:
                    trophy.image = trophey_game[trophy_now]
                elif what_room == 2:
                    trophy.image = trophey_game_water[trophy_now]
            else:
                rooms[now]["type"] = 1
        else:
            if what_room == 1:
                type = random.randint(2, len(types_rooms) - 1)
                while not "type" in rooms[now]:
                    if "chance" in types_rooms[type]:
                        chance = random.randint(0, 100)
                        if chance > types_rooms[type]["chance"]:
                            type = random.randint(2, len(types_rooms) - 1)
                        else:
                            rooms[now]["type"] = type
            elif what_room == 2:
                type = random.randint(2, len(types_rooms_water) - 1)
                while not "type" in rooms[now]:
                    if "chance" in types_rooms_water[type]:
                        chance = random.randint(0, 100)
                        if chance > types_rooms_water[type]["chance"]:
                            type = random.randint(2,
                                                  len(types_rooms_water) - 1)
                        else:
                            rooms[now]["type"] = type
        if not "door_1" in rooms[how]:
            rooms[how]["door_1"] = now
            rooms[how]["amount_door"] = 1
        elif not "door_2" in rooms[how]:
            rooms[how]["door_2"] = now
            rooms[how]["amount_door"] = 2
        elif not "door_3" in rooms[how]:
            rooms[how]["door_3"] = now
            rooms[how]["amount_door"] = 3
        rooms[now]["door_1"] = rooms[how]["index"]
    for i in range(len(rooms)):
        if rooms[i]["amount_door"] == 0:
            rooms[i]["amount_door"] = 1
        if types_rooms[rooms[i]["type"]]["room"] == "random":
            if what_room == 1:
                rooms[i]["room_type"] = random.randint(
                    0,
                    len(types_rooms[rooms[i]["type"]]["rooms_variable_spisok"])
                    - 1)
            elif what_room == 2:
                rooms[i]["room_type"] = random.randint(
                    0,
                    len(types_rooms_water[rooms[i]["type"]]
                        ["rooms_variable_spisok"]) - 1)
        if what_room == 1:
            if (rooms[i]["type"] == 3 or rooms[i]["type"] == 4):
                rooms[i]["item_number"] = random.randint(1, 3)
            flower = random.randint(0, 11)
            if flower - 8 > 0:
                for j in range(flower - 8):
                    rooms[i]["flowers_number"] = flower - 8
        if what_room == 2:
            sharkes = []
            for j in range(random.randint(0, 2)):
                shark = Actor(
                    "shark",
                    (random.randint(1000, 1500), random.randint(20, 500)))
                shark.speed = random.randint(3, 7)
                sharkes.append(shark)
            rooms[i]["sharks"] = sharkes
            fishes = []
            for j in range(random.randint(0, 3)):
                fish = Actor(
                    fish_colors[random.randint(0,
                                               len(fish_colors) - 1)],
                    (random.randint(1000, 1500), random.randint(20, 500)))
                fish.speed = random.randint(2, 6)
                fishes.append(fish)
            rooms[i]["fish"] = fishes
    pug.x += 1
    if what_room == 1:
        pug.image = skin_now["right"]
    elif what_room == 2:
        pug.image = skin_now["right_water"]
    if what_room == 1:
        item7.y = 20
        item8.y = 20

def mushroom_colliderct():
    if rooms[index]["type"] == 4:
        if (rooms[index]["item_number"] == 1 or rooms[index]["item_number"] == 3) and pug.colliderect(item3) and keyboard.e:
            if pug.hp != 100:
                pug.hp += 20
            if pug.hp > 80:
                pug.hp = 100
            if rooms[index]["item_number"] == 3:
                rooms[index]["item_number"] = 2
            else:
                rooms[index]["type"] = 2
            eatsound.play()
        if (rooms[index]["item_number"] == 2 or rooms[index]["item_number"] == 3) and pug.colliderect(item4) and keyboard.e:
            if pug.hp != 100:
                pug.hp += 20
            if pug.hp > 80:
                pug.hp = 100
            if rooms[index]["item_number"] == 3:
                rooms[index]["item_number"] = 1
            else:
                rooms[index]["type"] = 2
            eatsound.play()

def music():
    global i, persec
    i += 1
    if persec == 6000:
        if i == persec:
            pygame.mixer.music.load('fonmusic.mp3')
            pygame.mixer.music.stop()
            pygame.mixer.music.play()
            i = 0
    elif persec == 3240:
        if i == persec:
            pygame.mixer.music.load('forest.wav')
            pygame.mixer.music.stop()
            pygame.mixer.music.play()
            i = 0
#Actors

musicreg = Actor('musicon', (30, 30))

losefon = Actor("losefon")
winfon = Actor("winfon")
colfon = Actor('colfon')
menu = Actor('menufon')

door1 = Actor('door1', (250, 410))
door2 = Actor('door1', (500, 410))
door3 = Actor('door1', (750, 410))
dominant_door = Actor('dominantdoor', (500, 410))

playbut = Actor('playbut', (500, 150))
collectinbut = Actor('collectionbut', (500, 300))
continuebut = Actor("continuebut", (500, 450))

pug = Actor(skin_now["right"], (150, skin_now["y"]))
room = Actor("room")
guidinglight = Actor("guidinglight", (633, 390))
trophy = Actor("burger", (633, 395))

cross = Actor('cross', (985, 15))
skin = Actor("pugr", (500, 300))
trophy_collection = Actor("burger", (500, 300))
clue = Actor("presswindow", (890, 540))
shopflayer = Actor('shopflayer', (100, 25))
collectionflayer = Actor('collectionflayer', (300, 25))
wallet = Actor("wallet", (850, 50))
left = Actor("left", (340, 300))
right = Actor("right", (660, 300))
coin = Actor("coin", (550, 200))
hpline = Actor('hpstripe', (430, 543))

item1 = Actor('spike', (375, 480))
item2 = Actor('spike', (625, 480))
item3 = Actor('mushroom', (375, 480))
item4 = Actor('mushroom', (625, 480))
item5 = Actor("poisonedflower", (375, 25))
item6 = Actor("poisonedflower", (625, 25))
item7 = Actor("poison", (375, 20))
item8 = Actor("poison", (625, 20))

#pugs hp
pug.hp = 100
hpstripe = []
for i in range(10):
    hp10 = Actor('10hp', (hprange, 564))
    hpstripe.append(hp10)
    hprange += 20

#Draw
def draw():
    global persec, i
    if mode == 'menu':
        menu.draw()
        musicreg.draw()
        playbut.draw()
        collectinbut.draw()
        if len(rooms) > 0:
            continuebut.draw()
        wallet.draw()
        screen.draw.text(str(count),
                         center=(930, 53),
                         color='black',
                         fontsize=40)
        
    elif mode == 'game':
        room.draw()
        musicreg.draw()
        door_draw()
        cross.draw()
        screen.draw.text(str(lvl), center=(105, 545), color='black', fontsize=50)
        screen.draw.text(str(rooms[index]["index"]),center=(230, 545), color='black', fontsize=50)
        if (pug.colliderect(door1) and int(rooms[index]["amount_door"]) >= 1) or (pug.colliderect(door2) and int(rooms[index]["amount_door"]) >= 2) or ( pug.colliderect(door3) and int(rooms[index]["amount_door"]) >= 3) or ( pug.colliderect(dominant_door) and rooms[index]["type"] == 1) or ( pug.colliderect(trophy) and rooms[index]["type"] == 0) or ( rooms[index]["type"] == 4 and pug.colliderect(item1) and (rooms[index]["item_number"] == 3 or rooms[index]["item_number"] == 1)) or ( rooms[index]["type"] == 4 and pug.colliderect(item2) and (rooms[index]["item_number"] == 3 or rooms[index]["item_number"] == 2)):
            clue.draw()
            screen.draw.text("E",center=(945, 543),color='black',fontsize=80)
        if what_room == 1:
            if rooms[index]["type"] == 3:
                if rooms[index]["type"] == 3 or rooms[index]["type"] == 4:
                    items_draw("item_number", item1, item2)
            if rooms[index]["type"] == 4:
                if rooms[index]["type"] == 3 or rooms[index]["type"] == 4:
                    items_draw("item_number", item3, item4)
            if "flowers_number" in rooms[index]:
                items_draw("flowers_number", item7, item8)
                items_draw("flowers_number", item5, item6)
        else:
            if "sharks" in rooms[index]:
                for i in range(len(rooms[index]["sharks"])):
                    rooms[index]["sharks"][i].draw()
            if "fish" in rooms[index]:
                for i in range(len(rooms[index]["fish"])):
                    rooms[index]["fish"][i].draw()
                    if pug.colliderect(rooms[index]["fish"][i]):
                        clue.draw()
                        screen.draw.text("E",
                                         center=(945, 543),
                                         color='black',
                                         fontsize=80)
        if rooms[index]["type"] == 0:
            if guidinglight.y == trophy.y:
                guidinglight.draw()
            trophy.draw()
        pug.draw()
        hp_draw()
        
    elif mode == 'col':
        colfon.draw()
        shopflayer.draw()
        collectionflayer.draw()
        wallet.draw()
        cross.draw()
        screen.draw.text(str(count), center=(930, 53), color='black', fontsize=40)
        if collection_mode == "shop":
            skin.draw()
            if index_skin != 0:
                left.draw()
            if index_skin != len(skins_collection) - 1:
                right.draw()
            if skins_collection[index_skin]["bonus"] != 0:
                screen.draw.text(skins_collection[index_skin]["bonus_text"] +
                                 str(skins_collection[index_skin]["bonus"]),
                                 center=(500, 400),
                                 color='black',
                                 fontsize=40)
            else:
                screen.draw.text(skins_collection[index_skin]["bonus_text"],
                                 center=(500, 400),
                                 color='black',
                                 fontsize=40)
            if skins_collection[index_skin]["price"] != 0:
                coin.draw()
                screen.draw.text(str(skins_collection[index_skin]["price"]), center=(500, 200), color='black', fontsize=40)   
        elif collection_mode == "collection":
            if len(trophey_collection) != 0:
                trophy_collection.draw()
                if index_trophy != 0:
                    left.draw()
                if index_trophy != len(trophey_collection) - 1:
                    right.draw()
                screen.draw.text(trophey_collection[index_trophy], center=(500, 400), color='black', fontsize=40)
                
    elif mode == "end":
        if end_mode == "win":
            winfon.draw()
            wallet.draw()
            pug.draw()
            cross.draw()
            screen.draw.text(" + " + str(reward_show),center=(930, 53),color='green',fontsize=40)
            Actor(trophi, (550, 450)).draw()
            screen.draw.text("Your trophy:", center=(420, 450), color='black', fontsize=40)
        elif end_mode == "lose":
            losefon.draw()
            wallet.draw()
            pug.draw()
            cross.draw()
            screen.draw.text(" + " + str(reward_show), center=(930, 53), color='green', fontsize=40)

#Update
def update(dt):
    global mode, index, pug_rotation, persec, i, end_mode, room_number_x_1, room_number_x_2, room_number_x_3
    music()
    if mode == "game":
        door_open()
        #trophey
        if rooms[index]["type"] == 0:
            if pug.x >= 500 and trophy.y == 395 and pug.x <= 666:
                animate(trophy, tween="decelerate", duration=0.5, y=390)
            elif (pug.x < 500 or pug.x > 666) and trophy.y == 390:
                animate(trophy, tween="accelerate", duration=0.5, y=395)
        
        #normal 
        if skin_now["bonus_type"] != "stupid":
            if what_room == 1:
                if pug_rotation == 1:
                    pug.image = skin_now["left"]
                elif pug_rotation == 2:
                    pug.image = skin_now["right"]
            elif what_room == 2:
                if pug_rotation == 1:
                    pug.image = skin_now["left_water"]
                elif pug_rotation == 2:
                    pug.image = skin_now["right_water"]

        #died
        if pug.hp <= 0:
            pug.image = skin_now["right"]
            mode = "end"
            end_mode = "lose"
            rooms.clear()
            pygame.mixer.music.stop()
            losesound.play()
        #gravitation
        if pug.y < skin_now["y"] and what_room == 1:
            pug.y += 5
        #Keyboard controls
        if keyboard.space or keyboard.w or keyboard.up:
            if what_room == 1 and pug.y == skin_now["y"]:
                animate(pug,
                        tween='decelerate',
                        duration=0.5,
                        y=skin_now["y"] - jump)
            if what_room == 2 and pug.y > 50:
                pug.y -= 5
        if (keyboard.right or keyboard.d) and pug.x < 940:
            if what_room == 1:
                if "right_run" in skin_now:
                    pug.image = skin_now["right_run"]
                else:
                    pug.image = skin_now["right"]
                pug.x += speed
            elif what_room == 2:
                if "right_run_water" in skin_now:
                    pug.image = skin_now["right_run_water"]
                else:
                    pug.image = skin_now["right_water"]
                pug.x += speed_water
            pug_rotation = 2
            if skin_now["bonus_type"] == "stupid":
                pug.angle -= 10
        if (keyboard.left or keyboard.a) and pug.x > 60:
            if what_room == 1:
                if "right_run" in skin_now:
                    pug.image = skin_now["left_run"]
                else:
                    pug.image = skin_now["left"]
                pug.x -= speed
            elif what_room == 2:
                if "right_run_water" in skin_now:
                    pug.image = skin_now["left_run_water"]
                else:
                    pug.image = skin_now["left_water"]
                pug.x -= speed_water
            pug_rotation = 1
            if skin_now["bonus_type"] == "stupid":
                pug.angle += 10        
        if ((keyboard.down or keyboard.s) and pug.y <= skin_now["y"]) and what_room == 2:
            pug.y += 5

        #rooms specials
        if mode == "game" and what_room == 1:
            if types_rooms[rooms[index]["type"]]["room"] == "random":
                room.image = types_rooms[rooms[index]["type"]]["rooms_variable_spisok"][rooms[index]["room_type"]]
            else:
                room.image = types_rooms[rooms[index]["type"]]["room"]
            if "flowers_number" in rooms[index]:
                flowers_update()
            if rooms[index]["type"] == 3:
                spikes_colliderect()
        elif mode == "game" and what_room == 2:
            if types_rooms_water[rooms[index]["type"]]["room"] == "random":
                room.image = types_rooms_water[rooms[index]["type"]]["rooms_variable_spisok"][rooms[index]["room_type"]]
            else:
                room.image = types_rooms_water[rooms[index]["type"]]["room"]
            if "sharks" in rooms[index]:
                shark_update()
            if "fish" in rooms[index]:
                fish_update()
                
                
    elif mode == "col":
        if collection_mode == "shop":
            shopflayer.image = "shopflayeron"
            collectionflayer.image = "collectionflayer"
            skin.image = skins_collection[index_skin]["right"]
        elif collection_mode == "collection":
            collectionflayer.image = "collectionflayeron"
            shopflayer.image = "shopflayer"
            if len(trophey_collection) != 0:
                trophy_collection.image = trophey_collection[index_trophy]

    elif mode == "end":
        if pug.image == ('gentlemanpugr' or 'gentlemanpugl'):
                pug.image = 'halfgentlemanpugr'
        if end_mode == "win":
            pug.image = skin_now["right"]
            pug.pos = (465, 348)
            pug.angle = 0
        elif end_mode == "lose":
            pug.image = skin_now["right"]
            pug.pos = (468, 320)
            pug.angle = 0

#doors_open
def on_key_down(key):
    global index, lvl, count_levels, count, rooms, mode, trophy_now, trophey_game, trophey_collection, end_mode, reward_show, trophi
    if mode == 'game':
        if "door_1" in rooms[index] and pug.colliderect(door1) and keyboard.e:
            door_use("door_1")
        elif "door_2" in rooms[index] and pug.colliderect(door2) and keyboard.e:
            door_use("door_2")
        elif "door_3" in rooms[index] and pug.colliderect(door3) and keyboard.e:
            door_use("door_3")
        elif pug.colliderect(dominant_door) and keyboard.e and rooms[index]["type"] == 1:
            dominant_door_use()
            generic()
        elif pug.colliderect(trophy) and keyboard.e and rooms[index]["type"] == 0:
            trophey_use()
        if what_room == 1 and mode == "game":
            mushroom_colliderct()
        elif what_room == 2 and mode == "game":
            if "fish" in rooms[index]:
                fish_eat()
                
#Control functions
def on_mouse_down(button, pos):
    global mode, lvl, count_levels, index, collection_mode, speed, jump, reward, index_skin, count, skin_now, index_trophy, reward_show, old_count, persec, i, speed_water
    if mouse.LEFT:
        if mode == "menu":
            if playbut.collidepoint(pos):
                but_menu_use()
                playbut_use()
                generic()
            elif collectinbut.collidepoint(pos):
                mode = 'col'
                buttonsound.stop()
                buttonsound.play()
            elif continuebut.collidepoint(pos) and len(rooms) > 0:
                but_menu_use()
            elif musicreg.collidepoint(pos):
                music_use()
        elif mode == "game":
            if cross.collidepoint(pos):
                croos_use()
            elif musicreg.collidepoint(pos):
                music_use()
        elif mode == "col":
            if cross.collidepoint(pos):
                mode = 'menu'
            elif shopflayer.collidepoint(pos):
                collection_flayer_use("shop")
            elif collectionflayer.collidepoint(pos):
                collection_flayer_use("collection")
            if collection_mode == "shop":
                if skin.collidepoint(pos):
                    skin.y -= 20
                    animate(skin, tween='bounce_end', duration=0.5, y=300)
                    skin_buy()
                elif left.collidepoint(pos) and index_skin != 0:
                    arrow_use(left)
                elif right.collidepoint(pos) and index_skin != len(skins_collection) - 1:
                    arrow_use(right)
            elif collection_mode == "collection":
                if len(trophey_collection) > 0:
                    if left.collidepoint(pos) and index_trophy != 0:
                        arrow_use(left)
                    elif right.collidepoint(pos) and index_trophy != len(trophey_collection) - 1:
                        arrow_use(right)                   
        elif mode == "end":
            if cross.collidepoint(pos):
                croos_use()

pgzrun.go()