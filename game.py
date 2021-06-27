#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 18:28:22 2021

@author: admin
"""
import random

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
    
My_gen = Generator()
en1 = My_gen.enemyGen()



class Game:
    
    def __init__(self):
        self.end = False
    
    def run(self):
        print("aaa")
        while self.end == False:
            print("a")
        print
    
class Main:

   def __init__(self):
       print("aa")
       game = Game()
       game.run()

    
    
Main()
    
        