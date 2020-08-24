"""Details about items such as weapons and armor."""
import json


class Weapon:
    name = None
    damage = 0
    
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


    @staticmethod
    def get_weapon(name):
        """Generates a weapon based on a name.
        
        TODO: Pull the data loader into some initialization thing
        Make an Item Factory.
        """
        with open("config.json") as f:
            game_config = json.load(f)

        try:
            damage = game_config['weapons'][name]['damage']
        except:
            AttributeError("No Weapon with name %s in config" % name)

        return Weapon(
            name=name,
            damage=damage
        )



class Armor:
    name = None
    defense = 0

    def __init__(self, name, defense):
        self.name = None
        self.defense = None


class InvalidItemException:
    pass