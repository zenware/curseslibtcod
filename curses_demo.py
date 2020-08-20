## IMPORTING
import random
import time
import curses

from curses import wrapper

# Curses initialization
stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)

def main(stdscr):
    drawbox()
    demo()
    end()

# Draws a nice box.
def drawbox():
    stdscr.clear()
    stdscr.addch(0, 0, "╔")
    stdscr.addch(0, curses.COLS - 2, "╗")
    stdscr.addch(curses.LINES - 1, 0, "╚")
    stdscr.addch(curses.LINES - 1, curses.COLS - 2, "╝")
    for i in range(1, curses.COLS - 2):
        stdscr.addch(0, i, "═")
    for i in range(1, curses.LINES - 1):
        stdscr.addch(i, 0, "║")
    for i in range(1, curses.COLS - 2):
        stdscr.addch(curses.LINES - 1, i, "═")
    for i in range(1, curses.LINES - 1):
        stdscr.addch(i, curses.COLS - 2, "║")

def demo():
    def drawmenu():
        exit = False
        drawbox()
        stdscr.addstr(5, 5, "OPTION 1", curses.A_STANDOUT)
        stdscr.addstr(5, 15, "OPTION 2")
        selection = 1
        while exit == False:
            stdscr.addstr(3, 5, "Here's a small menu mockup. Use the left and right arrow keys to move, and use the down key to select an option. (Press Q when you finish).", curses.A_BOLD)

            key = stdscr.getkey()
            if key == "KEY_LEFT":
                stdscr.addstr(5, 5, "OPTION 1", curses.A_STANDOUT)
                stdscr.addstr(5, 15, "OPTION 2")
                selection = 1
            elif key == "KEY_RIGHT":
                stdscr.addstr(5, 5, "OPTION 1")
                stdscr.addstr(5, 15, "OPTION 2", curses.A_STANDOUT)
                selection = 2
            elif key == "KEY_DOWN":
                stdscr.addstr(7, 5, f"You picked OPTION {selection}", curses.A_BOLD)
            elif key == "q":
                exit = True

    stdscr.addstr(3, 5, "STOP! During this demo, ensure you have fullscreen enabled, since this program is not yet optimized for small windows.", curses.A_BOLD)
    stdscr.addstr(4, 5, "To do this, make your window fullscreen (doing so will automatically exit this program) and then run this program again.", curses.A_BOLD)
    stdscr.addstr(5, 5, "Press a key...", curses.A_BLINK)
    stdscr.getch()
    drawbox()
    stdscr.addstr(3, 5, "As you can see, I've drawn a box that fits perfectly inside your terminal / console.", curses.A_BOLD)
    stdscr.addstr(4, 5, f"This is neat, because I know that your window is {curses.LINES} cells tall and {curses.COLS} cells wide and draw the box accordingly.", curses.A_BOLD)
    stdscr.addstr(5, 5, "(Note that those numbers change accordingly to your window size. BUT if you change your window size now, the program will exit.)", curses.A_BOLD)
    stdscr.addstr(6, 5, "Press a key...", curses.A_BLINK)
    stdscr.getch()
    drawbox()
    stdscr.addstr(3, 5, "This is significant because it only took 11 lines of Python to do so.", curses.A_BOLD)
    stdscr.addstr(4, 5, "Press a key to see the code...", curses.A_STANDOUT)
    stdscr.getch()
    drawbox()
    stdscr.addstr(3, 5, "stdscr.addch(0, 0, '╔')")
    stdscr.addstr(4, 5, "stdscr.addch(0, curses.COLS - 2, '╗')")
    stdscr.addstr(5, 5, "stdscr.addch(curses.LINES - 1, 0, '╚')")
    stdscr.addstr(6, 5, "stdscr.addch(curses.LINES - 1, curses.COLS - 2, '╝')")
    stdscr.addstr(7, 5, "for i in range(1, curses.COLS - 2):")
    stdscr.addstr(8, 5, "    stdscr.addch(0, i, '═')")
    stdscr.addstr(9, 5, "for i in range(1, curses.LINES - 1):")
    stdscr.addstr(10, 5, "    stdscr.addch(i, 0, '║')")
    stdscr.addstr(11, 5, "for i in range(1, curses.COLS - 2):")
    stdscr.addstr(12, 5, "    stdscr.addch(curses.LINES - 1, i, '═')")
    stdscr.addstr(13, 5, "for i in range(1, curses.LINES - 1):")
    stdscr.addstr(14, 5, "    stdscr.addch(i, curses.COLS - 2, '║')")
    stdscr.addstr(16, 5, "Press a key...", curses.A_BLINK)
    stdscr.getch()
    drawbox()
    stdscr.addstr(3, 5, "All of this was done with the power of CURSES!", curses.A_BOLD)
    stdscr.addstr(4, 5, "(Note that I'm not trying to convince you to use it, I know you are already interested lol. This is just a demo to show off the capabilities!)", curses.A_BOLD)
    stdscr.addstr(5, 5, "Press a key...", curses.A_BLINK)
    stdscr.getch()
    drawbox()
    stdscr.addstr(3, 5, "You can do fancy things such as...")
    stdscr.addstr(4, 5, "Have BLINKY text!", curses.A_BLINK)
    stdscr.addstr(5, 5, "Have BOLD text!", curses.A_BOLD)
    stdscr.addstr(6, 5, "Have HIGHLIGHTED text!", curses.A_STANDOUT)
    stdscr.addstr(7, 5, "Have UNDERLINED text!", curses.A_UNDERLINE)

    if curses.has_colors():
        curses.init_pair(1, curses.COLOR_MAGENTA, curses.COLOR_YELLOW)
        curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_RED)
        stdscr.addstr(8, 5, "Have COLORED text!", curses.color_pair(1))
        stdscr.addstr(9, 5, "And MORE colored text!", curses.color_pair(2))
    else:
        stdscr.addstr(8, 5, "And you'd be seeing colored text if you had a color terminal!", curses.A_BOLD)

    stdscr.addstr(11, 5, "Press a key...", curses.A_BLINK)
    stdscr.getch()
    drawbox()
    stdscr.addstr(3, 5, "And all of this is a total breeze to do. It only took me half an hour to write this demo!", curses.A_BOLD)
    stdscr.addstr(4, 5, "Press a key...", curses.A_BLINK)
    stdscr.getch()
    drawmenu()
    drawbox()
    stdscr.addstr(3, 5, "Anyways, that's all I wanted to show you. It should be noted, however, that you will need to rewrite much of your code if you want to work with Curses.", curses.A_BOLD)
    stdscr.addstr(4, 5, "Press a key to exit the program...", curses.A_BLINK)
    stdscr.getch()

# De-initializes curses.
def end():
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    curses.endwin()

wrapper(main)
