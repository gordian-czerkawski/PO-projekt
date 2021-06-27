#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
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
    def __init__(self, name, health, strength, power, dexterity):
        super(Player, self).__init__(name, health, strength, 
                       power, dexterity)
       # self.inventory = Inventory()
        self.level = 0
        

        
class Enemy(Character):
    def __init__(self, name, description ,health, strength, power, dexterity):
        super(Enemy, self).__init__(name, health, strength, power, dexterity)
        self.description = description
        
    def get_description(self):
        return self.description

class Generator:
    def enemyGen(self):
        temp = []
        file = open("enemys.txt","r")
        lines = file.readlines()
        enemy_name = lines[random.randint(0,len(lines)-1)][:-1]
        file.close
    
    
        health = random.randint(50,100)
        attack = random.randint(1,10)
        power = random.randint(10,20)
        dexterity = random.randint(1,10)
        return Enemy(enemy_name, "", health, attack, power, dexterity)




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
    
    def request_end(self): return self.end
    
    def update(self):
        print("update")
    
    
    
class MainMenu(State):
    def __init__(self):
        super(MainMenu, self).__init__()
    def update(self):
        gui.Title()
        gui.menu_option("1", "Go to game")
        gui.menu_option("2", "Exit game")
        number = gui.get_input("")
        print(number)
        self.proccess_input(number)
        
    def proccess_input(self, inp):
        if inp == "2":
            print("a")
            self.end == True
        elif inp == "1":
            states.append(CharacterCreator())
        else:
            return "invalid input"
            
        
        
class RoomState(State):
    global states
    def __init__(self):
        super(RoomState, self).__init__()
        print("Hello from Room state")
    def update(self):
        print("update")
        
class CharacterCreator(State):
    global states
    def __init__(self):
        super(CharacterCreator, self).__init__()
        print("Hello from character creator")
    
    

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
        
        

class Game:
    
    def __init__(self):
        self.__end = False
        global states
        states = []
        characters = []
    
    def get_end(self): return self.__end

    def set_end(self, booll): self.__end = booll
    
    def run(self):
        global gui
        gui = GUI() 
        states.append(MainMenu())
        while self.__end == False:
            if len(states) > 0:
                states[-1].update()
                if states[-1].request_end():
                    states.pop()
        print("ending a game")

    
    
class Main:

   def __init__(self):
       game = Game()
       game.run()

    
    
a=Main()
    
        