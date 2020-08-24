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

from characters import Player, NonPlayer
from tui_manager import TUIManager

import logging


tui = TUIManager()  # This controls our Curses TUI
# global player = Player(name="")

def main(tui):
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
        tui.bkgd(curses.ACS_S1)
        tui.refresh()
        time.sleep(0.05)
        tui.bkgd(curses.ACS_S1)
        tui.refresh()
        time.sleep(0.05)
        tui.bkgd(curses.ACS_S7)
        tui.refresh()
        time.sleep(0.05)
        tui.bkgd(curses.ACS_S9)
        tui.refresh()
        time.sleep(0.05)
    tui.bkgd(" ")
    for i in range(len(title1)):
        time.sleep(0.05)
        tui.addch(10, 38-(len(title1)//2)+i, title1[i], curses.color_pair(1))
        tui.refresh()
    time.sleep(1)
    for i in range(len(title1)):
        time.sleep(0.05)
        tui.addch(10, 38-(len(title1)//2)+i, " ")
        tui.refresh()
    for i in range(len(title2)):
        time.sleep(0.05)
        tui.addch(10, 38-(len(title2)//2)+i, title2[i], curses.color_pair(1))
        tui.refresh()
    time.sleep(1)
    for i in range(len(title2)):
        time.sleep(0.05)
        tui.addch(10, 38-(len(title2)//2)+i, " ")
        tui.refresh()
    for i in range(len(title3)):
        time.sleep(0.10)
        tui.addch(10, 38-(len(title3)//2)+i, title3[i], curses.color_pair(2) | curses.A_BOLD)
        tui.refresh()
    for i in range(8):
        box()
        time.sleep(0.5)
        tui.addstr(num0 - i, 38-(len(title3)//2), title3, curses.color_pair(2) | curses.A_BOLD)
        tui.refresh()

def mainmenu():
    choice = tui.draw_menu(
        menu_title="THE FIRES OF NORBAK",
        title_attribute=curses.color_pair(2) | curses.A_BOLD,
        menu_options=["PLAY", "QUIT"]
    )
    if choice == 1:
        ureg()
    else:
        end()

def ureg():
    global pname
    box()
    center("Welcome, traveller. Enter your name below.")
    tui.addstr(3, cy, "Welcome, traveller. Enter your name below.", curses.A_BOLD)
    curses.textpad.rectangle(tui, 5, 32, 7, 43)
    #tui.addstr(7, 32, "____________", curses.A_BOLD)
    curses.echo()
    pname = tui.getstr(6, 33, 10)
    pname = pname.decode('utf-8')
    if pname == "":
        ureg()

    player = Player(name=pname)  # Create a player with default stats and a custom name.

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
        tui.addstr(14-i, 38-(len(f"Oh, {pname}, tell us you are the powerful warrior we've been waiting on!")//2), f"Oh, {pname}, tell us you are the powerful warrior we've been waiting on!", curses.A_BOLD | curses.color_pair(1))
        time.sleep(0.10)
        tui.refresh()
    choice = tui.draw_menu(
        menu_title=f"Oh, {pname}, tell us you are the powerful warrior we've been waiting on!",
        title_attribute=curses.A_BOLD | curses.color_pair(1),
        menu_options=["Yes, I am.", "No, I am not."]
    )
    if choice == 1:
        start()
    elif choice == 2:
        box()
        typetext(3, "Oh, only the gods above can save us now!", curses.A_BOLD)
        gameover()

    return player

def start():
    box()
    typetext(3, "Thank the heavens!", curses.A_BOLD)
    typetext(5, "Here, take this map, it will guide you along your journey...", curses.A_BOLD)
    typetext(7, "To the Fires of Norbak!", curses.A_BOLD | curses.color_pair(2))
    tui.getch()
    #viewmap()

def viewmap():
    box()
    choice = tui.draw_menu(
        menu_title="Map",
        title_attribute=curses.color_pair(1) | curses.A_BOLD,
        menu_options=[  # TODO: Pull out location details into some sort of data-file.
            "The Fungal Forests", 
            "The Vermin Caves", 
            "The Evil Town", 
            "The Dragon's Lair", 
            "Goblin Mountain"
        ]
    )
    if choice == 1:
        loc("The Fungal Forests", 2)
    elif choice == 2:
        loc("The Vermin Caves", 4)
    elif choice == 3:
        loc("The Evil Town", 6)
    elif choice == 4:
        loc("The Dragon's Lair", 8)
    elif choice == 5:
        loc("Goblin Mountain", 10)
    elif choice == 6:
        town()

def town():
    global pcoins
    global pweaponname
    global pweapon
    global parmorname
    global parmor
    tui.draw_menu("Shop", curses.color_pair(3)|curses.A_BOLD, ["Armor", "Weapons", "View Map"])
    if choice == 1:
        tui.draw_menu("Armor Shop", curses.color_pair(3)|curses.A_BOLD, ["Cloth Rags: 100", "Hardened Leather: 200", "Chain Mail: 300", "Metal Armor: 400", "Hardened Metal Armor: 500", "Back"])
        if choice == 1:
            if pcoins >= 100:
                pcoins -= 100
                parmor = 1
                parmorname = "Cloth Rags"
                box()
                center(f"You bought a {parmorname}! You have {pcoins} coins left.")
                tui.addstr(3, cy, f"You bought a {parmorname}! You have {pcoins} coins left.", curses.A_BOLD)
                tui.getch()
                town()
            else:
                box()
                center("You don't have enough coins!")
                tui.addstr(3, cy, "You don't have enough coins!", curses.A_BOLD)
                tui.getch()
                town()
        elif choice == 2:
            if pcoins >= 200:
                pcoins -= 200
                parmor = 2
                parmorname = "Hardened Leather"
                box()
                center(f"You bought a {parmorname}! You have {pcoins} coins left.")
                tui.addstr(3, cy, f"You bought a {parmorname}! You have {pcoins} coins left.", curses.A_BOLD)
                tui.getch()
                town()
            else:
                box()
                center("You don't have enough coins!")
                tui.addstr(3, cy, "You don't have enough coins!", curses.A_BOLD)
                tui.getch()
                town()
        elif choice == 3:
            if pcoins >= 300:
                pcoins -= 300
                parmor = 3
                parmorname = "Chain Mail"
                box()
                center(f"You bought a {parmorname}! You have {pcoins} coins left.")
                tui.addstr(3, cy, f"You bought a {parmorname}! You have {pcoins} coins left.", curses.A_BOLD)
                tui.getch()
                town()
            else:
                box()
                center("You don't have enough coins!")
                tui.addstr(3, cy, "You don't have enough coins!", curses.A_BOLD)
                tui.getch()
                town()
        elif choice == 4:
            if pcoins >= 400:
                pcoins -= 400
                parmor = 4
                parmorname = "Metal Armor"
                box()
                center(f"You bought a {parmorname}! You have {pcoins} coins left.")
                tui.addstr(3, cy, f"You bought a {parmorname}! You have {pcoins} coins left.", curses.A_BOLD)
                tui.getch()
                town()
            else:
                box()
                center("You don't have enough coins!")
                tui.addstr(3, cy, "You don't have enough coins!", curses.A_BOLD)
                tui.getch()
                town()
        elif choice == 5:
            if pcoins >= 500:
                pcoins -= 500
                parmor = 5
                parmorname = "Hardened Metal Armor"
                box()
                center(f"You bought a {parmorname}! You have {pcoins} coins left.")
                tui.addstr(3, cy, f"You bought a {parmorname}! You have {pcoins} coins left.", curses.A_BOLD)
                tui.getch()
                town()
            else:
                box()
                center("You don't have enough coins!")
                tui.addstr(3, cy, "You don't have enough coins!", curses.A_BOLD)
                tui.getch()
                town()
        elif choice == 6:
            town()
    elif choice == 2:
        choice = tui.draw_menu(
            "Weapon Shop",
            curses.color_pair(3)|curses.A_BOLD,
            ["Toy Sword: 100", "Small Dagger: 200", "Staff: 300", "Short Sword: 400", "Long Sword: 500", "Back"]
        )
        if choice == 1:
            if pcoins >= 100:
                pcoins -= 100
                pweapon = 1
                pweaponname = "Toy Sword"
                box()
                center(f"You bought a {pweaponname}! You have {pcoins} coins left.")
                tui.addstr(3, cy, f"You bought a {pweaponname}! You have {pcoins} coins left.", curses.A_BOLD)
                tui.getch()
                town()
            else:
                box()
                center("You don't have enough coins!")
                tui.addstr(3, cy, "You don't have enough coins!", curses.A_BOLD)
                tui.getch()
                town()
        elif choice == 2:
            if pcoins >= 200:
                pcoins -= 200
                pweapon = 2
                pweaponname = "Small Dagger"
                box()
                center(f"You bought a {pweaponname}! You have {pcoins} coins left.")
                tui.addstr(3, cy, f"You bought a {pweaponname}! You have {pcoins} coins left.", curses.A_BOLD)
                tui.getch()
                town()
            else:
                box()
                center("You don't have enough coins!")
                tui.addstr(3, cy, "You don't have enough coins!", curses.A_BOLD)
                tui.getch()
                town()
        elif choice == 3:
            if pcoins >= 300:
                pcoins -= 300
                pweapon = 3
                pweaponame = "Staff"
                box()
                center(f"You bought a {pweaponname}! You have {pcoins} coins left.")
                tui.addstr(3, cy, f"You bought a {pweaponname}! You have {pcoins} coins left.", curses.A_BOLD)
                tui.getch()
                town()
            else:
                box()
                center("You don't have enough coins!")
                tui.addstr(3, cy, "You don't have enough coins!", curses.A_BOLD)
                tui.getch()
                town()
        elif choice == 4:
            if pcoins >= 400:
                pcoins -= 400
                pweapon = 4
                pweaponname = "Short Sword"
                box()
                center(f"You bought a {pweaponname}! You have {pcoins} coins left.")
                tui.addstr(3, cy, f"You bought a {pweaponname}! You have {pcoins} coins left.", curses.A_BOLD)
                tui.getch()
                town()
            else:
                box()
                center("You don't have enough coins!")
                tui.addstr(3, cy, "You don't have enough coins!", curses.A_BOLD)
                tui.getch()
                town()
        elif choice == 5:
            if pcoins >= 500:
                pcoins -= 500
                pweapon = 5
                pweaponname = "Long Sword"
                box()
                center(f"You bought a {pweaponname}! You have {pcoins} coins left.")
                tui.addstr(3, cy, f"You bought a {pweaponname}! You have {pcoins} coins left.", curses.A_BOLD)
                tui.getch()
                town()
            else:
                box()
                center("You don't have enough coins!")
                tui.addstr(3, cy, "You don't have enough coins!", curses.A_BOLD)
                tui.getch()
                town()
        elif choice == 6:
            town()
    elif choice == 3:
        viewmap()

def loc(location, difficulty):
    choice = tui.draw_menu(
        menu_title=f"{location}",
        title_attribute=curses.color_pair(3) | curses.A_BOLD,
        menu_options=["Look for something to kill", "View map"]
    )
    if choice == 1:
        combat(location, difficulty)
    elif choice == 2:
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
        global pname
        tui.addstr(22, 2, f"{pname}'s health: {phealth}.", curses.color_pair(3) | curses.A_BOLD)
        tui.addstr(22, 50, f"{enemyname}'s health: {enemyhealth}", curses.color_pair(2) | curses.A_BOLD)
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
        center(f"You are entering combat with a {enemyname}!")
        tui.addstr(3, cy, f"You are entering combat with a {enemyname}!", curses.A_BOLD | curses.color_pair(2))
        tui.getch()
        while True:
            choice = tui.draw_menu(
                menu_title=f"{enemyname}",
                title_attribute=curses.color_pair(2) | curses.A_BOLD,
                menu_options=["ATTACK", "DEFEND", "RUN", "STATS"]
            )
            if choice == 1:
                # Your attack
                box()
                displayhealth()
                tui.refresh()
                time.sleep(1)
                center(f"Attacking the {enemyname}!")
                tui.addstr(3, cy, f"Attacking the {enemyname}!", curses.color_pair(2) | curses.A_BOLD)
                tui.refresh()
                time.sleep(1)
                global pweapon
                pturndmg = randint(0, pdmg) - earmor
                if pturndmg < 0:
                    pturndmg = 0
                enemyhealth -= pturndmg
                box()
                displayhealth()
                if pturndmg == 0:
                    center(f"You missed the {enemyname}!")
                    tui.addstr(3, cy, f"You missed the {enemyname}!", curses.A_BOLD)
                else:
                    #playsound("./sounds/atk.wav", False)
                    center(f"You dealt {pturndmg} to the {enemyname}!")
                    tui.addstr(3, cy, f"You dealt {pturndmg} damage to the {enemyname}!", curses.color_pair(2) | curses.A_BOLD)
                tui.refresh()
                time.sleep(1)
                if enemyhealth <= 0:
                    box()
                    global pxp
                    pxp += enemyid*5
                    center(f"You killed the {enemyname}! You get {enemyid*5} experience points.")
                    tui.addstr(3, cy, f"You killed the {enemyname}! You get {enemyid*5} experience points.", curses.color_pair(3) | curses.A_BOLD)
                    center(f"You now have {pxp} experience points!")
                    tui.addstr(4, cy, f"You now have {pxp} experience points!", curses.color_pair(3) | curses.A_BOLD)
                    if earmor != 0:
                        center(f"The {enemyname} was wearing a {earmorname}!")
                        tui.addstr(5, cy, f"The {enemyname} was wearing a {earmorname}!")
                        tui.getch()
                        choice = tui.draw_menu("Pick up the armor?", curses.color_pair(1)|curses.A_BOLD, ["Yes", "No"])
                        if choice == 1:
                            global parmor
                            parmor = earmor
                            global parmorname
                            parmorname = earmorname
                    elif eweapon != 0:
                        center(f"The {enemyname} was carrying a {eweaponname}!")
                        tui.addstr(5, cy, f"The {enemyname} was carrying a {eweaponname}!")
                        tui.getch()
                        choice = tui.draw_menu("Pick up the weapon?", curses.color_pair(1)|curses.A_BOLD, ["Yes", "No"])
                        if choice == 1:
                            pweapon = eweapon
                            global pweaponname
                            pweaponname = eweaponname
                    elif coinloot != 0:
                        global pcoins
                        center(f"The {enemyname} dropped {coinloot} coins!")
                        tui.addstr(5, cy, f"The {enemyname} dropped {coinloot} coins!")
                        pcoins += coinloot
                        tui.getch()
                    else:
                        tui.getch()
                    loc(location, difficulty)

                # Enemy's attack
                box()
                displayhealth()
                tui.refresh()
                time.sleep(1)
                center(f"{enemyname} is attacking!")
                tui.addstr(3, cy, f"{enemyname} is attacking!", curses.color_pair(2) | curses.A_BOLD)
                tui.refresh()
                time.sleep(1)
                eturndmg = randint(0, enemydmg) + eweapon - parmor
                if eturndmg < 0:
                    eturndmg = 0
                global phealth
                phealth -= eturndmg
                box()
                displayhealth()
                if eturndmg == 0:
                    center(f"The {enemyname} missed you!")
                    tui.addstr(3, cy, f"The {enemyname} missed you!", curses.color_pair(3) | curses.A_BOLD)
                else:
                    #playsound("./sounds/atk.wav", False)
                    center(f"The {enemyname} dealt {eturndmg} damage to you!")
                    tui.addstr(3, cy, f"The {enemyname} dealt {eturndmg} damage to you!", curses.color_pair(2) | curses.A_BOLD)
                tui.refresh()
                time.sleep(1)
                if phealth <= 0:
                    gameover()
            elif choice == 2:
                box()
                displayhealth()
                center("You spend the turn resting...")
                tui.addstr(3, cy, "You spend the turn resting.", curses.A_BOLD)
                tui.refresh()
                time.sleep(1)
                recover = phealth // 4
                phealth += recover
                if phealth > pxp // 10:
                    phealth = pxp // 10
                box()
                displayhealth()
                center(f"You recovered {recover} health!")
                tui.addstr(3, cy, f"You recovered {recover} health!", curses.A_BOLD | curses.color_pair(3))
                tui.refresh()
                time.sleep(1)
                box()
                displayhealth()
                tui.refresh()
                time.sleep(1)
                center(f"{enemyname} is attacking!")
                tui.addstr(3, cy, f"{enemyname} is attacking!", curses.color_pair(2) | curses.A_BOLD)
                tui.refresh()
                time.sleep(1)
                eturndmg = randint(0, enemydmg) + eweapon - parmor
                if eturndmg < 0:
                    eturndmg = 0
                #global phealth
                phealth -= eturndmg
                box()
                displayhealth()
                if eturndmg == 0:
                    center(f"The {enemyname} missed you!")
                    tui.addstr(3, cy, f"The {enemyname} missed you!", curses.color_pair(3) | curses.A_BOLD)
                else:
                    #playsound("./sounds/atk.wav", False)
                    center(f"The {enemyname} dealt {eturndmg} damage to you!")
                    tui.addstr(3, cy, f"The {enemyname} dealt {eturndmg} damage to you!", curses.color_pair(2) | curses.A_BOLD)
                tui.refresh()
                time.sleep(1)
                if phealth <= 0:
                    gameover()
            elif choice == 3:
                gotaway = randint(0, 3)
                if gotaway == 2 or gotaway == 3:
                    box()
                    center("You got away!")
                    tui.addstr(3, cy, "You got away!", curses.A_BOLD)
                    tui.refresh()
                    tui.getch()
                    loc(location, difficulty)
                elif gotaway == 0 or 1:
                    box()
                    center("You didn't get away!")
                    tui.addstr(3, cy, "You didn't get away!", curses.A_BOLD)
                    tui.getch()
                    eturndmg = randint(0, enemydmg) + eweapon - parmor
                    if eturndmg < 0:
                        eturndmg = 0
                    #global phealth
                    phealth -= eturndmg
                    box()
                    displayhealth()
                    if eturndmg == 0:
                        center(f"The {enemyname} missed you!")
                        tui.addstr(3, cy, f"The {enemyname} missed you!", curses.color_pair(3) | curses.A_BOLD)
                    else:
                        #playsound("./sounds/atk.wav", False)
                        center(f"The {enemyname} dealt {eturndmg} damage to you!")
                        tui.addstr(3, cy, f"The {enemyname} dealt {eturndmg} damage to you!", curses.color_pair(2) | curses.A_BOLD)
                    tui.refresh()
                    time.sleep(1)
                    if phealth <= 0:
                        gameover()
            elif choice == 4:
                box()
                tui.draw_enemy_stats(current_enemy)
                tui.draw_player_stats(player)
                tui.update()
                tui.getch()  # NOTE: This should passthrough to the _CursesWindow with __getattr__ override...

def typetext(y, text, attr):
    for i in range(len(text)):
        #playsound("./sounds/click.wav", False)
        center(text)
        tui.addch(y, cy+i, text[i], attr)
        time.sleep(0.05)
        tui.refresh()
        tui.nodelay(True)
        skip = tui.getch()
        if skip == 32:
            tui.addstr(y, 1, "                                                                                ")
            tui.addstr(y, cy, text, attr)
            tui.border()
            tui.refresh()
            tui.nodelay(False)
            break
    tui.nodelay(False)


def box():
    tui.erase()
    tui.border()

def center(text):
    global cy
    cy = 38-len(text)//2
    return cy

def gameover():
    time.sleep(1)
    box()
    tui.refresh()
    time.sleep(1)
    #playsound("./sounds/death.wav", False)
    for i in range(len("GAME OVER")):
        tui.addch(11, 38-(len("GAME OVER")//2)+i, "GAME OVER"[i], curses.color_pair(2) | curses.A_BOLD)
        time.sleep(0.10)
        tui.refresh()
    tui.getch()
    mainmenu()

# De-init curses and window.
def end():
    curses.nocbreak()
    tui.keypad(False)
    curses.echo()
    curses.endwin()
    quit()

wrapper(main)
