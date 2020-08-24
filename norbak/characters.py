# Should this be inheritance based or interface based?
# i.e. things that are true of characters or things that are... "fightable"

from .items import Weapon, Armor, InvalidItemException

class Character:
    """This is our base-representation of a character...

    Characters have names, HP, deal damage, "based on exp"
    """
    name = None
    experience_points = None
    weapon = None
    armor = None
    item_bag = None


    @abstractmethod
    def __init__(self, name, experience_points=200, armor=0, pd):
        self.name = name


    def calculate_damage(self):
        if not self.weapon:
            return (self.experience_points // 100)
        return self.weapon.damage + (self.experience_points // 100)


    def calculate_defense(self):
        if not self.armor:
            return 0
        return self.armor.defense


    def calculate_max_health(self):
        return (self.experience_points // 10)


    def equip_item(self, item):
        if isinstance(item, Weapon):
            self.weapon = item
        elif isinstance(item, Armor):
            self.armor = item
        else:
            raise InvalidItemException()


    def on_defeat(self):
        """What happens when we're defeated"""
        pass


    def display_health(self, display):
        """Takes in a TUIManager display and write out the health to it."""
        stdscr.addstr(21, 2, f"{pname}'s health: {phealth}.", curses.color_pair(3) | curses.A_BOLD)
        # TODO: Figure out the display-write API
        display.write(f"{self.name}'s health: {self.current_health}'")


class NonPlayer(Character):

class Player(Character):
    def __init__(self, name, experience_points=200, armor=None, weapon=Weapon.get_weapon("Toy Sword")):
        self.name = name
        self.experience_points = experience_points
        self.armor = armor
        self.weapon = weapon
