import curses
import time
import random
#import keyboard
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
coinloot = 0

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
    ## Player's money
    global pcoins
    pcoins = 200

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
    playerinit()
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
    typetext(3, "Could it be? The prophecy fulfilled?", curses.A_BOLD)
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
    menu("Map", curses.color_pair(1) | curses.A_BOLD, "The Fungal Forests", "The Vermin Caves", "The Evil Town", "The Dragon's Lair", "Goblin Mountain", "The Good Town (Shop)")
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
    elif selection == 6:
        town()

def town():
    global pcoins
    global pweaponname
    global pweapon
    global parmorname
    global parmor
    menu("Shop", curses.color_pair(3)|curses.A_BOLD, "Armor", "Weapons", "View Map")
    if selection == 1:
        menu("Armor Shop", curses.color_pair(3)|curses.A_BOLD, "Cloth Rags: 100", "Hardened Leather: 200", "Chain Mail: 300", "Metal Armor: 400", "Hardened Metal Armor: 500", "Back")
        if selection == 1:
            if pcoins >= 100:
                pcoins -= 100
                parmor = 1
                parmorname = "Cloth Rags"
                box()
                stdscr.addstr(3, 38-len(f"You bought a {parmorname}! You have {pcoins} coins left.")//2, f"You bought a {parmorname}! You have {pcoins} coins left.", curses.A_BOLD)
                stdscr.getch()
                town()
            else:
                box()
                stdscr.addstr(3, 38-len("You don't have enough coins!")//2, "You don't have enough coins!", curses.A_BOLD)
                stdscr.getch()
                town()
        elif selection == 2:
            if pcoins >= 200:
                pcoins -= 200
                parmor = 2
                parmorname = "Hardened Leather"
                box()
                stdscr.addstr(3, 38-len(f"You bought a {parmorname}! You have {pcoins} coins left.")//2, f"You bought a {parmorname}! You have {pcoins} coins left.", curses.A_BOLD)
                stdscr.getch()
                town()
            else:
                box()
                stdscr.addstr(3, 38-len("You don't have enough coins!")//2, "You don't have enough coins!", curses.A_BOLD)
                stdscr.getch()
                town()
        elif selection == 3:
            if pcoins >= 300:
                pcoins -= 300
                parmor = 3
                parmorname = "Chain Mail"
                box()
                stdscr.addstr(3, 38-len(f"You bought a {parmorname}! You have {pcoins} coins left.")//2, f"You bought a {parmorname}! You have {pcoins} coins left.", curses.A_BOLD)
                stdscr.getch()
                town()
            else:
                box()
                stdscr.addstr(3, 38-len("You don't have enough coins!")//2, "You don't have enough coins!", curses.A_BOLD)
                stdscr.getch()
                town()
        elif selection == 4:
            if pcoins >= 400:
                pcoins -= 400
                parmor = 4
                parmorname = "Metal Armor"
                box()
                stdscr.addstr(3, 38-len(f"You bought a {parmorname}! You have {pcoins} coins left.")//2, f"You bought a {parmorname}! You have {pcoins} coins left.", curses.A_BOLD)
                stdscr.getch()
                town()
            else:
                box()
                stdscr.addstr(3, 38-len("You don't have enough coins!")//2, "You don't have enough coins!", curses.A_BOLD)
                stdscr.getch()
                town()
        elif selection == 5:
            if pcoins >= 500:
                pcoins -= 500
                parmor = 5
                parmorname = "Hardened Metal Armor"
                box()
                stdscr.addstr(3, 38-len(f"You bought a {parmorname}! You have {pcoins} coins left.")//2, f"You bought a {parmorname}! You have {pcoins} coins left.", curses.A_BOLD)
                stdscr.getch()
                town()
            else:
                box()
                stdscr.addstr(3, 38-len("You don't have enough coins!")//2, "You don't have enough coins!", curses.A_BOLD)
                stdscr.getch()
                town()
        elif selection == 6:
            town()
    elif selection == 2:
        menu("Weapon Shop", curses.color_pair(3)|curses.A_BOLD, "Toy Sword: 100", "Small Dagger: 200", "Staff: 300", "Short Sword: 400", "Long Sword: 500", "Back")
        if selection == 1:
            if pcoins >= 100:
                pcoins -= 100
                pweapon = 1
                pweaponname = "Toy Sword"
                box()
                stdscr.addstr(3, 38-len(f"You bought a {pweaponname}! You have {pcoins} coins left.")//2, f"You bought a {pweaponname}! You have {pcoins} coins left.", curses.A_BOLD)
                stdscr.getch()
                town()
            else:
                box()
                stdscr.addstr(3, 38-len("You don't have enough coins!")//2, "You don't have enough coins!", curses.A_BOLD)
                stdscr.getch()
                town()
        elif selection == 2:
            if pcoins >= 200:
                pcoins -= 200
                pweapon = 2
                pweaponname = "Small Dagger"
                box()
                stdscr.addstr(3, 38-len(f"You bought a {pweaponname}! You have {pcoins} coins left.")//2, f"You bought a {pweaponname}! You have {pcoins} coins left.", curses.A_BOLD)
                stdscr.getch()
                town()
            else:
                box()
                stdscr.addstr(3, 38-len("You don't have enough coins!")//2, "You don't have enough coins!", curses.A_BOLD)
                stdscr.getch()
                town()
        elif selection == 3:
            if pcoins >= 300:
                pcoins -= 300
                pweapon = 3
                pweaponame = "Staff"
                box()
                stdscr.addstr(3, 38-len(f"You bought a {pweaponname}! You have {pcoins} coins left.")//2, f"You bought a {pweaponname}! You have {pcoins} coins left.", curses.A_BOLD)
                stdscr.getch()
                town()
            else:
                box()
                stdscr.addstr(3, 38-len("You don't have enough coins!")//2, "You don't have enough coins!", curses.A_BOLD)
                stdscr.getch()
                town()
        elif selection == 4:
            if pcoins >= 400:
                pcoins -= 400
                pweapon = 4
                pweaponname = "Short Sword"
                box()
                stdscr.addstr(3, 38-len(f"You bought a {pweaponname}! You have {pcoins} coins left.")//2, f"You bought a {pweaponname}! You have {pcoins} coins left.", curses.A_BOLD)
                stdscr.getch()
                town()
            else:
                box()
                stdscr.addstr(3, 38-len("You don't have enough coins!")//2, "You don't have enough coins!", curses.A_BOLD)
                stdscr.getch()
                town()
        elif selection == 5:
            if pcoins >= 500:
                pcoins -= 500
                pweapon = 5
                pweaponname = "Long Sword"
                box()
                stdscr.addstr(3, 38-len(f"You bought a {pweaponname}! You have {pcoins} coins left.")//2, f"You bought a {pweaponname}! You have {pcoins} coins left.", curses.A_BOLD)
                stdscr.getch()
                town()
            else:
                box()
                stdscr.addstr(3, 38-len("You don't have enough coins!")//2, "You don't have enough coins!", curses.A_BOLD)
                stdscr.getch()
                town()
        elif selection == 6:
            town()
    elif selection == 3:
        viewmap()

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
        global coinloot
        loot = randint(1, 3)
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
        elif loot == 3:
            coinloot = randint(1, 10) * enemyid
    def displayhealth():
        stdscr.addstr(22, 2, f"{pname}'s health: {phealth}.", curses.color_pair(3) | curses.A_BOLD)
        stdscr.addstr(22, 50, f"{enemyname}'s health: {enemyhealth}", curses.color_pair(2) | curses.A_BOLD)
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
            loot()
        elif enemyid == 8:
            enemyname = "Father Dragon"
            enemydmg = 16
            enemyhealth = 17
            loot()
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
                        stdscr.getch()
                        menu("Pick up the armor?", curses.color_pair(1)|curses.A_BOLD, "Yes", "No")
                        if selection == 1:
                            global parmor
                            parmor = earmor
                            global parmorname
                            parmorname = earmorname
                    elif eweapon != 0:
                        stdscr.addstr(5, 38-len(f"The {enemyname} was carrying a {eweaponname}!")//2, f"The {enemyname} was carrying a {eweaponname}!")
                        stdscr.getch()
                        menu("Pick up the weapon?", curses.color_pair(1)|curses.A_BOLD, "Yes", "No")
                        if selection == 1:
                            pweapon = eweapon
                            global pweaponname
                            pweaponname = eweaponname
                    elif coinloot != 0:
                        global pcoins
                        stdscr.addstr(5, 38-len(f"The {enemyname} dropped {coinloot} coins!")//2, f"The {enemyname} dropped {coinloot} coins!")
                        pcoins += coinloot
                        stdscr.getch()
                    else:
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
                    stdscr.getch()
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
            elif selection == 4:
                box()
                stdscr.addstr(3, 5, "Enemy:", curses.color_pair(2)|curses.A_BOLD)
                stdscr.addstr(4, 5, f"Health: {enemyhealth}", curses.color_pair(2)|curses.A_BOLD)
                stdscr.addstr(5, 5, f"Weapon: {eweaponname}", curses.color_pair(2)|curses.A_BOLD)
                stdscr.addstr(6, 5, f"Armor: {earmorname}", curses.color_pair(2)|curses.A_BOLD)
                stdscr.addstr(7, 5, f"Damage: {enemydmg+eweapon}", curses.color_pair(2)|curses.A_BOLD)
                stdscr.addstr(3, 50, "You:", curses.color_pair(3)|curses.A_BOLD)
                stdscr.addstr(4, 50, f"Health: {phealth}", curses.color_pair(3)|curses.A_BOLD)
                stdscr.addstr(5, 50, f"Weapon: {pweaponname}", curses.color_pair(3)|curses.A_BOLD)
                stdscr.addstr(6, 50, f"Armor: {parmorname}", curses.color_pair(3)|curses.A_BOLD)
                stdscr.addstr(7, 50, f"Damage: {pdmg+pweapon}", curses.color_pair(3)|curses.A_BOLD)
                stdscr.addstr(8, 50, f"Experience: {pxp}", curses.color_pair(3)|curses.A_BOLD)
                stdscr.refresh()
                stdscr.getch()

def menu(title, titleattr, option1, option2, option3="", option4="", option5="", option6="", option7="", option8=""):
    global selection
    selection = 1
    attr1 = curses.A_UNDERLINE
    attr2 = 0
    attr3 = 0
    attr4 = 0
    attr5 = 0
    attr6 = 0
    attr7 = 0
    attr8 = 0
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
        elif option6 != "" and option7 == "":
            items = 6
            box()
            stdscr.addstr(3, 38-len(title)//2, title, titleattr)
            stdscr.addstr(5, 38-(len(option1)//2), option1, attr1)
            stdscr.addstr(7, 38-(len(option2)//2), option2, attr2)
            stdscr.addstr(9, 38-(len(option3)//2), option3, attr3)
            stdscr.addstr(11, 38-(len(option4)//2), option4, attr4)
            stdscr.addstr(13, 38-(len(option5)//2), option5, attr5)
            stdscr.addstr(15, 38-(len(option6)//2), option6, attr6)
        elif option7 != "" and option8 == "":
            items = 7
            box()
            stdscr.addstr(3, 38-len(title)//2, title, titleattr)
            stdscr.addstr(5, 38-(len(option1)//2), option1, attr1)
            stdscr.addstr(7, 38-(len(option2)//2), option2, attr2)
            stdscr.addstr(9, 38-(len(option3)//2), option3, attr3)
            stdscr.addstr(11, 38-(len(option4)//2), option4, attr4)
            stdscr.addstr(13, 38-(len(option5)//2), option5, attr5)
            stdscr.addstr(15, 38-(len(option6)//2), option6, attr6)
            stdscr.addstr(17, 38-(len(option7)//2), option7, attr7)
        elif option8 != "":
            items = 8
            box()
            stdscr.addstr(3, 38-len(title)//2, title, titleattr)
            stdscr.addstr(5, 38-(len(option1)//2), option1, attr1)
            stdscr.addstr(7, 38-(len(option2)//2), option2, attr2)
            stdscr.addstr(9, 38-(len(option3)//2), option3, attr3)
            stdscr.addstr(11, 38-(len(option4)//2), option4, attr4)
            stdscr.addstr(13, 38-(len(option5)//2), option5, attr5)
            stdscr.addstr(15, 38-(len(option6)//2), option6, attr6)
            stdscr.addstr(17, 38-(len(option7)//2), option7, attr7)
            stdscr.addstr(19, 38-(len(option8)//2), option8, attr8)
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
            attr7 = 0
            attr8 = 0
        elif selection == 2:
            attr2 = curses.A_UNDERLINE
            attr1 = 0
            attr3 = 0
            attr4 = 0
            attr5 = 0
            attr6 = 0
            attr7 = 0
            attr8 = 0
        elif selection == 3:
            attr3 = curses.A_UNDERLINE
            attr1 = 0
            attr2 = 0
            attr4 = 0
            attr5 = 0
            attr6 = 0
            attr7 = 0
            attr8 = 0
        elif selection == 4:
            attr4 = curses.A_UNDERLINE
            attr1 = 0
            attr2 = 0
            attr3 = 0
            attr5 = 0
            attr6 = 0
            attr7 = 0
            attr8 = 0
        elif selection == 5:
            attr5 = curses.A_UNDERLINE
            attr1 = 0
            attr2 = 0
            attr3 = 0
            attr4 = 0
            attr6 = 0
            attr7 = 0
            attr8 = 0
        elif selection == 6:
            attr6 = curses.A_UNDERLINE
            attr1 = 0
            attr2 = 0
            attr3 = 0
            attr4 = 0
            attr5 = 0
            attr7 = 0
            attr8 = 0
        elif selection == 7:
            attr7 = curses.A_UNDERLINE
            attr1 = 0
            attr2 = 0
            attr3 = 0
            attr4 = 0
            attr5 = 0
            sttr6 = 0
            attr8 = 0
        elif selection == 8:
            attr8 = curses.A_UNDERLINE
            attr1 = 0
            attr2 = 0
            attr3 = 0
            attr4 = 0
            attr5 = 0
            sttr6 = 0
            attr7 = 0
def typetext(y, text, attr):
    for i in range(len(text)):
        #playsound("./sounds/click.wav", False)
        stdscr.addch(y, 38-(len(text)//2)+i, text[i], attr)
        time.sleep(0.05)
        stdscr.refresh()
        stdscr.nodelay(True)
        skip = stdscr.getch()
        if skip == 32:
            stdscr.addstr(y, 1, "                                                                                ")
            stdscr.addstr(y, 38-(len(text)//2), text, attr)
            stdscr.border()
            stdscr.refresh()
            stdscr.nodelay(False)
            break

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
