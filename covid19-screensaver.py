# Version 0.1
import pyglet
import random
import numpy as np
from pyglet.gl import *
import math

screen_width  = 640 #4240
screen_height = 480 #1050

pops = [False, True]
ratio = screen_height/screen_width

spawn_num = 24 # number of objects to spawn
spawns = [] # spawned objects
endscreen = False
flap = (0,0,0,0,1,1,1,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,22,23,23,23,24,24,24,24)
#spin = (0,1,2,3,4,5,6,7,8,9,10,10,11,12,12,12,13,13,13,13,14,14,14,14,15,15,15,16,16,17,18,19,20,21,22,23,24)
spin = (0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24)

flapspeed = 2
spinspeed = 2
flaps = []
spins = []

rot = 0

def nflaps(flap):
	global flapspeed
	for i in flap:
		for g in range(flapspeed):
			flaps.append(i)

def nspins(spin):
	global spinspeed
	for o in spin:
		for b in range(spinspeed):
			spins.append(o)

nflaps(flap)
nspins(spin)
flaplen = len(flaps)
spinlen = len(spins)
flapcount = 0
spincount = 0

def init_virus(screen_width, screen_height):
	#otype  = random.choices([0,1], weights=[3,20])
	otype  = 1 #random.choice([1,1])
	pos = np.array([random.random()*screen_width, random.random()*screen_height])
	vecdir = np.array([-2, -1])
	vel   = 0.5+random.random() # velocity
	spawn = [otype, pos, vecdir*vel]
	spawns.append(spawn)

def spawn_virus(screen_width, screen_height):
	otype  = random.choices([0,1,2], weights=[5,56,2])
	otype = otype[0]
	diceroll = random.choices(pops, weights=[screen_width, screen_height])
	if diceroll[0] == False:
		pos = np.array([random.random()*(screen_width), screen_height])
	if diceroll[0] == True:
		pos = np.array([screen_width, random.random()*screen_height])

	vecdir = np.array([-2, -1])# direction vector
	vel   = 0.5+random.random()*1.5 # velocity
	spawn = [otype, pos, vecdir*vel]
	spawns.append(spawn)

window = pyglet.window.Window(screen_width, screen_height) #4240x1050
x, y = window.get_location()
window.set_location(x - 1, y - 1)
#window.set_location(1280 - 1, y - 1)
virus = pyglet.image.load('sprites/virus.png')
virus_anim = pyglet.image.ImageGrid(virus, 1, 25)

skull = pyglet.image.load('sprites/cranium.png')
skull_anim = pyglet.image.ImageGrid(skull, 1, 25)

syringe = pyglet.image.load('sprites/syringes.png')
syringe_anim = pyglet.image.ImageGrid(syringe, 1, 25)

glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

for i in range(spawn_num):
	init_virus(screen_width, screen_height)

def update(dt):
	global spawns
	global endscreen
	global rot
	index = 0

	if endscreen == True:
		missing = spawn_num - len(spawns)
		if missing > 1:
			for u in range(missing):
				spawn_virus(screen_width, screen_height)
		else:
			spawn_virus(screen_width, screen_height)
		endscreen = False
	
	for i in spawns:
		i[1] = (i[1]) + i[2]
		i[1][1] = i[1][1] + (math.sin(rot)*1.5)

		if rot >= (2*math.pi):
			rot = 0

		if i[1][1] < -128 or i[1][0] < -128:
			endscreen = True
			del spawns[index]
		index += 1
	rot += 0.005
			
@window.event
def on_draw():
	global spawns
	global endscreen
	global flapcount
	global spincount
	window.clear()

	for p in spawns:
		if p[0] == 0:
			skull_anim[spins[spincount]].blit(round(p[1][0]), round(p[1][1]))
		if p[0] == 1:
			virus_anim[flaps[flapcount]].blit(round(p[1][0]), round(p[1][1]))
		if p[0] == 2:
			syringe_anim[spins[spincount]].blit(round(p[1][0]), round(p[1][1]))
			
	flapcount += 1
	if flapcount >= flaplen:
		flapcount = 0

	spincount += 1
	if spincount >= spinlen:
		spincount = 0

pyglet.clock.schedule_interval(update, 0.01)
pyglet.app.run()
