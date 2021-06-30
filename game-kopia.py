#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import os

class Character:
    
    def __init__(self, name, health, strength, power, dexterity):
         self.name = name
         self.health = health
         self.strength = strength
         self.power = power
         self.dexterity = dexterity

         self.alive = True
         
    def get_health(self):
        return self.health
    
    def get_strength(self):
        return self.strength
     
    def get_power(self):
        return self.power
    
    def get_dexterity(self):
        return self.dexterity
    
    def get_name(self):
        return self.name
    
    def get_level(self):
        return self.level
    
    def is_alive(self):
        return self.alive
    
    def increase_level(self, p):
        self.level += p
     
    def change_health(self, i):
        self.health += i
        if self.health < 1:
            self.alive = False
    
    def set_strength(self, ns):
        self.strength = ns
    
    def set_power(self, np):
        self.power = np
    
    def set_dexterity(self, nd):
        self.dexterity = nd
    
    def set_dead(self):
        self.alive = False
    
        
    
         
class Player(Character):
    def __init__(self, name, health, strength, power, dexterity):
        super(Player, self).__init__(name, health, strength, 
                       power, dexterity)

        self.exp = 0
        
    def get_exp(self):
        return self.exp
    def change_exp(self, i):
        self.exp += i
        

        

class Generator:
    def enemyGen(self):
        temp = []
        file = open("enemys.txt","r")
        lines = file.readlines()
        enemy_name = lines[random.randint(0,len(lines)-1)][:-1]
        file.close
        vals = [30, 45, 60]
        random.shuffle(vals)
        a = vals[0]
        b = vals[1]
        c = vals[2]
        health = random.randint(1,5)
        attack = random.randint(10,a)
        power = random.randint(10,b)
        dexterity = random.randint(10,c)
        return Character(enemy_name, health, attack, power, dexterity)




class Item:
    def __innit__(self, name, description, modifier, attribute):
        self.name = name
        self.description = description
        self.modifier = modifier
        self.attribute = attribute


class Food(Item):
    def be_consumed(self):
        self.__del__()



class Inventory:
    def __innit__(self, capacity):
        self.content = []
        self.capacity = capacity
    
    def add(self, item):
        if self.content.length() < self.capacity:
            self.content.append(item)
        else:
            print("TO DO")
    
    def delete(self, item):
         self.content.append.remove(item)
         
    def clear(self):
        self.content = []
        
    def __innit__(self, integer):
        self.capacity += integer
    


class State:
    def __init__(self):
        global states
        self.end = False
        self.end_game = False
    
    def request_end(self): return self.end
    
    def ending_game(self): return self.end_game
    
    def update(self): None

    
    
    
class MainMenu(State):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.character_created = False
    def update(self):
        if not self.character_created:
            gui.Title()
            gui.option("1", "Choose character")
            gui.option("2", "Exit game")
            number = ''
            while number != "1" and number != "2":
                number = gui.get_input("")
            return number
            self.request_end()

    def proccess_input(self, inp):
        if inp == "1":
            player = CharacterCreator()
            states.append(CharacterCreator())
            self.character_created = True
            states.pop()
        elif inp == "2":
            self.end_game = True
        else:
            return "invalid input"
    
    def character_cr(self):
        self.character_cr = True
        
            
        
        
class RoomState(State):
    def __init__(self):
        super(RoomState, self).__init__()
    def update(self):
        global player
        generator = Generator()
        encounter = generator.enemyGen()
        gui.enter_room(encounter)
        while encounter.is_alive() and player.is_alive():
            gui.fight_interface(player, encounter)
            ch = gui.get_input("What are you doing?").lower()
            self.attack_enemy(ch, player, encounter)
            os.system("clear")
            if not encounter.is_alive(): 
                time.sleep(2)
                break
            gui.fight_interface(player, encounter)
            time.sleep(2)
            self.attack_enemy(str(random.randint(1,2)), encounter, player)
            time.sleep(2)
            os.system("clear")
        if player.is_alive():
            player.change_exp(10)
            gui.show_stats(player)
            print("EXP: " + str(player.get_exp()))
            print()
            print(encounter.get_name() + " is dead!") 
            input("Press enter when you're ready to get in to the next room ")
        else:
            self.end_game = True
            
        
    
    def attack_enemy(self, typ, ch1, ch2):
        time.sleep(1)
        print()
        print(ch1.get_name() + " attacks " + ch2.get_name())
        print()
        time.sleep(1)
        rzut_pl = random.randint(1, 100)
        rzut_en = random.randint(1, 100)
        if typ == "1":
            if (ch1.get_strength() - rzut_pl) >= (ch2.get_strength() - rzut_en):
                print(ch2.get_name() + " gets hit!")
                print()
                time.sleep(2)
                ch2.change_health(-1)
            else:
                print(ch2.get_name() + " doesn't get hit!")
                print()
                time.sleep(2)
                
        elif typ == "2":
            if (ch1.get_power() - rzut_pl) >= (ch2.get_power() - rzut_en):
                print(ch2.get_name() + " gets hit!")
                print()
                time.sleep(2)
                ch2.change_health(-1)
            else:
                print(ch2.get_name() + " doesn't get hit!")
                print()
                time.sleep(2)
        elif typ == "3":
            if (ch1.get_dexterity() - rzut_pl) >= (ch2.get_dexterity() - rzut_en):
                print(ch2.get_name() + " gets hit!")
                print()
                time.sleep(2)
                ch2.change_health(-1)
            else:
                print(ch2.get_name() + " doesn't get hit!")
                print()
                time.sleep(2)
        else:
            print()
            print('Enter "1", "2" or "3"!!!')
            print()
        
        
class CharacterCreator(State):

    def __init__(self):
        super(CharacterCreator, self).__init__()
        self.created = False
        self.update()
    def update(self):
        while not self.created:
            gui.fighters()
            fighter = gui.get_input("Choose your fighter ").lower()
            global player
            if fighter == "wizard":
                player = Player("Wizard", 7, 30, 50, 40)
                self.created = True
                return player
            elif fighter == "knight":
                player = Player("Knight", 7, 50, 40, 30)
                self.created = True
                return player
            elif fighter == "archer":
                player = Player("Archer", 7, 40, 30, 50)
                self.created = True
                return player
        self.request_end()

        

    
    

class GUI:
    def Title(self):
        os.system("clear")
        print("=====WELCOME=====")
        print("       TO A")
        print("     RPG_GAME\n")
    def option(self, i, option):
        print(f"- {i} -> " + option)
        
    def get_input(self, i):
        j = input(i + " ----> ")
        return j
    
    def fighters(self):
        os.system("clear")
        print("                    AVAIBLE FIGHTERS\n  ")
        print("                 WIZARD|KNIGHT|ARCHER|")
        print("STRENGTH:          30 |  50  |   40   ")
        print("POWER:             50 |  40  |   30  ")
        print("DEXTERITY:         40 |  30  |   50  ")
        print("\n")
    
    def enter_room(self, encounter):
        os.system("clear")
        time.sleep(1)
        print("You are entering a room...\n")
        time.sleep(2)
        print("The door are closing behind you...\n")
        time.sleep(2)
        if str(type(encounter)) == "<class '__main__.Character'>":
            print("There is a " + encounter.get_name() + " in front of you.\n")
            time.sleep(1)
            print("Get ready to fight\n")
            time.sleep(2.5)
            os.system("clear")
        else:
            print("Your luck's in!")
            print(type(encounter))
            time.sleep(1)
            print("You found a " + encounter.get_name())
    
    def show_stats(self, char):
        print(char.name)
        print("HP: " + str(char.health))
        print("STRENGTH: " + str(char.strength))
        print("POWER: " + str(char.power))
        print("DEXTERITY: " + str(char.dexterity))
    
    def show_enemy_stats(self, char):
        print(char.name)
        print("HP: " + str(char.health))
        
    def fight_interface(self, player, encounter):
        gui.show_enemy_stats(encounter)
        print("")
        gui.show_stats(player)
        print("")
        gui.option("1", "melee attack")
        gui.option("2", "magic attack")
        gui.option("3", "range attack")
                
        
        

class Game:
    
    def __init__(self):
        self.__end = False
        global states
        states = []
    
    def get_end(self): return self.__end

    def set_end(self, booll): self.__end = booll
    
    def run(self):
        os.system("clear")
        global gui
        gui = GUI()
        states.append(MainMenu())
        self.menu_options(states[-1].update())
        states.pop()
        while self.__end == False:
            if len(states) > 0:
                states[-1].update()
                if states[-1].ending_game():
                    self.set_end(False)
                if states[-1].request_end():
                    states.pop()  
            else:
                states.append(RoomState())
        os.system("clear")
        print()
        print("THANK YOU FOR PLAYING")
        input()
    
    def menu_options(self, i):
        if i == "1":
            states.append(CharacterCreator())
            self.character_created = True
            states.pop()
        elif i == "2":
            self.__end = True
        else:
            return "invalid input"
    
class Main:

   def __init__(self):
       game = Game()
       game.run()

    
    
a=Main()
    
        