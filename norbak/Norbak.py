import curses
import time
import random
#import playsound

#from playsound import playsound
from random import randint
from curses import wrapper
from curses import textpad
from curses.textpad import Textbox

## Initialize curses and window
stdscr = curses.initscr()
curses.start_color()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
curses.curs_set(0)
stdscr.resize(24, 80)

## Initialize color pairs
curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)

## For menu().
selection = 0

earmor = 0
earmorname = "None"
eweapon = 0
eweaponname = "None"

def playerinit():
    ## Player data defaults.
    ## XP points
    global pxp
    pxp = 200
    ## Armor level and name
    global parmor
    global parmorname
    parmor = 0
    parmorname = "None"
    ## Weapon level and name
    global pweapon
    global pweaponname
    pweapon = 1
    pweaponname = "Stick"
    ## Total damage dealable
    global pdmg
    pdmg = pweapon + pxp // 100
    ## Total health
    global phealth
    phealth = 0 + pxp // 10
    ## Playername variable declaration
    global pname
    pname = 0

def main(stdscr):
    playerinit()
    #viewmap()
    intro()
    mainmenu()
    viewmap()

## The intro "cinematic".
def intro():
    #playsound("./sounds/intro.wav", False)
    num0 = 10
    title1 = "A LucasH-DiskKun Production"
    title2 = "In Association With Tember.ca"
    title3 = "THE FIRES OF NORBAK"
    box()
    for i in range(5):
        stdscr.bkgd(curses.ACS_S1)
        stdscr.refresh()
        time.sleep(0.05)
        stdscr.bkgd(curses.ACS_S1)
        stdscr.refresh()
        time.sleep(0.05)
        stdscr.bkgd(curses.ACS_S7)
        stdscr.refresh()
        time.sleep(0.05)
        stdscr.bkgd(curses.ACS_S9)
        stdscr.refresh()
        time.sleep(0.05)
    stdscr.bkgd(" ")
    for i in range(len(title1)):
        time.sleep(0.05)
        stdscr.addch(10, 38-(len(title1)//2)+i, title1[i], curses.color_pair(1))
        stdscr.refresh()
    time.sleep(1)
    for i in range(len(title1)):
        time.sleep(0.05)
        stdscr.addch(10, 38-(len(title1)//2)+i, " ")
        stdscr.refresh()
    for i in range(len(title2)):
        time.sleep(0.05)
        stdscr.addch(10, 38-(len(title2)//2)+i, title2[i], curses.color_pair(1))
        stdscr.refresh()
    time.sleep(1)
    for i in range(len(title2)):
        time.sleep(0.05)
        stdscr.addch(10, 38-(len(title2)//2)+i, " ")
        stdscr.refresh()
    for i in range(len(title3)):
        time.sleep(0.10)
        stdscr.addch(10, 38-(len(title3)//2)+i, title3[i], curses.color_pair(2) | curses.A_BOLD)
        stdscr.refresh()
    for i in range(8):
        box()
        time.sleep(0.5)
        stdscr.addstr(num0 - i, 38-(len(title3)//2), title3, curses.color_pair(2) | curses.A_BOLD)
        stdscr.refresh()

def mainmenu():
    pxp = 200
    parmor = 0
    pdmg = 0 + pxp // 100
    phealth = 0 + pxp // 10
    pweapon = 1
    pname = 0
    global selection
    box()
    menu("THE FIRES OF NORBAK", curses.color_pair(2) | curses.A_BOLD, "PLAY", "QUIT")
    if selection == 1:
        ureg()
    else:
        end()

def ureg():
    box()
    stdscr.addstr(3, 38-len("Welcome, traveller. Enter your name below.")//2, "Welcome, traveller. Enter your name below.", curses.A_BOLD)
    curses.textpad.rectangle(stdscr, 5, 32, 7, 43)
    #stdscr.addstr(7, 32, "____________", curses.A_BOLD)
    curses.echo()
    pname = stdscr.getstr(6, 33, 10)
    pname = pname.decode('utf-8')
    if pname == "":
        ureg()
    #playsound("./confirm.wav", False)
    curses.noecho()
    curses.curs_set(0)
    box()
    typetext(3, "\"Could it be? The prophecy fulfilled?", curses.A_BOLD)
    typetext(5, "Our land has fallen under a dark depression.", curses.A_BOLD)
    typetext(7, "A powerful mage has put all of the animals under a spell.", curses.A_BOLD)
    typetext(9, "They serve the mage and attack anybody who comes near him.", curses.A_BOLD)
    typetext(11, "We are in desperate need of a warrior to defeat the mage.", curses.A_BOLD)
    typetext(13, f"The prophecy states that a powerful warrior with the name {pname}", curses.A_BOLD)
    typetext(14, "will come to save our lives and land!\"", curses.A_BOLD)
    typetext(16, f"Oh, {pname}, tell us you are the powerful warrior we've been waiting on!", curses.A_BOLD | curses.color_pair(1))
    for i in range(12):
        box()
        stdscr.addstr(14-i, 38-(len(f"Oh, {pname}, tell us you are the powerful warrior we've been waiting on!")//2), f"Oh, {pname}, tell us you are the powerful warrior we've been waiting on!", curses.A_BOLD | curses.color_pair(1))
        time.sleep(0.10)
        stdscr.refresh()
    menu(f"Oh, {pname}, tell us you are the powerful warrior we've been waiting on!", curses.A_BOLD | curses.color_pair(1), "Yes, I am.", "No, I am not.")
    if selection == 1:
        start()
    elif selection == 2:
        box()
        typetext(3, "Oh, only the gods above can save us now!", curses.A_BOLD)
        gameover()

def start():
    box()
    typetext(3, "Thank the heavens!", curses.A_BOLD)
    typetext(5, "Here, take this map, it will guide you along your journey...", curses.A_BOLD)
    typetext(7, "To the Fires of Norbak!", curses.A_BOLD | curses.color_pair(2))
    stdscr.getch()
    #viewmap()

def viewmap():
    box()
    menu("Map", curses.color_pair(1) | curses.A_BOLD, "The Fungal Forests", "The Vermin Caves", "The Evil Town", "The Dragon's Lair", "Goblin Mountain")
    if selection == 1:
        loc("The Fungal Forests", 2)
    elif selection == 2:
        loc("The Vermin Caves", 4)
    elif selection == 3:
        loc("The Evil Town", 6)
    elif selection == 4:
        loc("The Dragon's Lair", 8)
    elif selection == 5:
        loc("Goblin Mountain", 10)

def loc(location, difficulty):
    menu(f"{location}", curses.color_pair(3) | curses.A_BOLD, "Look for something to kill", "View map")
    if selection == 1:
        combat(location, difficulty)
    elif selection == 2:
        viewmap()

def combat(location, difficulty):
    def loot():
        global earmor
        global earmorname
        global eweapon
        global eweaponname
        loot = randint(1, 4)
        if loot == 1:
            armorloot = randint(1, 5)
            if armorloot == 1:
                earmor = 1
                earmorname = "Cloth Rags"
            elif armorloot == 2:
                earmor = 2
                earmorname = "Hardened Leather"
            elif armorloot == 3:
                earmor = 3
                earmorname = "Chain Mail"
            elif armorloot == 4:
                earmor = 4
                armorname = "Metal Armor"
            elif armorloot == 5:
                earmor = 5
                earmorname = "Hardened Metal Armor"
        elif loot == 2:
            weaponloot = randint(1, 5)
            if weaponloot == 1:
                eweapon = 1
                eweaponname = "Toy Sword"
            elif weaponloot == 2:
                eweapon = 2
                eweaponname = "Small Dagger"
            elif weaponloot == 3:
                eweapon = 3
                eweaponname = "Staff"
            elif weaponloot == 4:
                eweapon = 4
                eweaponname = "Short Sword"
            elif weaponloot == 5:
                eweapon = 5
                eweaponname = "Long Sword"
    def displayhealth():
        stdscr.addstr(21, 2, f"{pname}'s health: {phealth}.", curses.color_pair(3) | curses.A_BOLD)
        stdscr.addstr(21, 50, f"{enemyname}'s health: {enemyhealth}", curses.color_pair(2) | curses.A_BOLD)
    exit = False
    box()
    while exit == False:
        enemyid = randint(1, difficulty)
        if enemyid == 1:
            enemyname = "Fungus"
            enemydmg = 2
            enemyhealth = 3
        elif enemyid == 2:
            enemyname = "Snail"
            enemydmg = 4
            enemyhealth = 5
        elif enemyid == 3:
            enemyname = "Insect"
            enemydmg = 6
            enemyhealth = 7
        elif enemyid == 4:
            enemyname = "Rat"
            enemydmg = 8
            enemyhealth = 9
        elif enemyid == 5:
            enemyname = "Small Child"
            enemydmg = 10
            enemyhealth = 11
            loot()
        elif enemyid == 6:
            enemyname = "Old Woman"
            enemydmg = 12
            enemyhealth = 13
            loot()
        elif enemyid == 7:
            enemyname = "Baby Dragon"
            enemydmg = 14
            enemyhealth = 15
        elif enemyid == 8:
            enemyname = "Father Dragon"
            enemydmg = 16
            enemyhealth = 17
        elif enemyid == 9:
            enemyname = "Goblin"
            enemydmg = 18
            enemyhealth = 19
            loot()
        elif enemyid == 10:
            enemyname = "Goblin King"
            enemydmg = 20
            enemyhealth = 21
            loot()
        stdscr.addstr(3, 38-len(f"You are entering combat with a {enemyname}!")//2, f"You are entering combat with a {enemyname}!", curses.A_BOLD | curses.color_pair(2))
        stdscr.getch()
        while True:
            menu(f"{enemyname}", curses.color_pair(2) | curses.A_BOLD, "ATTACK", "DEFEND", "RUN", "STATS")
            if selection == 1:
                # Your attack
                box()
                displayhealth()
                stdscr.refresh()
                time.sleep(1)
                stdscr.addstr(3, 38-len(f"Attacking the {enemyname}!")//2, f"Attacking the {enemyname}!", curses.color_pair(2) | curses.A_BOLD)
                stdscr.refresh()
                time.sleep(1)
                global pweapon
                pturndmg = randint(0, pdmg) - earmor
                if pturndmg < 0:
                    pturndmg = 0
                enemyhealth -= pturndmg
                box()
                displayhealth()
                if pturndmg == 0:
                    stdscr.addstr(3, 38-len(f"You missed the {enemyname}!")//2, f"You missed the {enemyname}!", curses.A_BOLD)
                else:
                    #playsound("./sounds/atk.wav", False)
                    stdscr.addstr(3, 38-len(f"You dealt {pturndmg} to the {enemyname}!")//2, f"You dealt {pturndmg} damage to the {enemyname}!", curses.color_pair(2) | curses.A_BOLD)
                stdscr.refresh()
                time.sleep(1)
                if enemyhealth <= 0:
                    box()
                    global pxp
                    pxp += enemyid*10
                    stdscr.addstr(3, 38-len(f"You killed the {enemyname}! You get {enemyid*10} experience points.")//2, f"You killed the {enemyname}! You get {enemyid*10} experience points.", curses.color_pair(3) | curses.A_BOLD)
                    stdscr.addstr(4, 38-len(f"You now have {pxp} experience points!")//2, f"You now have {pxp} experience points!", curses.color_pair(3) | curses.A_BOLD)
                    if earmor != 0:
                        stdscr.addstr(5, 38-len(f"The {enemyname} was wearing a {earmorname}!")//2, f"The {enemyname} was wearing a {earmorname}!")
                        stdscr.refresh()
                        stdscr.getch()
                        menu("Pick up the armor?", curses.color_pair(1)|curses.A_BOLD, "Yes", "No")
                        if selection == 1:
                            global parmor
                            parmor = earmor
                            global parmorname
                            parmorname = earmorname
                    elif eweapon != 0:
                        stdscr.addstr(5, 38-len(f"The {enemyname} was carrying a {eweaponname}!")//2, f"The {enemyname} was carrying a {eweaponname}!")
                        stdscr.refresh()
                        stdscr.getch()
                        menu("Pick up the weapon?", curses.color_pair(1)|curses.A_BOLD, "Yes", "No")
                        if selection == 1:
                            pweapon = eweapon
                            global pweaponname
                            pweaponname = eweaponname
                    else:
                        stdscr.refresh()
                        stdscr.getch()
                    loc(location, difficulty)
                # Enemy's attack
                box()
                displayhealth()
                stdscr.refresh()
                time.sleep(1)
                stdscr.addstr(3, 38-len(f"{enemyname} is attacking!")//2, f"{enemyname} is attacking!", curses.color_pair(2) | curses.A_BOLD)
                stdscr.refresh()
                time.sleep(1)
                eturndmg = randint(0, enemydmg) + eweapon - parmor
                if eturndmg < 0:
                    eturndmg = 0
                global phealth
                phealth -= eturndmg
                box()
                displayhealth()
                if eturndmg == 0:
                    stdscr.addstr(3, 38-len(f"The {enemyname} missed you!")//2, f"The {enemyname} missed you!", curses.color_pair(3) | curses.A_BOLD)
                else:
                    #playsound("./sounds/atk.wav", False)
                    stdscr.addstr(3, 38-len(f"The {enemyname} dealt {eturndmg} damage to you!")//2, f"The {enemyname} dealt {eturndmg} damage to you!", curses.color_pair(2) | curses.A_BOLD)
                stdscr.refresh()
                time.sleep(1)
                if phealth <= 0:
                    gameover()
            elif selection == 2:
                box()
                displayhealth()
                stdscr.addstr(3, 38-len("You spend the turn resting...")//2, "You spend the turn resting.", curses.A_BOLD)
                stdscr.refresh()
                time.sleep(1)
                recover = phealth // 4
                phealth += recover
                if phealth > pxp // 10:
                    phealth = pxp // 10
                box()
                displayhealth()
                stdscr.addstr(3, 38-len(f"You recovered {recover} health!")//2, f"You recovered {recover} health!", curses.A_BOLD | curses.color_pair(3))
                stdscr.refresh()
                time.sleep(1)
                box()
                displayhealth()
                stdscr.refresh()
                time.sleep(1)
                stdscr.addstr(3, 38-len(f"{enemyname} is attacking!")//2, f"{enemyname} is attacking!", curses.color_pair(2) | curses.A_BOLD)
                stdscr.refresh()
                time.sleep(1)
                eturndmg = randint(0, enemydmg) + eweapon - parmor
                if eturndmg < 0:
                    eturndmg = 0
                #global phealth
                phealth -= eturndmg
                box()
                displayhealth()
                if eturndmg == 0:
                    stdscr.addstr(3, 38-len(f"The {enemyname} missed you!")//2, f"The {enemyname} missed you!", curses.color_pair(3) | curses.A_BOLD)
                else:
                    #playsound("./sounds/atk.wav", False)
                    stdscr.addstr(3, 38-len(f"The {enemyname} dealt {eturndmg} damage to you!")//2, f"The {enemyname} dealt {eturndmg} damage to you!", curses.color_pair(2) | curses.A_BOLD)
                stdscr.refresh()
                time.sleep(1)
                if phealth <= 0:
                    gameover()
            elif selection == 3:
                gotaway = randint(0, 3)
                if gotaway == 2 or gotaway == 3:
                    box()
                    stdscr.addstr(3, 38-len("You got away!")//2, "You got away!", curses.A_BOLD)
                    stdscr.refresh()
                    stdscr.getch()
                    loc(location, difficulty)
                elif gotaway == 0 or 1:
                    box()
                    stdscr.addstr(3, 38-len("You didn't get away!")//2, "You didn't get away!", curses.A_BOLD)
                    stdscr.refresh()
                    stdscr.refresh()
                    eturndmg = randint(0, enemydmg) + eweapon - parmor
                    if eturndmg < 0:
                        eturndmg = 0
                    #global phealth
                    phealth -= eturndmg
                    box()
                    displayhealth()
                    if eturndmg == 0:
                        stdscr.addstr(3, 38-len(f"The {enemyname} missed you!")//2, f"The {enemyname} missed you!", curses.color_pair(3) | curses.A_BOLD)
                    else:
                        #playsound("./sounds/atk.wav", False)
                        stdscr.addstr(3, 38-len(f"The {enemyname} dealt {eturndmg} damage to you!")//2, f"The {enemyname} dealt {eturndmg} damage to you!", curses.color_pair(2) | curses.A_BOLD)
                    stdscr.refresh()
                    time.sleep(1)
            elif selection == 4:
                box()
                stdscr.addstr(3, 5, "Enemy:", curses.color_pair(2)|curses.A_BOLD)
                stdscr.addstr(4, 5, f"Health: {enemyhealth}", curses.color_pair(2)|curses.A_BOLD)
                stdscr.addstr(5, 5, f"Weapon: {eweaponname}", curses.color_pair(2)|curses.A_BOLD)
                stdscr.addstr(6, 5, f"Armor: {earmorname}", curses.color_pair(2)|curses.A_BOLD)
                stdscr.addstr(7, 5, f"Damage: {enemydmg}", curses.color_pair(2)|curses.A_BOLD)
                stdscr.addstr(3, 50, "You:", curses.color_pair(3)|curses.A_BOLD)
                stdscr.addstr(4, 50, f"Health: {phealth}", curses.color_pair(3)|curses.A_BOLD)
                stdscr.addstr(5, 50, f"Weapon: {pweaponname}", curses.color_pair(3)|curses.A_BOLD)
                stdscr.addstr(6, 50, f"Armor: {parmorname}", curses.color_pair(3)|curses.A_BOLD)
                stdscr.addstr(7, 50, f"Damage: {pdmg}", curses.color_pair(3)|curses.A_BOLD)
                stdscr.addstr(8, 50, f"Experience: {pxp}", curses.color_pair(3)|curses.A_BOLD)
                #stdscr.addstr(5, 38-len(f"{pname}: {phealth} health, can deal {pdmg} damage.")//2, f"{pname}: {phealth} health, can deal {pdmg} damage.", curses.color_pair(3)|curses.A_BOLD)
                stdscr.refresh()
                stdscr.getch()

def menu(title, titleattr, option1, option2, option3="", option4="", option5="", option6=""):
    global selection
    selection = 1
    attr1 = curses.A_UNDERLINE
    attr2 = 0
    attr3 = 0
    attr4 = 0
    attr5 = 0
    attr6 = 0
    while True:
        if option3 == "":
            items = 2
            box()
            stdscr.addstr(3, 38-len(title)//2, title, titleattr)
            stdscr.addstr(5, 38-(len(option1)//2), option1, attr1)
            stdscr.addstr(7, 38-(len(option2)//2), option2, attr2)
        elif option3 != "" and option4 == "":
            items = 3
            box()
            stdscr.addstr(3, 38-len(title)//2, title, titleattr)
            stdscr.addstr(5, 38-(len(option1)//2), option1, attr1)
            stdscr.addstr(7, 38-(len(option2)//2), option2, attr2)
            stdscr.addstr(9, 38-(len(option3)//2), option3, attr3)
        elif option4 != "" and option5 == "":
            items = 4
            box()
            stdscr.addstr(3, 38-len(title)//2, title, titleattr)
            stdscr.addstr(5, 38-(len(option1)//2), option1, attr1)
            stdscr.addstr(7, 38-(len(option2)//2), option2, attr2)
            stdscr.addstr(9, 38-(len(option3)//2), option3, attr3)
            stdscr.addstr(11, 38-(len(option4)//2), option4, attr4)
        elif option5 != "" and option6 == "":
            items = 5
            box()
            stdscr.addstr(3, 38-len(title)//2, title, titleattr)
            stdscr.addstr(5, 38-(len(option1)//2), option1, attr1)
            stdscr.addstr(7, 38-(len(option2)//2), option2, attr2)
            stdscr.addstr(9, 38-(len(option3)//2), option3, attr3)
            stdscr.addstr(11, 38-(len(option4)//2), option4, attr4)
            stdscr.addstr(13, 38-(len(option5)//2), option5, attr5)
        elif option6 != "":
            items = 6
            box()
            stdscr.addstr(3, 38-len(title)//2, title, titleattr)
            stdscr.addstr(5, 38-(len(option1)//2), option1, attr1)
            stdscr.addstr(7, 38-(len(option2)//2), option2, attr2)
            stdscr.addstr(9, 38-(len(option3)//2), option3, attr3)
            stdscr.addstr(11, 38-(len(option4)//2), option4, attr4)
            stdscr.addstr(13, 38-(len(option5)//2), option5, attr5)
            stdscr.addstr(15, 38-(len(option6)//2), option6, attr6)
        key = stdscr.getkey()
        if key == "KEY_UP":
            if selection == 1:
                selection = 1
            else:
                selection -= 1
        elif key == "KEY_DOWN":
            if selection >= items:
                selection = items
            else:
                selection += 1
        elif key == " ":
            #playsound("./sounds/confirm.wav", False)
            return

        if selection == 1:
            attr1 = curses.A_UNDERLINE
            attr2 = 0
            attr3 = 0
            attr4 = 0
            attr5 = 0
            attr6 = 0
        elif selection == 2:
            attr2 = curses.A_UNDERLINE
            attr1 = 0
            attr3 = 0
            attr4 = 0
            attr5 = 0
            attr6 = 0
        elif selection == 3:
            attr3 = curses.A_UNDERLINE
            attr1 = 0
            attr2 = 0
            attr4 = 0
            attr5 = 0
            attr6 = 0
        elif selection == 4:
            attr4 = curses.A_UNDERLINE
            attr1 = 0
            attr2 = 0
            attr3 = 0
            attr5 = 0
            attr6 = 0
        elif selection == 5:
            attr5 = curses.A_UNDERLINE
            attr1 = 0
            attr2 = 0
            attr3 = 0
            attr4 = 0
            attr6 = 0
        elif selection == 6:
            attr6 = curses.A_UNDERLINE
            attr1 = 0
            attr2 = 0
            attr3 = 0
            attr4 = 0
            attr5 = 0

def typetext(y, text, attr):
    for i in range(len(text)):
        #playsound("./sounds/click.wav", False)
        stdscr.addch(y, 38-(len(text)//2)+i, text[i], attr)
        time.sleep(0.05)
        stdscr.refresh()
    time.sleep(0.5)

def box():
    stdscr.erase()
    stdscr.border()

def gameover():
    time.sleep(1)
    box()
    stdscr.refresh()
    time.sleep(1)
    #playsound("./sounds/death.wav", False)
    for i in range(len("GAME OVER")):
        stdscr.addch(11, 38-(len("GAME OVER")//2)+i, "GAME OVER"[i], curses.color_pair(2) | curses.A_BOLD)
        time.sleep(0.10)
        stdscr.refresh()
    stdscr.getch()
    mainmenu()

# De-init curses and window.
def end():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()
    quit()

wrapper(main)
