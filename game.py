#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import time
import os

class Character:
    
    def __init__(self, name, health, strength, power, dexterity, defence):
         self.name = name
         self.health = health
         self.strength = strength
         self.power = power
         self.dexterity = dexterity
         self.defence = defence
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
    
    def increase_level(self, p):
        self.level += p
     
    def set_health(self, nh):
        self.health = nh
    
    def set_strength(self, ns):
        self.strength = ns
    
    def set_power(self, np):
        self.power = np
    
    def set_dexterity(self, nd):
        self.dexterity = nd
        
    
         
class Player(Character):
    def __init__(self, name, health, strength, power, dexterity, defence):
        super(Player, self).__init__(name, health, strength, 
                       power, dexterity, defence)
       # self.inventory = Inventory()
        self.level = 0
        

        
class Enemy(Character):
    def __init__(self, name ,health, strength, power, dexterity, defence):
        super(Enemy, self).__init__(name, health, strength, power, dexterity, defence)
        

class Generator:
    def enemyGen(self):
        temp = []
        file = open("enemys.txt","r")
        lines = file.readlines()
        enemy_name = lines[random.randint(0,len(lines)-1)][:-1]
        file.close
    
    
        health = random.randint(1,5)
        attack = random.randint(10,60)
        power = random.randint(10,60)
        dexterity = random.randint(1,60)
        defence = random.randint(1,60) 
        return Enemy(enemy_name, health, attack, power, dexterity, defence)




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
    
    def update(self):
        print("update")

    
    
    
class MainMenu(State):
    def __init__(self):
        super(MainMenu, self).__init__()
        self.character_created = False
    def update(self):
        while not self.character_created:
            gui.Title()
            gui.menu_option("0", "Create character")
            gui.menu_option("2", "Exit game")
            number = gui.get_input("")
            print(number)
            self.proccess_input(number)
        os.system("clear")
        gui.Title()
        gui.menu_option("1", "Go to game")
        gui.menu_option("2", "Exit game")
        number = gui.get_input("")
        print(number)
        self.proccess_input(number)
        
    def proccess_input(self, inp):
        if inp == "1":
            states.append(RoomState())
        elif inp == "0":
            print("aaaa")
            states.append(CharacterCreator())
            self.character_created = True
        elif inp == "2":
            self.ending_game()
        else:
            return "invalid input"
        
            
        
        
class RoomState(State):
    def __init__(self):
        super(RoomState, self).__init__()
    def update(self):
        encounter = generator.enemyGen()
        gui.enter_room(encounter)
        states.append(FightState(encounter))
        
        
class FightState(State):
    def __init__(self, encounter):
        super(FightState, self).__init__()
        self.encounter = encounter
    def update(self):
        global player
        gui.show_stats(player)
        gui.show_stats(self.encounter)
        input("")
        
class CharacterCreator(State):
    global player
    def __init__(self):
        super(CharacterCreator, self).__init__()
        print("Hello from character creator")
        self.update()
    def update(self):
        print("pdssfdfsd")
        while True:
            gui.fighters()
            fighter = gui.get_input("Choose your fighter ").lower()
            if fighter == "wizard":
                player = Player("wizard", 7, 40, 60, 50, 45)
                break
            elif fighter == "knight":
                player = Player("knight", 7, 50, 40, 40, 50)
                break
            elif fighter == "barbarian":
                player = Player("barbarian", 7, 60, 40, 50, 40)
                break
            elif fighter == "rogue": 
                player = Player("rogue", 7, 40, 60, 50, 45)
                break
        self.request_end()

        

    
    

class GUI:
    def Title(self):
        print("=====WELCOME=====")
        print("       TO A")
        print("     RPG_GAME\n")
    def menu_option(self, i, option):
        print(f"- {i} -> " + option)
        
    def get_input(self, i):
        j = input(i + " ----> ")
        return j
    
    def fighters(self):
        os.system("clear")
        print("                    AVAIBLE FIGHTERS\n  ")
        print("             WIZARD|KNIGHT|BARBARIAN|ROGUE ")
        print("STRENGTH:       35 |  50  |   60    | 40   ")
        print("POWER:          60 |  40  |   30    | 35   ")
        print("DEFENCE:        35 |  60  |   35    | 35   ")
        print("DEXTERITY:      40 |  30  |   40    | 60   ")
        print("\n")
    
    def enter_room(self, encounter):
        os.system("clear")
        time.sleep(1)
        print("You are entering a room...\n")
        time.sleep(2)
        print("The door are closing behind you...\n")
        time.sleep(2)
        if str(type(encounter)) == "<class '__main__.Enemy'>":
            print("There is a " + encounter.get_name() + " in front of you.\n")
            time.sleep(1)
            print("Get ready to fight\n")
        else:
            print("Your luck's in!")
            print(type(encounter))
            time.sleep(1)
            print("You found a " + encounter.get_name())
    
    def show_stats(self, char):
        print(char.name)
        print("STRENGTH: " + char.strength)
        print("POWER: " + char.power)
        print("DEFENCE: " + char.defence)
        print("DEXTERITY: " + char.dexterity)
                
        
        

class Game:
    
    def __init__(self):
        self.__end = False
        global states
        states = []
        characters = []
    
    def get_end(self): return self.__end

    def set_end(self, booll): self.__end = booll
    
    def run(self):
        os.system("clear")
        global gui
        global generator
        generator = Generator()
        gui = GUI() 
        states.append(MainMenu())
        while self.__end == False:
            if len(states) > 0:
                states[-1].update()
                if states[-1].request_end():
                    states.pop()
            elif states[-1].end_game():
                    break    
            else:
                states.append(RoomState())
        print("THANK YOU FOR PLAYING")

    
    
class Main:

   def __init__(self):
       game = Game()
       game.run()

    
    
a=Main()
    
        