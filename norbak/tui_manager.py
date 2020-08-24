import curses


class TUIManager:
    """Hangs onto and drives our curses instance"""


    def __getattr__(self, name):
        """If we don't have an attribute, pass through to the curses screen..."""
        try:
            return self._screen.__getattr__(name)
        except:
            raise AttributeError("Neither TUIManager nor _CursesWindow has attribute %s" % name)


    def __init__(self):
        """Sets up a _CursesWindow and some colors for later use"""
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

        self._screen = stdscr


    def draw_menu(self, menu_title, title_attribute, menu_options, selected_option=0):
        """Draw various kinds of generic menus /w 6 choices
        
        menu_title - the name of the menu
        title_attributes - curses/terminal attributes affecting the title text
        menu_options - up to 6 choices available in the menu
        selected_option - the currently highlighted option, default: 0

        When the user presses up or down arrow keys it changes the highlighted option...
        in a really lazy way.

        Returns the chosen option to the caller?
        """
        if len(menu_options) > 6:
            raise ValueError("You may only use 6 menu options.")

        option_attributes = [0] * len(menu_options)  # Generate an array of zeros
        option_attributes[selected_option] = curses.A_UNDERLINE

        while True:
            # Clear the screen in prep for a menu to be drawn
            self.erase()
            self.border()
            row_numbers = [3, 5, 7, 9, 11, 13, 15]
            self._screen.addstr(row_numbers[0], 38-len(menu_title)//2, menu_title, title_attribute)
            for idx, option in enumerate(menu_options):
                self._screen.addstr(row_numbers[idx+1], 38-len(option)//2, option, option_attributes[idx])

            def move_up():
                if selected_option <= 0:
                    return  # Do nothing
                selected_option -= 1
                option_attributes = [0] * len(menu_options)  # Generate an array of zeros
                option_attributes[selected_option] = curses.A_UNDERLINE

            def move_down():
                if selected_option >= 5:
                    return  # Do nothing
                selected_option += 1
                option_attributes = [0] * len(menu_options)  # Generate an array of zeros
                option_attributes[selected_option] = curses.A_UNDERLINE

            menu_movement = {
                "KEY_UP": move_up,
                "KEY_DOWN": move_down,
            }

            pressed_key = self.getkey()

            if pressed_key == " ":
                return selected_option  # Return the chose option.

            try:
                menu_movement[self.getkey()]()  # NOTE: This is currently very breakable but clever and I like it.
            except:
                pass  # I don't actually care about this exception tbh
        




    def draw_enemy_stats(self, enemy):
        self._screen.addstr(3, 5, "Enemy:", curses.color_pair(2)|curses.A_BOLD)
        self._screen.addstr(4, 5, f"Health: {enemyhealth}", curses.color_pair(2)|curses.A_BOLD)
        self._screen.addstr(5, 5, f"Weapon: {eweaponname}", curses.color_pair(2)|curses.A_BOLD)
        self._screen.addstr(6, 5, f"Armor: {earmorname}", curses.color_pair(2)|curses.A_BOLD)
        self._screen.addstr(7, 5, f"Damage: {enemydmg}", curses.color_pair(2)|curses.A_BOLD)


    def draw_player_stats(self, player):
        self._screen.addstr(4, 50, f"Health: {phealth}", curses.color_pair(3)|curses.A_BOLD)
        self._screen.addstr(5, 50, f"Weapon: {pweaponname}", curses.color_pair(3)|curses.A_BOLD)
        self._screen.addstr(6, 50, f"Armor: {parmorname}", curses.color_pair(3)|curses.A_BOLD)
        self._screen.addstr(7, 50, f"Damage: {pdmg}", curses.color_pair(3)|curses.A_BOLD)
        self._screen.addstr(8, 50, f"Experience: {pxp}", curses.color_pair(3)|curses.A_BOLD)


    def update(self):
        self._screen.refresh()