import pygame, math, random
display = pygame.display.set_mode((800, 600))
f = open("wordlist.10000", "r")
words = f.read().split("\n")
class one_friend():
    def __init__(self, sprite, x=0):
        self.sprite = sprite
        self.start_y = 500 - self.sprite.get_size()[1]
        self.x, self.y = x, self.start_y
        self.last_increment = 0
        self.stage = 0
        self.magnitude = random.randint(20, 400)
        self.granularity = 1000/self.magnitude
        self.speed = random.randint(5, 10)
        self.direction = random.choice([self.speed, -self.speed])
        self.boundaries = [0, 600-self.sprite.get_size()[0]]
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_size()[0], self.sprite.get_size()[1])
    def update(self):
        if (self.direction >= 0 and self.x >= self.boundaries[1]) or (self.direction < 0 and self.x <= self.boundaries[0]): self.direction = -self.direction
        self.x += self.direction
        x = math.sin(math.radians(self.stage))
        self.y += (self.last_increment - x) * self.magnitude
        self.last_increment = x
        self.stage += self.granularity
        if self.stage >= 180:
            self.last_increment = 0
            self.stage = 0
            self.magnitude = random.randint(20, 400)
            self.granularity = 1000/self.magnitude
            self.y = self.start_y
        self.rect[0] = self.x
        self.rect[1] = self.y
class friends():
    def __init__(self, font):
        self.friends = []
        self.font = font
        self.tetotext = self.font.render(str(5), 0, [0, 0, 0])
    def add_member(self, member): self.friends.append(member)
    def update_friends(self, menu, fruits):
        v = self.lifeordeathforpearteto(menu, fruits)
        for friends in self.friends: friends.update()
        return v
    def show(self, display):
        for friends in self.friends: display.blit(friends.sprite, (friends.x, friends.y))
    def lifeordeathforpearteto(self, menu, new_fruits):
        for friend in self.friends:
            for burger in menu.menu:
                if friend.rect.colliderect(burger.rect):
                    if burger.good:
                        self.friends.append(one_friend(random.choice(new_fruits), x=random.randint(0, 500)))
                        menu.menu.remove(burger)
                        return "WAHOO"
                    else:
                        self.friends.remove(friend)
                        menu.menu.remove(burger)
                        return "ARGH"
class grounds():
    def __init__(self):
        self.x, self.y = -400, 0
        self.sprite = pygame.transform.scale(pygame.image.load("ground.png").convert(), (800, 100))
    def update(self, surface):
        surface.blit(self.sprite, (self.x, 500))
        surface.blit(self.sprite, (self.x+800, 500))
        self.x -= 15
        if self.x <= -800:
            self.x += 800
class bunger():
    def __init__(self, good):
        self.good = good
        if self.good: self.sprite = rescale(image_load("diet.png"), 0.2)
        else: self.sprite = rescale(image_load("demon.png"), 0.275)
        self.x, self.y = 1000, 500-self.sprite.get_size()[1]
        self.rect = pygame.Rect(self.x, self.y, self.sprite.get_size()[0], self.sprite.get_size()[1])
    def update(self):
        self.x -= 15
        self.rect[0] -= 15
        if self.x <= -200: return True
        return False
class burger_menu():
    def __init__(self):
        self.menu = []
    def add_burger(self, burger):
        for bulger in self.menu:
            if bulger.x >= 950:         #   SPAWN RATE KIND OF
                return False
        self.menu.append(burger)
    def update_burgers(self):
        for burger in self.menu:
            if burger.update(): self.menu.remove(burger)
    def show(self, display):
        for burger in self.menu: display.blit(burger.sprite, (burger.x, burger.y))
    def click_burger(self, point, friends):
        for burger in self.menu:
            if burger.rect.collidepoint(point):
                self.menu.remove(burger)
                if burger.good:
                    del friends.friends[random.randint(0, len(friends.friends)-1)]
                    return "UR STUPID"
                return False
class screamersss():
    def __init__(self):
        self.screamers = []
    def add_creamer(self, screamer):
        self.screamers.append(screamer)
    def update_screamers(self):
        for scream in self.screamers:
            if scream.update(): self.screamers.remove(scream)
    def show(self):
        for scream in self.screamers: display.blit(scream.sprite, (0, 0))
class screamer():
    def __init__(self, sprite, sfx):
        self.sprite = sprite
        self.alpha = 255+15
    def update(self):
        self.alpha -= 15
        self.sprite.set_alpha(self.alpha)
        if self.alpha <= 0:
            return True
        return False
#import AND rescale people
def rescale(sprite, scaleX, scaleY=0):
    x = sprite.get_size()
    if scaleY == 0: scaleY = scaleX
    return pygame.transform.scale(sprite, (x[0]*scaleX, x[1]*scaleY))
#this exists only to have 2.png as fallback
def image_load(file):
    try:    x = pygame.image.load(file)
    except: x = pygame.image.load("2.png")
    return x
def spawn_buger(menu):
    menu.add_burger(bunger(random.choice([True, False, False, False, False])))
pygame.init()
class word():
    def __init__(self, text, rgb, font):
        self.x = 800
        self.sprite = font.render(text, 0, rgb)
    def update(self):
        self.x -= 5
class dictionary():
    def __init__(self):
        self.members = []
    def addmember(self, item):
        self.members.append(item)
    def updateshow(self, surface):
        for member in self.members:
            member.update()
            if member.x <= -800: self.members.remove(member)
            surface.blit(member.sprite, (member.x, 480))
tondella = pygame.font.Font("Tondella.otf", size=80)
tondella2 = pygame.font.Font("Tondella.otf", size=120)
friendlies = friends(tondella)
ground = grounds()
menu = burger_menu()
cream = screamersss()
idkwhattocallthisclass = dictionary()
background = pygame.transform.scale(image_load("sky.png").convert(), (800, 600))
deathpillar = rescale(image_load("kill.png").convert_alpha(), (0.81))
screamer1 = image_load("screamer1.png").convert()
screamer2 = image_load("screamer2.png").convert()
screamer3 = image_load("screamer3.png").convert()
myfamily = [screamer1, screamer2, screamer3]
happy = image_load("happy.png").convert()
happoy = image_load("happoy.png").convert()
joy = image_load("rainbow.png").convert()
punjabi = image_load("punjabi.png").convert()
funworld = [happy, happoy, joy, punjabi]
dolpher = image_load("dolphin.png").convert()
aquarium = [dolpher]
pygame.mixer.init()
pygame.mixer.music.load("ust.mp3")
pygame.mixer.music.set_volume(0.25)
pygame.mixer.music.play()
screameraudio = pygame.mixer.Sound("kill.mp3")
screameraudio.set_volume(0.1)
apple = rescale(image_load("apple.png").convert_alpha(), 0.4)
grape = rescale(image_load("grape.png").convert_alpha(), 0.25)
mushroom = rescale(image_load("mushroom.png").convert_alpha(), 0.35)
pear = rescale(image_load("pear.png").convert_alpha(), 0.25)
pickle = rescale(image_load("pickle.png").convert_alpha(), 0.30)
pineapple = rescale(image_load("pineapple.png").convert_alpha(), 0.30)
fruits = [apple, grape, mushroom, pear, pickle, pineapple]
for tastyfruit in fruits: friendlies.add_member(one_friend(tastyfruit, x=random.randint(0, 500)))
stupid = str(random.randint(0, 99999))
clock = pygame.time.Clock()
mousetoggle = False
rgb = [255, 0, 0]
component = 1
inc = True
def rgbcycle(rgb, component, inc):
    if inc and rgb[component] == 255:
           inc = False
    elif not inc and rgb[component-1] == 0:
        inc = True
        component += 1
        component %= 3
    if inc:
        rgb[component] += 20
        if rgb[component] > 255: rgb[component] = 255
    else:
        rgb[component-1] -= 20
        if rgb[component-1] < 0: rgb[component-1] = 0
    return rgb, component, inc
framecounter = 0
while True:
    globby = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    v = pygame.mouse.get_pressed()[0]
    if v and not mousetoggle:
        mousetoggle = True
        globby = menu.click_burger(pygame.mouse.get_pos(), friendlies)
    if not v and mousetoggle: mousetoggle = False
    #clear the screen yes
    display.blit(background, (0, 0))
    ground.update(display)
    #put the guys down
    if not(random.randint(0, 10)):
        stupid = (str(random.randint(0, 99999)))
        spawn_buger(menu)
    lobster = friendlies.update_friends(menu, fruits)
    if lobster == "ARGH":
        friendlies.tetotext = friendlies.font.render(str(len(friendlies.friends)), 0, [0, 0, 0])
        cream.add_creamer(screamer(random.choice(myfamily), 0))
        screameraudio.play()
    elif lobster == "WAHOO":
        friendlies.tetotext = friendlies.font.render(str(len(friendlies.friends)), 0, [0, 0, 0])
        cream.add_creamer(screamer(random.choice(funworld), 0))
    elif globby == "UR STUPID":
        friendlies.tetotext = friendlies.font.render(str(len(friendlies.friends)), 0, [0, 0, 0])
        cream.add_creamer(screamer(random.choice(aquarium), 0))
    friendlies.show(display)
    menu.update_burgers()
    menu.show(display)
    if not framecounter:
        idkwhattocallthisclass.addmember(word(random.choice(words), [255, 255, 255], tondella2))
    idkwhattocallthisclass.updateshow(display)
    framecounter += 1
    framecounter %= 75
    rgb, component, inc = rgbcycle(rgb, component, inc)
    display.blit(deathpillar, (600, -40))
    display.blit(friendlies.tetotext, (650, 0))
    display.blit(pygame.transform.rotate(tondella.render(str(stupid), 0, rgb), 80), (630, 100))
    cream.update_screamers()
    cream.show()
    #updateado
    pygame.display.flip()
    clock.tick(30)
