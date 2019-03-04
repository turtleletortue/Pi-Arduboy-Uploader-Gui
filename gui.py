import os
import tkinter
from time import *
continuevar = 1
downloadup = 0
downloaddat = 0
readdirectory = 0
screen = tkinter.Tk()
if os.path.isfile('./gindex.sh') == False:
	os.system("curl -o gindex.sh https://raw.githubusercontent.com/turtleletortue/Pi-Arduboy-Uploader-Gui/master/gindex.sh")
if os.path.isfile('./README.md') == False:
	os.system("curl -o README.md https://raw.githubusercontent.com/turtleletortue/Pi-Arduboy-Uploader-Gui/master/README.md")
if os.path.isfile('./version.txt') == False:
	os.system("curl -o version.txt https://raw.githubusercontent.com/turtleletortue/Pi-Arduboy-Uploader-Gui/master/version.txt")
if os.path.isdir('./gindex') == False:
	os.system("mkdir gindex")
if os.path.isfile('./games.txt') == True:
	os.remove("games.txt")
if os.path.isdir('./ArduboyCollection') == False:
	os.system("git clone https://github.com/eried/ArduboyCollection.git")
	downloaddat = 1
if os.path.isfile('./games.txt') == False:
	gaems = open("games.txt", "a")
	if os.path.isfile("./gindex/action.txt") == True:
		os.remove("./gindex/action.txt")
		os.remove("./gindex/application.txt")
		os.remove("./gindex/arcade.txt")
		os.remove("./gindex/demo.txt")
		os.remove("./gindex/misc.txt")
		os.remove("./gindex/platformer.txt")
		os.remove("./gindex/puzzle.txt")
		os.remove("./gindex/racing.txt")
		os.remove("./gindex/rpg.txt")
		os.remove("./gindex/shooter.txt")
		os.remove("./gindex/sports.txt")
	os.system("sh gindex.sh")
	act = open("gindex/action.txt", "r")
	for x in act.readlines():
		gaems.write("act: " + x)
	act.close()
	app = open("gindex/application.txt", "r")
	for x in app.readlines():
		gaems.write("app: " + x)
	app.close()
	arc = open("gindex/arcade.txt", "r")
	for x in arc.readlines():
		gaems.write("arc: " + x)
	arc.close()
	dem = open("gindex/demo.txt", "r")
	for x in dem.readlines():
		gaems.write("dem: " + x)
	dem.close()
	mis = open("gindex/misc.txt", "r")
	for x in mis.readlines():
		gaems.write("mis: " + x)
	mis.close()
	pla = open("gindex/platformer.txt", "r")
	for x in pla.readlines():
		gaems.write("pla: " + x)
	pla.close()
	puz = open("gindex/puzzle.txt", "r")
	for x in puz.readlines():
		gaems.write("puz: " + x)
	puz.close()
	rac = open("gindex/racing.txt", "r")
	for x in rac.readlines():
		gaems.write("rac: " + x)
	rac.close()
	rpg = open("gindex/rpg.txt", "r")
	for x in rpg.readlines():
		gaems.write("rpg:" + x)
	rpg.close()
	sho = open("gindex/shooter.txt", "r")
	for x in sho.readlines():
		gaems.write("sho: " + x)
	sho.close()
	spo = open("gindex/sports.txt", "r")
	for x in spo.readlines():
		gaems.write("spo: " + x)
	spo.close()
	gaems.close()
if os.path.isfile('./uploader.py') == False:
	os.system("curl -o uploader.py https://raw.githubusercontent.com/MrBlinky/Arduboy-Python-Utilities/master/uploader.py")
	downloadup = 1
box = tkinter.Listbox(screen)
gaems = open("games.txt", "r")
fg = 1
def upload(event):
	widget = event.widget
	selection = widget.curselection()
	value = widget.get(selection[0])
	if (value[0:3]) == "act":
		fold = "Action"
	if (value[0:3]) == "app":
		fold = "Application"
	if (value[0:3]) == "arc":
		fold = "Arcade"
	if (value[0:3]) == "dem":
		fold = "Demo"
	if (value[0:3]) == "mis":
		fold = "Misc"
	if (value[0:3]) == "pla":
		fold = "Platformer"
	if (value[0:3]) == "puz":
		fold = "Puzzle"
	if (value[0:3]) == "rac":
		fold = "Racing"
	if (value[0:3]) == "rpg":
		fold = "RPG"
	if (value[0:3]) == "sho":
		fold = "Shooter"
	if (value[0:3]) == "spo":
		fold = "Sports"
	h = value[:-1]
	h = h[5:]
	comman = 'python3 uploader.py ' + '"ArduboyCollection/'+ fold + "/" + h + "/" + h + '.hex' + '"'
	print (comman)
	screen.quit()
	continuevar = 0
	os.system(comman)
for i in gaems.readlines():
	box.insert(fg, i)
box.bind("<Double-Button-1>", upload)
box.pack()
while continuevar == 1:	
	screen.update()

