import pgzero
import pgzrun
import random
#Variables
TITLE = "The pug's saga"
WIDTH = 1000
HEIGHT = 590
FPS = 120
mode = 'menu'
#names
index = 0
count_levels = 10
lvl = 1
#spisok
variable_rooms = [{"max_doors": 1, "room": "room"},{"max_doors": 3, "room": "room"}]
rooms = []

#funktions
def door_draw():
    if int(rooms[index]["amount_door"]) == 1:
        door1.draw()
        screen.draw.text(str(rooms[index]["door_1"]), center=(250, 367), color = 'black', fontsize = 38)
    elif int(rooms[index]["amount_door"]) == 2:
        door1.draw()
        screen.draw.text(str(rooms[index]["door_1"]), center=(250, 367), color = 'black', fontsize = 38)
        door2.draw()
        screen.draw.text(str(rooms[index]["door_2"]), center=(500, 367), color = 'black', fontsize = 38)
    elif int(rooms[index]["amount_door"]) == 3:
        door1.draw()
        screen.draw.text(str(rooms[index]["door_1"]), center=(250, 367), color = 'black', fontsize = 38)
        door2.draw()
        screen.draw.text(str(rooms[index]["door_2"]), center=(500, 367), color = 'black', fontsize = 38)
        door3.draw()
        screen.draw.text(str(rooms[index]["door_3"]), center=(750, 367), color = 'black', fontsize = 38)
    if rooms[index]["type"] == 0:
        dominant_door.draw()
    

def generic():
    global rooms
    pug.pos = (150,457)
    rooms = [{"type": 1, "amount_door": 0, "index": 0}]
    for i in range(count_levels):
        now = i + 1
        how = random.randint(0, len(rooms) - 1)
        while len(rooms[how].keys()) -3 >= variable_rooms[rooms[how]["type"]]["max_doors"]:
            how = random.randint(0, len(rooms) - 1)
        if now == count_levels:
            rooms.append({"type": 0, "amount_door": 0, "index": now })
        else:
            rooms.append({"type": random.randint(1, len(variable_rooms) -1), "amount_door": 0, "index": now })
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
#Actors
menu = Actor('menufon')
room = Actor("room")
door1 = Actor('door1', (250, 410))
door2 = Actor('door1', (500, 410))
door3 = Actor('door1', (750, 410))
dominant_door = Actor('dominantdoor', (500, 410))
playbut = Actor('playbut', (500, 150))
collectinbut = Actor('collectionbut', (500, 300))
colfon = Actor('colfon')
cross = Actor('cross', (985, 15))
pug = Actor('pugr',(150, 457))
#Draw
def draw():
    if mode == 'menu':
        menu.draw()
        playbut.draw()
        collectinbut.draw()
    elif mode == 'game':
        room.draw()
        door_draw()
        pug.draw()
    elif mode == 'col':
        colfon.draw()
        cross.draw()
#Update
def update(dt):
    global mode, index
    if mode == "game":
        #gravitation
        if pug.y < 457:
            pug.y += 10
        #Keyboard controls
        if (keyboard.space or keyboard.w or keyboard.up) and pug.y == 457:
            animate(pug, tween = 'decelerate', duration = 0.2, y = 367)
        if (keyboard.right or keyboard.d) and pug.x < 1000: 
            pug.image = 'pugr'
            pug.x += 5
        elif (keyboard.left or keyboard.a) and pug.x > 0: 
            pug.image = 'pugl'
            pug.x -= 5
    
    
#doors_open
def on_key_down(key):
    global index, lvl, count_levels
    if mode == 'game':
        if "door_1" in rooms[index] and pug.colliderect(door1) and keyboard.e:
            pug.pos = (250, 457)
            room.image = variable_rooms[rooms[index]["type"]]["room"]
            index = rooms[index]["door_1"]
        elif "door_2" in rooms[index] and pug.colliderect(door2) and keyboard.e:
            pug.pos = (250, 457)
            room.image = variable_rooms[rooms[index]["type"]]["room"]
            index = rooms[index]["door_2"]
        elif "door_3" in rooms[index] and pug.colliderect(door3) and keyboard.e:
            pug.pos = (250, 457)
            room.image = variable_rooms[rooms[index]["type"]]["room"]
            index = rooms[index]["door_3"]
        elif pug.colliderect(dominant_door) and keyboard.e and rooms[index]["type"] == 0:
            count_levels += 10
            lvl += 1
            index = 0
            generic() 
#Control functions
def on_mouse_down(button,pos):
    global mode, lvl
    if mouse.LEFT:
        if playbut.collidepoint(pos) and mode == 'menu':
            playbut.y += 5
            animate(playbut, tween='bounce_end', duration=0.5, y=150)
            mode = 'game'
            lvl = 1 
            generic()
        elif collectinbut.collidepoint(pos) and mode == 'menu':
            collectinbut.y += 5
            animate(collectinbut, tween='bounce_end', duration=0.5, y=300)
            mode = 'col'
        elif cross.collidepoint(pos) and mode == 'col':
            cross.y += 5
            animate(cross, tween='bounce_end', duration=0.5, y=15)
            mode = 'menu'
            
pgzrun.go()