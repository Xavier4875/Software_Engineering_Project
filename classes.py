class entity:
    def __init__(self, max_health:int, current_health:int, attack:int, defense:int, location:list):
        self.max_health = max_health
        self.current_health = current_health
        self.attack = attack
        self.defense = defense
        self.location = location

    '''def attacks_other(self, other):
        other.current_health -= max(self.attack - other.defense, 0)'''

class player(entity):
    def __init__(self, map_obj, **kwargs):
        super().__init__(**kwargs)
        self.map_obj = map_obj  # This gives the player access to the map object
        # Set the initial location from the map
        self.armor_list = []
        self.weapon_list = []
        self.base_attack = self.attack
        self.base_defense = self.defense
        self.inventory = {"armor": [], "weapon": [], "potion": []}  # Inventory dictionary

    def move(self, direction):
        self.map_obj.move_player(self, direction)

    def add_to_inventory(self, object):
        "Adds an item to the inventory by checking if the given item is armor or a weapon"
        if isinstance(object, armor):
            self.inventory["armor"].append(object)
        elif isinstance(object, weapon):
            self.inventory["weapons"].append(object)
        elif isinstance(object, potion):
            self.inventory["potion"].append(object)


    def equip_armor(self, armor_piece):
        if armor_piece in self.inventory["armor"]:
            self.armor_list.append(armor_piece)
            self.inventory["armor"].remove(armor_piece)
            self.defense = self.base_defense + sum(a.defense_value for a in self.armor_list)

    """removes the armor from armor_list, appends it back to inventory, and
    recalculates player defense when armor is unequipped"""
    def unequip_armor(self, armor_piece):
        if armor_piece in self.armor_list:
            self.armor_list.remove(armor_piece)
            self.inventory["armor"].append(armor_piece)
            self.defense = self.base_defense + sum(a.defense_value for a in self.armor_list)

    def equip_weapon(self, weapon_piece):
        if weapon_piece in self.inventory["weapon"]:
            self.weapon_list.append(weapon_piece)
            self.inventory["weapon"].remove(weapon_piece)
            self.attack = self.base_attack + sum(a.attack_value for a in self.weapon_list)

    def unequip_weapon(self, weapon_piece):
        if weapon_piece in self.weapon_list:
            self.weapon_list.remove(weapon_piece)
            self.inventory["weapon"].append(weapon_piece)
            self.attack = self.base_attack + sum(a.attack_value for a in self.weapon_list)

    def drop_potion(self, potion):
        self.inventory["potion"].remove(potion)


class enemy(entity):
   def __init__(self, max_health: int, current_health: int, attack: int, defense: int, location: list):
       super().__init__(max_health, current_health, attack, defense, location)

class Room:
    def __init__(self, location: list, room_type: str, image_path, Desc: str, enemy = None, enemy_image_path = None, enemy_desc = None, prev = 0,):
        self.location = location  # Coordinates (x, y)
        self.room_type = room_type  # Either 'Enemy', 'Wall', 'Chest', or "S"?
        self.image_path = image_path  # image representing the room?
        self.Desc = Desc #Room description
        self.enemy = enemy
        self.enemy_image_path = enemy_image_path
        self.enemy_desc = enemy_desc
        self.prev = prev


    def __str__(self):
        return f"Room({self.location}, Type: {self.room_type})" #could also add the image path

class potion():
    def __init__(self, size:str):
        self.size = size
        if size == "s":
            self.name = "Small Potion"
        if size == "m":
            self.name = "Medium Potion"
        if size == "l":
            self.name = "Large Potion"
class armor:
    def __init__(self, defense_value:int, name:str, body_part:str):

        self.defense_value = defense_value
        self.name = name
        self.body_part = body_part

class weapon:
    def __init__(self, attack_value:int, name:str):

        self.attack_value = attack_value
        self.name = name


class item:
    def __init__(self, item_type:str):

        self.type = item_type
"""
leather_chestplate = armor(defense_value = 5,name = "leather chestplate", body_part = "chest")
map_obj = None
test_player = player(map_obj, max_health=100, current_health=100, attack=10, defense=5, location=[0, 0])
test_player.equip_armor(leather_chestplate)
print(f"Player's defense: {test_player.defense}")
"""

"""
iron_sword = weapon(attack_value = 5, name = "iron sword")
map_obj = None
test_player = player(map_obj, max_health=100, current_health=100, attack=10, defense=5, location=[0, 0])
test_player.equip_weapon(iron_sword)
print(f"Player's attack: {test_player.attack}")

"""
"""
arr = []

goblin = enemy(100, 100, 10, 10, arr)

orc = enemy(500, 500, 100, 25, arr)

bandit = enemy(250, 250, 75, 20, arr)

Player = entity(1000, 1000, 200, 30, arr)
"""