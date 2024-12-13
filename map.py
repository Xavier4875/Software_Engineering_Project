#10-10-24
# MVP SWE
# Creating a map that will later be connected to the UI and other conditions/classes
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from random import *
from classes import *

num_steps = [2]

class LevelMap:
    def __init__(self, level):
        self.level = level
        self.player_position = [0, 0]
        self.exit_position = [0, 0]
        self.map = self.create_map(level)

    def create_map(self, level):
        if level == 1:
            self.player_position = [4, 0]
            self.exit_position = [4, 0]

            #create the room objects
            return [
                [Room([0,0], 'Chest', './Resources/dungeon1.jpg', 'Chest Room Full of chests\nYou pick up A new set of armor and a new weapon\nClick Next then a direction to continue', [armor(5, "Leather Chestplate", "body_armor"), armor(5, "Leather Cap", "head_armor"), potion("s"), potion("m"), potion("l")]), Room([0,1], 'Enemy', './Resources/dungeon1.jpg','A Marble lit hall', enemy(80, 80, 15, 10, [0,1], ), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"), Room([0,2], 'Enemy', './Resources/dungeon2.jpg',"A dark Marble room", enemy(80, 80, 15, 10, [0,2]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"), Room([0,3], 'Enemy', './Resources/dungeon3.jpg', "A dark forrest sprouts around you", enemy(80, 80, 15, 10, [0, 3]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"), Room([0,4], 'Enemy', './Resources/dungeon4.jpg', "A fire filled cavern", enemy(80, 80, 15, 10, [0,4]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"), Room([0,5], 'Enemy', './Resources/dungeon5.jpg', "A fiery environment envelops you. Something dangerous lies ahead", enemy(50, 50, 30, 10, [0, 5]), './Resources/orc.jpg', "An orc jumps out and slashes at your armor!"), Room([0,6], 'Enemy', './Resources/dungeon5.jpg', "A fiery environment envelops you.", enemy(50, 50, 30, 10, [0,6]), './Resources/orc.jpg', "An orc jumps out and slashes at your armor!"), Room([0,7], 'StairsD', './Resources/dungeon1.jpg', "The stairs down\nPress Next to continue down")],
                [Room([1,0], 'Wall', './Resources/dungeon1.jpg',"You Should not be here"), Room([1,1], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"), Room([1,2], 'Wall', './Resources/dungeon1.jpg',"You Should not be here"), Room([1,3], 'Enemy', './Resources/dungeon24.jfif',"The path begins to narrow...", enemy(80, 80, 15, 10, [1,3]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"), Room([1,4], 'Enemy', './Resources/dungeon8.jpg',"A well lit arch appears before you", enemy(80, 80, 15, 10, [1,4]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"), Room([1,5], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"), Room([1,6], 'Wall', './Resources/dungeon1.jpg', "You should not be here"), Room([1,7], 'Wall', './Resources/dungeon1.jpg',"You Should not be here")],
                [Room([2,0], 'Wall', './Resources/dungeon1.jpg',"You Should not be here"), Room([2,1], 'Wall', './Resources/dungeon1.jpg',"You Should not be here"), Room([2,2], 'Wall', './Resources/dungeon1.jpg',"You Should not be here"), Room([2,3], 'Enemy', './Resources/dungeon9.jpg',"A dark path lies ahead", enemy(20, 20, 12, 10, [2, 3]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."), Room([2,4], 'Enemy', './Resources/dungeon10.jpg',"a door stands in front of you, it leads into the dark", enemy(20, 20, 12, 10, [2, 4]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."), Room([2,5], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"), Room([2,6], 'Wall', './Resources/dungeon1', "You Should not be here"), Room([2,7], 'Wall', './Resources/dungeon1', "You Should not be here")],
                [Room([3,0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"), Room([3,1], 'Wall', './Resources/dungeon1.jpg',"You Should not be here"), Room([3,2], 'Wall', './Resources/dungeon1.jpg',"You Should not be here"), Room([3,3], 'Enemy', './Resources/dungeon11.jpg',"A armory stands before you", enemy(20, 20, 12, 10, [3, 3]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."), Room([3,4], 'Enemy', './Resources/dungeon23.jfif', "The path gets more dangerous ahead", enemy(20, 20, 12, 10, [3,4]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."), Room([3,5], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"), Room([3,6], 'Wall', './Resources/dungeon1', "You Should not be here"), Room([3,7], 'Wall', './Resources/dungeon1', "You Should not be here")],
                [Room([4,0], 'Player', './Resources/dungeon12.jpg', "The exit, I must not return here"), Room([4,1], 'Enemy', './Resources/dungeon13.jpg',"An old entryway stands before you", enemy(20, 20, 12, 10, [4, 1]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."), Room([4,2], 'Enemy', './Resources/dungeon14.jpg', "You sense danger in each step", enemy(20, 20, 12, 10, [4, 2]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."), Room([4,3], 'Enemy', './Resources/dungeon15.jpg', "lanterns light your way north", enemy(20, 20, 12, 10, [4, 3]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."), Room([4,4], 'Enemy', './Resources/dungeon16.jpg',"It becomes darker again", enemy(20, 20, 12, 10, [4, 4]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."), Room([4,5], 'Enemy', './Resources/dungeon17.jpg',"You reach the warmth of a fireplace", enemy(20, 20, 12, 10, [4, 5]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."), Room([4,6], 'Enemy', './Resources/dungeon18.jpg', "More abandoned environments seem to expand around you", enemy(20, 20, 12, 10, [4, 6]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."), Room([4,7], 'Enemy', './Resources/dungeon19.jpg', "A dance studio equipped with jojo merch", enemy(20, 20, 12, 10, [4, 7]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle.")],
            ]
        if level == 2:
            self.player_position = [4, 0]
            self.exit_position = [4, 0]
            # create the room objects
            return [
                [Room([0, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([0, 1], 'Enemy', './Resources/dungeon55.jpg', 'A cold illuminated hall stands before you',
                      enemy(80, 80, 15, 10, [0,1]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([0, 2], 'Enemy', './Resources/dungeon2.jpg', "A dark Marble room",
                      enemy(80, 80, 15, 10, [0,2]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([0, 3], 'Chest', './Resources/dungeon1.jpg', 'Chest Room Full of chests\nYou pick up A new set of armor and a new weapon\nClick Next then a direction to continue',
                      [weapon(10, "Sharp Sword"), armor(5, "Right Glove", "right_gauntlet"), potion("s"), potion("m"), potion("l")]),
                 Room([0, 4], 'Enemy', './Resources/dungeon63.jpg', "A dim light shows in front of you",
                      enemy(50, 50, 30, 10, [0,4]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([0, 5], 'Enemy', './Resources/dungeon66.jpg', "The light draws closer",
                      enemy(50, 50, 30, 10, [0,5]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([0, 6], 'Enemy', './Resources/dungeon64.jpg', "The light is upon you just in the next room",
                      enemy(50, 50, 30, 10, [0,4]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([0, 7], 'Chest', './Resources/dungeon68.jpg',
                      'Three items sit before you, you pick them up\nClick Next then a direction to continue',
                      [armor(10, "Bold Boots", "boots"), armor(5, "Seemless", "pants"), armor(5, "Left Glove", "left_gauntlet")]),],

                [Room([1, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([1, 1], 'Enemy', './Resources/dungeon62.jpg', "The path winds ahead",
                      enemy(80, 80, 15, 10, [1,1]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([1, 2], 'Enemy', './Resources/dungeon80.jpg', "a warm room with a spire stands before you",
                      enemy(80, 80, 15, 10, [1,2]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([1, 3], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([1, 4], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([1, 5], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([1, 6], 'Enemy', './Resources/dungeon77.jpg', "A carpeted room spreads around you",
                      enemy(50, 50, 30, 10, [1, 6]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([1, 7], 'Enemy', './Resources/dungeon79.jpg',"a warmer room appears as you progress",
                      enemy(50, 50, 30, 10, [1, 7]), './Resources/orc.jpg', "An orc jumps out and slashes your armor")],

                [Room([2, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([2, 1], 'Enemy', './Resources/dungeon61.jpg', "A dark path lies ahead, only a light fixture illuminates your path",
                      enemy(80, 80, 15, 10, [2,1]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([2, 2], 'Enemy', './Resources/dungeon66.jpg', "You grow weary with each step",
                      enemy(80, 80, 15, 10, [2,2]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([2, 3], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([2, 4], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([2, 5], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([2, 6], 'Enemy', './Resources/dungeon66.jpg', "By now you'd expect to see more adversaries",
                      enemy(50, 50, 30, 10, [2, 6]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([2, 7], 'Enemy', './Resources/dungeon70.jpg', "You reach the warmth of a mostly empty room",
                      enemy(50, 50, 30, 10, [2, 7]), './Resources/orc.jpg', "An orc jumps out and slashes your armor")],


                [Room([3, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 1], 'Enemy', './Resources/dungeon57.jpg', "A dark path lies ahead, light shines through the wall to the right",
                      enemy(80, 80, 15, 10, [3, 1]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([3, 2], 'Enemy', './Resources/dungeon112.jpg', "The empty halls echo with the lives that used to live here",
                      enemy(80, 80, 15, 10, [3, 2]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([3, 3], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 4], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 5], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 6], 'Enemy', './Resources/dungeon115.jpg', "You look back and see the glow of past rooms",
                      enemy(50, 50, 30, 10, [2, 6]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([3, 7], 'Enemy', './Resources/dungeon126.jpg', "Someone or something used to live here",
                      enemy(50, 50, 30, 10, [2, 7]), './Resources/orc.jpg', "An orc jumps out and slashes your armor")],

                [Room([4, 0], 'StairsU', './Resources/dungeon12.jpg', "A glowing staircase spirals upward, leading to the previous level."),
                 Room([4, 1], 'Enemy', './Resources/dungeon159.jpg', "This floor seems darker than the last",
                      enemy(80, 80, 15, 10, [4, 1]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([4, 2], 'Enemy', './Resources/dungeon157.jpg', "Tip: The dev is tired of writing explanations",
                      enemy(80, 80, 15, 10, [4, 2]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([4, 3], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([4, 4], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([4, 5], 'StairsD', './Resources/dungeon1.jpg', "A glowing staircase spirals downward, leading to the next level"),
                 Room([4, 6], 'Enemy', './Resources/dungeon168.jpg', "You can see the way down from here",
                      enemy(50, 50, 30, 10, [4, 6]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([4, 7], 'Enemy', './Resources/dungeon178.jpg', "The architecture seems weird here",
                      enemy(50, 50, 30, 10, [2, 7]), './Resources/orc.jpg', "An orc jumps out and slashes your armor")],
            ]

        if level == 3:
            self.player_position = [0,0]
            self.exit_position = [0, 0]
            # create the room objects
            return [
                [Room([0, 0], 'StairsU', './Resources/dungeon12.jpg', "A glowing staircase spirals upward, leading to the previous level."),
                 Room([0, 1], 'Enemy', './Resources/dungeon13.jpg',"An old entryway stands before you",
                      enemy(20, 20, 12, 10, [0, 1]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."),
                 Room([0, 2], 'Enemy', './Resources/dungeon2.jpg', "A dark Marble room",
                      enemy(80, 80, 15, 10, [0, 2]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([0, 3], 'Enemy', './Resources/dungeon3.jpg', "A dark forest sprouts arond you",
                      enemy(80, 80, 15, 10, [0, 3]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([0, 4], 'Enemy', './Resources/dungeon178.jpg', "The architecture seems weird here",
                      enemy(50, 50, 30, 10, [0, 4]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([0, 5], 'Enemy', './Resources/dungeon159.jpg', "This floor seems darker than the last",
                      enemy(20, 20, 12, 10, [0, 5]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."),
                 Room([0, 6], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([0, 7], 'Wall', './Resources/dungeon1.jpg', "You Should not be here")],
                
                [Room([1, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([1, 1], 'Enemy', './Resources/dungeon18.jpg',"More abandoned enviroments seem to expand around you", 
                      enemy(80, 80, 15, 10, [1,1]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([1, 2], 'Enemy', './Resources/dungeon66.jpg', "By now you'd expect to see more adversaries",
                      enemy(50, 50, 30, 10, [1, 2]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([1, 3], 'Enemy', './Resources/dungeon70.jpg', "You reach the warmth of a mostly empty room",
                      enemy(50, 50, 30, 10, [1, 3]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([1, 4], 'Enemy',  './Resources/dungeon190.jpg', "A creepy lonely hall",
                       enemy(20, 20, 12, 10, [0, 1]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."),
                 Room([1, 5], 'Enemy', './Resources/dungeon3.jpg', "A dark forest sprouts arond you",
                      enemy(80, 80, 15, 10, [1,5]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([1, 6], 'Enemy', './Resources/dungeon17.jpg', "You reach the warmth of a fireplace",
                      enemy(80, 80, 15, 10, [1,6]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([1, 7], 'Enemy', './Resources/dungeon66.jpg', "By now you'd expect to see more adversaries",
                      enemy(50, 50, 30, 10, [1, 7]), './Resources/orc.jpg', "An orc jumps out and slashes your armor")],
                
                [Room([2, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([2, 1], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([2, 2], 'Enemy', './Resources/dungeon2.jpg', "A dark Marble room",
                      enemy(80, 80, 15, 10, [2,2]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([2, 3], 'Enemy', './Resources/dungeon9.jpg', "A dark path lies ahead",
                      enemy(80, 80, 15, 10, [2,3]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"), 
                 Room([2, 4], 'Enemy', './Resources/dungeon10.jpg',"A door stands in front of you, it leads into the dark",
                      enemy(80, 80, 15, 10, [2,4]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([2, 5], 'Enemy', './Resources/dungeon5.jpg', "A firery envrioment envelops you",
                      enemy(50, 50, 30, 10, [2,5]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([2, 6], 'Wall', './Resources/dungeon1', "You Should not be here"),
                 Room([2, 7], 'Wall', './Resources/dungeon1', "You Should not be here")],
                
                [Room([3, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 1], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 2], 'Enemy', './Resources/dungeon3.jpg', "A dark forrest sprouts arond you",
                      enemy(50, 50, 30, 10, [3,2]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([3, 3], 'Enemy', './Resources/dungeon11.jpg', "A armory stands before you",
                      enemy(80, 80, 15, 10, [3, 3]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([3, 4], 'Enemy', './Resources/dungeon13.jpg',"An old entryway stands before you",
                      enemy(20, 20, 12, 10, [3, 4]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."),
                 Room([3, 5], 'Enemy', './Resources/dungeon146.jpg', "A dark red room is at sight",
                      enemy(80, 80, 15, 10, [3, 5]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([3, 6], 'Wall', './Resources/dungeon1', "You Should not be here"),
                 Room([3, 7], 'Wall', './Resources/dungeon1', "You Should not be here")],
                
                [Room([4, 0], 'Chest', './Resources/dungeon1.jpg', 'Chest Room Full of chests\nYou pick up A new set of armor and a new weapon\nClick Next then a direction to continue',
                      [armor(20, "Dwarven Plate", "body_armor"), armor(1, "Broken", "body_armor"), weapon(25, "Sharp Nail"), potion("s"), potion("m"), potion("l")]),
                 Room([4, 1], 'Enemy', './Resources/dungeon108.jpg', "You see through the fog an abandoned hall",
                       enemy(55, 55,  35, 10, [4,1]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([4, 2], 'Enemy', './Resources/dungeon79.jpg', "The room is bathed in an eerie orange glow with single pool table sitting in the center.",
                       enemy(20, 20, 12, 10, [4,2]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."),
                 Room([4, 3], 'Enemy', './Resources/dungeon15.jpg', "laterns light your way north",
                      enemy(50, 50, 30, 10, [4,3]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([4, 4], 'Enemy', './Resources/dungeon66.jpg', "The air hangs heavy with an unsettling silence, broken only by the soft crackle of the candles that illuminate the room.",
                      enemy(55, 55,  35, 10, [4,4]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([4, 5], 'Enemy', './Resources/dungeon17.jpg', "You reach the warmth of a fireplace",
                       enemy(20, 20, 12, 10, [4,5]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."),
                 Room([4, 6], 'Enemy', './Resources/dungeon18.jpg', "More abandoned enviroments seem to expand around you",
                      enemy(55, 55,  35, 10, [4,6]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([4, 7], 'StairsD', './Resources/dungeon1.jpg', "A glowing staircase spirals downward, leading to the next level.")],
            ]

        if level == 4:
            self.player_position = [3,0]
            self.exit_position = [3, 0]
            # create the room objects
            return [
                [Room([0, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([0, 1], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([0, 2], 'StairsD', './Resources/dungeon9.jpg', "A dark path lies ahead",
                     enemy(55, 55,  35, 10, [0,2]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([0, 3], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([0, 4], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([0, 5], 'StairsD', './Resources/dungeon1.jpg', "A glowing staircase spirals downward, leading to the next level."),
                 Room([0, 6], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([0, 7], 'Wall', './Resources/dungeon1.jpg', "You Should not be here")],
                [Room([1, 0], 'StairsD', './Resources/dungeon1.jpg', "A glowing staircase spirals downward, leading to the next level."),
                 Room([1, 1], 'Enemy', './Resources/dungeon9.jpg', "A dark path lies ahead",
                       enemy(20, 20, 12, 10, [1,1]), './Resources/goblin.jpg', "A goblin has caught you! Prepare for battle."),
                 Room([1, 2], 'Enemy', './Resources/dungeon2.jpg', "A dark Marble room",
                       enemy(50, 50, 30, 10, [1,2]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([1, 3], 'Enemy','./Resources/dungeon159.jpg', "This floor seems darker than the last",
                      enemy(80, 80, 15, 10, [1,3]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([1, 4], 'Enemy', './Resources/dungeon8.jpg', "A well lit arch appears before you",
                        enemy(50, 50, 30, 10, [1,4]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([1, 5], 'Enemy', './Resources/dungeon2.jpg', "A dark Marble room",
                      enemy(80, 80, 15, 10, [1, 5]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([1, 6], 'Enemy', './Resources/dungeon190.jpg', "A creepy lonely hall",
                      enemy(80, 80, 15, 10, [1, 6]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([1, 7], 'StairsD', './Resources/dungeon1.jpg', "A glowing staircase spirals downward, leading to the next level.")],

                [Room([2, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([2, 1], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([2, 2], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([2, 3], 'Enemy', './Resources/dungeon9.jpg', "A dark path lies ahead",
                      enemy(80, 80, 15, 10, [2, 3]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([2, 4], 'Enemy', './Resources/dungeon10.jpg', "a door stands in front of you, it leads into the dark",
                      enemy(80, 80, 15, 10, [2,4]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([2, 5], 'Enemy', './Resources/dungeon153.jpg', "A very brigth, yet lonely hall",
                      enemy(65, 65, 45, 20, [2,5]), './Resources/Zom.png', "An evil Zombie appears out of nowhere, attack!"),
                 Room([2, 6], 'Wall', './Resources/dungeon1', "You Should not be here"),
                 Room([2, 7], 'Wall', './Resources/dungeon1', "You Should not be here")],
                [Room([3, 0], 'StairsU', './Resources/dungeon1.jpg', "A glowing staircase spirals upward, leading to the previous level."),
                 Room([3, 1], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 2], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 3], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 4], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 5], 'Enemy', './Resources/dungeon5.jpg', "A firery envrioment envelops you",
                      enemy(65, 65, 45, 20, [3,5]), './Resources/Zom.png', "An evil Zombie appears out of nowhere, attack!"),
                 Room([3, 6], 'Wall', './Resources/dungeon1', "You Should not be here"),
                 Room([3, 7], 'Wall', './Resources/dungeon1', "You Should not be here")],
                [Room([4, 0], 'Enemy', './Resources/dungeon108.jpg', "You see though the fog an abandoned hall",
                      enemy(55, 55, 35, 10, [4,0]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([4, 1], 'Enemy', './Resources/dungeon13.jpg', "An old entryway stands before you",
                      enemy(55, 55,  35, 10, [4,1]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([4, 2], 'Chest', './Resources/dungeon1.jpg', 'Chest Room Full of chests\nYou pick up A new set of armor and a new weapon\nClick Next then a direction to continue',
                      [armor(25, "Golden Helm", "head_armor"), armor(20, "Golden Shorts", "pants"), potion("s"), potion("m"), potion("l")]),
                 Room([4, 3], 'Enemy', './Resources/dungeon15.jpg', "laterns light your way north",
                      enemy(80, 80, 15, 10, [4, 3]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([4, 4], 'Enemy', './Resources/dungeon16.jpg', "It becomes darker again",
                      enemy(80, 80, 15, 10, [4, 4]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([4, 5], 'Enemy', './Resources/dungeon17.jpg', "You reach the warmth of a fireplace",
                      enemy(50, 50, 30, 10, [4,5]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([4, 6], 'Enemy', './Resources/dungeon18.jpg',"More abandoned enviroments seem to expand around you",
                      enemy(65, 65, 45, 20, [4,6]), './Resources/Zom.png', "An evil Zombie appears out of nowhere, attack!"),
                 Room([4, 7], 'StairsD', './Resources/dungeon1.jpg', "A glowing staircase spirals downward, leading to the next level.")],
            ]


        if level == 5:
            self.player_position = [3,0]
            self.exit_position = [3, 0]

            # create the room objects
            return [
                [Room([0, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([0, 1], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([0, 2], 'Enemy', './Resources/dungeon2.jpg', "A dark Marble room",
                      enemy(65, 65, 45, 20, [0,2]), './Resources/Zom.png', "An evil Zombie appears out of nowhere, attack!"),
                 Room([0, 3], 'Enemy', './Resources/dungeon3.jpg', "A dark forest sprouts arond you",
                      enemy(50, 50, 30, 10, [0,3]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([0, 4], 'Enemy', './Resources/dungeon4.jpg', "A fire filled cavern",
                      enemy(50, 50, 30, 10, [0,4]), './Resources/orc.jpg', "An orc jumps out and slashes your armor"),
                 Room([0, 5], 'Enemy', './Resources/dungeon5.jpg', "A firery envrioment envelops you",
                      enemy(55, 55, 35, 10, [0,5]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([0, 6], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([0, 7], 'Wall', './Resources/dungeon1.jpg', "You Should not be here")],
                [Room([1, 0], 'Enemy', './Resources/dungeon5.jpg', "A firery envrioment envelops you",
                      enemy(55, 55,  35, 10, [1,0]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([1, 1], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([1, 2], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([1, 3], 'Enemy', './Resources/dungeon135.jpg', "You can barely see anything!",
                      enemy(65, 65, 45, 20, [1,3]), './Resources/Zom.png', "An evil Zombie appears out of nowhere, attack!"),
                 Room([1, 4], 'Enemy', './Resources/dungeon8.jpg', "A well lit arch appears before you",
                      enemy(65, 65, 45, 20, [1,4]), './Resources/Zom.png', "An evil Zombie appears out of nowhere, attack!"),
                 Room([1, 5], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([1, 6], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([1, 7], 'Enemy', './Resources/dungeon9.jpg', "A dark path lies ahead",
                      enemy(80, 80, 15, 10, [1,7]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'")],
                [Room([2, 0], 'Enemy', './Resources/dungeon9.jpg', "A dark path lies ahead",
                      enemy(80, 80, 15, 10, [2, 0]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([2, 1], 'Enemy', './Resources/dungeon13.jpg', "An old entryway stands before you",
                      enemy(80, 80, 15, 10, [2, 1]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([2, 2], 'Enemy', './Resources/dungeon79.jpg', "The room is bathed in an eerie orange glow with single pool table sitting in the center.",
                      enemy(55, 55,  35, 10, [2,2]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([2, 3], 'Enemy', './Resources/dungeon9.jpg', "A dark path lies ahead",
                       enemy(55, 55,  35, 10, [2,3]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),

                      
                 Room([2, 4], 'Boss', './Resources/dungeon10.jpg', "a door stands in front of you, it leads into the dark",
                       enemy(200, 200, 25, 20, [2, 4]),'./Resources/Mini.png', "Must use all your strenght and be clever to defeat the FINAL boss"),
                 Room([2, 5], 'Enemy', './Resources/dungeon3.jpg', "A dark forrest sprouts arond you",
                      enemy(80, 80, 15, 10, [2,5]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([2, 6], 'Enemy', './Resources/dungeon146.jpg', "A dark red room is at sight",
                       enemy(80, 80, 15, 10, [2,6]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([2, 7], 'Enemy', './Resources/dungeon108.jpg', "You see though the fog an abandoned hall",
                      enemy(80, 80, 15, 10, [2,7]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'")],
                [Room([3, 0], 'StairsU', './Resources/dungeon12.jpg', "A glowing staircase spirals upward, leading to the previous level."),
                 Room([3, 1], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 2], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 3], 'Enemy','./Resources/dungeon66.jpg', "The air hangs heavy with an unsettling silence, broken only by the soft crackle of the candles that illuminate the room.",
                      enemy(80, 80, 15, 10, [3,3]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([3, 4], 'Enemy', './Resources/dungeon108.jpg', "You see though the fog an abandoned hall",
                      enemy(55, 55,  35, 10, [3,4]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([3, 5], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 6], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([3, 7], 'Enemy', './Resources/dungeon19.jpg', "A dance studio equipped with jojo merch",
                      enemy(55, 55,  35, 10, [3,7]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light")],
                [Room([4, 0], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([4, 1], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([4, 2], 'Enemy', './Resources/dungeon14.jpg', "You sense danger in each step",
                      enemy(55, 55,  35, 10, [4,2]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([4, 3], 'Enemy', './Resources/dungeon15.jpg', "laterns light your way north",
                      enemy(80, 80, 15, 10, [4,3]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([4, 4], 'Enemy', './Resources/dungeon16.jpg', "It becomes darker again",
                      enemy(80, 80, 15, 10, [4,4]), './Resources/bandit.jpg', "You've been seen by a bandit! 'You should not be here!'"),
                 Room([4, 5], 'Enemy', './Resources/dungeon79.jpg', "The room is bathed in an eerie orange glow with single pool table sitting in the center.",
                      enemy(55, 55,  35, 10, [4,5]),'./Resources/Skelly.png', "Prepare for Battle! A menacing skeleton stands before you, its hollow eyes glowing with eerie light"),
                 Room([4, 6], 'Wall', './Resources/dungeon1.jpg', "You Should not be here"),
                 Room([4, 7], 'Wall', './Resources/dungeon1.jpg', "You Should not be here")],
            ]


    def display_map(self):
        for row in self.map:
            print(' '.join([room.room_type[0] for room in row]))
        print("---------------------\n") #to separate new location

def move_player(self, direction, player):
    x, y = player.location #gets coordinates each time
    print(f"Player current position: {x}, {y}")
    print(f"Trying to move: {direction}")

    if direction == 'up' and x > 0:
        new_position = [x - 1, y]
    elif direction == 'down' and x < len(self.map) - 1:
        new_position = [x + 1, y]
    elif direction == 'left' and y > 0:
        new_position = [x, y - 1]
    elif direction == 'right' and y < len(self.map[0]) - 1:
        new_position = [x, y + 1]
    else:
        print("Invalid move! Player is at the edge of the map or there's a wall.")
        return -1
    
    if self.map[new_position[0]][new_position[1]].room_type == 'Wall':#checks for walls
        print("Invalid move! There's a wall.")
        return -1

    #updates the positon of the player


    if self.map[x][y].prev != 1:
        if self.map[x][y].room_type != 'StairsU' and self.map[x][y].room_type != 'StairsD' and self.map[x][y].room_type != 'Chest':
            self.map[x][y].room_type = 'Enemy'
     


    self.player_position = new_position
    player.location = new_position
    self.display_map() #new map with new position
    
    print(f"New position: {new_position[0]}, {new_position[1]}") #helps us visualize where it is f no issues when moving

    if self.map[new_position[0]][new_position[1]].room_type == 'Enemy': # checks for enemies
        if self.map[new_position[0]][new_position[1]].room_type != 'StairsU' and self.map[new_position[0]][new_position[1]].room_type != 'StairsD' and self.map[new_position[0]][new_position[1]].room_type != 'Chest':
            self.map[new_position[0]][new_position[1]].room_type = 'Player'

        if num_steps[0] >= 2:
            num = randint(1, 3)

            if num == 2:
                num_steps[0] = 0
                return 1
            else:
                num_steps[0] += 1
                return 0

        else:
            num_steps[0] += 1
            return 0
    elif self.map[new_position[0]][new_position[1]].room_type == 'Chest': #checks for chest room
        return 3
    elif self.map[new_position[0]][new_position[1]].room_type == 'Boss':
        self.map[new_position[0]][new_position[1]].room_type = 'Player'
        return 2
    elif self.map[new_position[0]][new_position[1]].room_type == 'StairsD':
        return 4
    elif self.map[new_position[0]][new_position[1]].room_type == 'StairsU':
        return 5
    else:
        self.map[new_position[0]][new_position[1]].room_type = 'Player'
        num_steps[0] += 1
        return 0





if __name__ == "__main__":
    dungeon = LevelMap(1)
    dungeon.display_map()

    #instructions loop
    myPlayer = player(map_obj=dungeon, max_health=100, current_health=100, attack=20,defense=10, location=dungeon.player_position)
    while True:
        move = input("Enter your move (up (forward), down (backward), left, right) or quit: ")
        if move == 'quit': #we need a quit button
            break
        move_player(dungeon, move, myPlayer)
        dungeon.display_map()
