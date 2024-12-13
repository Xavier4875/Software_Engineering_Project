from map import *
from combat import *
from classes import *
import unittest

class TestUM(unittest.TestCase):

    def setUp(selfself):
        pass

    def test_Enemy_player(self):
        dungeon = LevelMap(1)
        myPlayer = player(map_obj=dungeon, max_health=100, current_health=100, attack=20, defense=10,
                          location=dungeon.player_position)
        myEnemy = enemy(100,100,10,10,[1,1])

        #Player
        self.assertEqual(100,myPlayer.max_health)
        self.assertEqual(100, myPlayer.current_health)
        self.assertEqual(20, myPlayer.attack)
        self.assertEqual(10, myPlayer.defense)

        #enemy
        self.assertEqual(100, myEnemy.max_health)
        self.assertEqual(100, myEnemy.current_health)
        self.assertEqual(10, myEnemy.attack)
        self.assertEqual(10, myEnemy.defense)

    def test_map_gen(self):
        dungeon = LevelMap(1)

        #column 1 room types
        self.assertEqual(dungeon.map[0][0].room_type,"Chest")
        self.assertEqual(dungeon.map[1][0].room_type, "Wall")
        self.assertEqual(dungeon.map[2][0].room_type, "Wall")
        self.assertEqual(dungeon.map[3][0].room_type, "Wall")
        self.assertEqual(dungeon.map[4][0].room_type, "Player")

        # column 2 room types
        self.assertEqual(dungeon.map[0][1].room_type, "Enemy")
        self.assertEqual(dungeon.map[1][1].room_type, "Wall")
        self.assertEqual(dungeon.map[2][1].room_type, "Wall")
        self.assertEqual(dungeon.map[3][1].room_type, "Wall")
        self.assertEqual(dungeon.map[4][1].room_type, "Enemy")

        # column 3 room types
        self.assertEqual(dungeon.map[0][2].room_type, "Enemy")
        self.assertEqual(dungeon.map[1][2].room_type, "Wall")
        self.assertEqual(dungeon.map[2][2].room_type, "Wall")
        self.assertEqual(dungeon.map[3][2].room_type, "Wall")
        self.assertEqual(dungeon.map[4][2].room_type, "Enemy")

        # column 4 room types
        self.assertEqual(dungeon.map[0][3].room_type, "Enemy")
        self.assertEqual(dungeon.map[1][3].room_type, "Enemy")
        self.assertEqual(dungeon.map[2][3].room_type, "Enemy")
        self.assertEqual(dungeon.map[3][3].room_type, "Enemy")
        self.assertEqual(dungeon.map[4][3].room_type, "Enemy")

        # column 5 room types
        self.assertEqual(dungeon.map[0][4].room_type, "Enemy")
        self.assertEqual(dungeon.map[1][4].room_type, "Enemy")
        self.assertEqual(dungeon.map[2][4].room_type, "Enemy")
        self.assertEqual(dungeon.map[3][4].room_type, "Enemy")
        self.assertEqual(dungeon.map[4][4].room_type, "Enemy")

        # column 6 room types
        self.assertEqual(dungeon.map[0][5].room_type, "Enemy")
        self.assertEqual(dungeon.map[1][5].room_type, "Wall")
        self.assertEqual(dungeon.map[2][5].room_type, "Wall")
        self.assertEqual(dungeon.map[3][5].room_type, "Wall")
        self.assertEqual(dungeon.map[4][5].room_type, "Enemy")

        # column 7 room types
        self.assertEqual(dungeon.map[0][6].room_type, "Enemy")
        self.assertEqual(dungeon.map[1][6].room_type, "Wall")
        self.assertEqual(dungeon.map[2][6].room_type, "Wall")
        self.assertEqual(dungeon.map[3][6].room_type, "Wall")
        self.assertEqual(dungeon.map[4][6].room_type, "Enemy")

        # column 8 room types
        self.assertEqual(dungeon.map[0][7].room_type, "StairsD")
        self.assertEqual(dungeon.map[1][7].room_type, "Wall")
        self.assertEqual(dungeon.map[2][7].room_type, "Wall")
        self.assertEqual(dungeon.map[3][7].room_type, "Wall")
        self.assertEqual(dungeon.map[4][7].room_type, "Enemy")

    def test_Enemy(self):

        #Gen map
        dungeon = LevelMap(1)

        #check first enemy
        self.assertEqual(50,dungeon.map[0][6].enemy.current_health)
        self.assertEqual(50,dungeon.map[0][6].enemy.max_health)
        self.assertEqual(30,dungeon.map[0][6].enemy.attack)
        self.assertEqual(10,dungeon.map[0][6].enemy.defense)
        self.assertEqual([0, 6],dungeon.map[0][6].enemy.location)

        # check second enemy
        self.assertEqual(20, dungeon.map[3][4].enemy.current_health)
        self.assertEqual(20, dungeon.map[3][4].enemy.max_health)
        self.assertEqual(12, dungeon.map[3][4].enemy.attack)
        self.assertEqual(10, dungeon.map[3][4].enemy.defense)
        self.assertEqual([3,4], dungeon.map[3][4].enemy.location)

        # check second enemy
        self.assertEqual(80, dungeon.map[1][3].enemy.current_health)
        self.assertEqual(80, dungeon.map[1][3].enemy.max_health)
        self.assertEqual(15, dungeon.map[1][3].enemy.attack)
        self.assertEqual(10, dungeon.map[1][3].enemy.defense)
        self.assertEqual([1, 3], dungeon.map[1][3].enemy.location)

        #max_health: int, current_health: int, attack: int, defense: int, location: list

    def test_combat(self):
        dungeon = LevelMap(1)
        myPlayer = player(map_obj=dungeon, max_health=100, current_health=100, attack=20,defense=10, location=dungeon.player_position)
        goblin = enemy(100, 100, 12, 10, [1,1])
        goblin1 = enemy(100, 100, 5, 10, [1,1])
        goblin3 = enemy(1,1,100000000,1, [1,1])

        #damage register and defense check
        combat(myPlayer,goblin)
        self.assertEqual(98,myPlayer.current_health)

        #check if damage block works
        combat(myPlayer, goblin1)
        self.assertEqual(98, myPlayer.current_health)

        #check if death function works
        Death = combat(myPlayer,goblin3)
        self.assertEqual(98,myPlayer.current_health)
        self.assertEqual(0,Death)

    def test_move(self):

        #Create world
        dungeon = LevelMap(1)
        myPlayer = player(map_obj=dungeon, max_health=100, current_health=100, attack=20,defense=10, location=dungeon.player_position)

        #Check right
        move_player(dungeon,"right",myPlayer)
        self.assertEqual([4,1],myPlayer.location)
        self.assertEqual([4,1],dungeon.player_position)

        #check left
        move_player(dungeon, "right", myPlayer)
        move_player(dungeon, "right", myPlayer)
        move_player(dungeon, "right", myPlayer)
        move_player(dungeon, "left", myPlayer)
        self.assertEqual([4, 3], myPlayer.location)
        self.assertEqual([4, 3], dungeon.player_position)

        #check up
        move_player(dungeon, "up", myPlayer)
        self.assertEqual([3, 3], myPlayer.location)
        self.assertEqual([3, 3], dungeon.player_position)

        #check down
        move_player(dungeon, "down", myPlayer)
        self.assertEqual([4, 3], myPlayer.location)
        self.assertEqual([4, 3], dungeon.player_position)

        #check border
        move_player(dungeon, "down", myPlayer)
        self.assertEqual([4, 3], myPlayer.location)
        self.assertEqual([4, 3], dungeon.player_position)

        #check wall
        move_player(dungeon, "up", myPlayer)
        move_player(dungeon, "left", myPlayer)
        self.assertEqual([3, 3], myPlayer.location)
        self.assertEqual([3, 3], dungeon.player_position)

    def test_equip_gen(self):
        dungeon = LevelMap(1)  # Create the map object
        Player = player(map_obj=dungeon, max_health=100, current_health=100, attack=20, defense=10,
                          location=dungeon.player_position)  # Create the player and link to the mapls

        Player.inventory["armor"].append(armor(200, "Test", "body_armor"))
        Player.inventory["armor"].append(armor(200, "Test", "head_armor"))
        Player.inventory["armor"].append(armor(200, "Test", "left_gauntlet"))
        Player.inventory["armor"].append(armor(200, "Test", "right_gauntlet"))
        Player.inventory["armor"].append(armor(200, "Test", "pants"))
        Player.inventory["armor"].append(armor(200, "Test", "boots"))
        Player.inventory["weapon"].append(weapon(200, "Test"))

        for cdd in Player.inventory["armor"]:
            self.assertEqual("Test", cdd.name)

        for bdd in Player.inventory["weapon"]:
            self.assertEqual("Test", bdd.name)


    def test_equip_arm(self):
        holder = 10
        dungeon = LevelMap(1)  # Create the map object
        Player = player(map_obj=dungeon, max_health=100, current_health=100, attack=20, defense=10,
                        location=dungeon.player_position)  # Create the player and link to the mapls

        Player.inventory["armor"].append(armor(200, "Test", "body_armor"))
        Player.inventory["armor"].append(armor(200, "Test", "head_armor"))
        Player.inventory["armor"].append(armor(200, "Test", "left_gauntlet"))
        Player.inventory["armor"].append(armor(200, "Test", "right_gauntlet"))
        Player.inventory["armor"].append(armor(200, "Test", "pants"))
        Player.inventory["armor"].append(armor(200, "Test", "boots"))
        Player.inventory["weapon"].append(weapon(200, "Test"))

        for cdd in Player.inventory["armor"]:
            Player.equip_armor(cdd)
            self.assertEqual(holder + 200, Player.defense)
            holder = holder + 200

    def test_equip_wep(self):
        holder = 20
        dungeon = LevelMap(1)  # Create the map object
        Player = player(map_obj=dungeon, max_health=100, current_health=100, attack=20, defense=10,
                        location=dungeon.player_position)  # Create the player and link to the mapls

        Player.inventory["weapon"].append(weapon(200, "Test"))
        Player.inventory["weapon"].append(weapon(200, "1233"))

        for bdd in Player.inventory["weapon"]:
            Player.equip_weapon(bdd)
            self.assertEqual(holder + 200, Player.attack)
            holder = holder + 200

    def test_unequip_arm(self):
        holder = 10
        dungeon = LevelMap(1)  # Create the map object
        Player = player(map_obj=dungeon, max_health=100, current_health=100, attack=20, defense=10,
                        location=dungeon.player_position)  # Create the player and link to the mapls

        Player.inventory["armor"].append(armor(200, "Test", "body_armor"))
        Player.inventory["armor"].append(armor(200, "Test", "head_armor"))
        Player.inventory["armor"].append(armor(200, "Test", "left_gauntlet"))
        Player.inventory["armor"].append(armor(200, "Test", "right_gauntlet"))
        Player.inventory["armor"].append(armor(200, "Test", "pants"))
        Player.inventory["armor"].append(armor(200, "Test", "boots"))
        Player.inventory["weapon"].append(weapon(200, "Test"))

        for cdd in Player.inventory["armor"]:
            Player.equip_armor(cdd)
            self.assertEqual(holder + 200, Player.defense)
            Player.unequip_armor(cdd)
            self.assertEqual(holder, Player.defense)

    def test_unequip_wep(self):
        holder = 20
        dungeon = LevelMap(1)  # Create the map object
        Player = player(map_obj=dungeon, max_health=100, current_health=100, attack=20, defense=10,
                        location=dungeon.player_position)  # Create the player and link to the mapls

        Player.inventory["weapon"].append(weapon(200, "Test"))
        Player.inventory["weapon"].append(weapon(200, "1233"))

        for bdd in Player.inventory["weapon"]:
            Player.equip_weapon(bdd)
            self.assertEqual(holder + 200, Player.attack)
            Player.unequip_weapon(bdd)
            self.assertEqual(holder, Player.attack)

if __name__ == '__main__':
    unittest.main()

