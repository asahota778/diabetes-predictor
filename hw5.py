## packages needed
import pandas as pd
import random
from abc import ABCMeta, abstractmethod
import math


###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively


class Patient:
    
    # init function
    def __init__(self, name: int, symptoms: list):
        self.name = name
        self.symptoms = symptoms
    
    
#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.


class Patient:
    
    # init function
    def __init__(self, name: int, symptoms: list):
        self.name = name
        self.symptoms = symptoms
        self.tests = {} # this dictionary will store the test names and results
        
    # test function
    def add_test(self, test_name: str, test_results: bool):
        test_name = test_name
        test_results = test_results
        self.tests[test_name] = test_results
        
        
#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and ncreases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']
        
        
class Patient:
    
    # init function
    def __init__(self, name: int, symptoms: list):
        self.name = name
        self.symptoms = symptoms
        self.tests = {} 
        
    # test function
    def add_test(self, test_name: str, test_results: bool):
        self.tests[test_name] = test_results
        
    # covid function
    def has_covid(self) -> float :
        
        if 'covid' in self.tests:
            if self.tests['covid'] == True:
                return 0.99
            else:
                return 0.01
        else:
            prob = 0.05
            sym_list = ['fever', 'cough', 'anosmia']
            
            for symptom in sym_list:
                if symptom in self.symptoms:
                    prob += 0.1
                else:
                    prob += 0
                     
        return prob
                

######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.

class Card:
    
    # init function
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value
    

# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.

        
class Card:
    
    # init function
    def __init__(self, suit: str, value: str):
        self.suit = suit
        self.value = value
        
    # type of card function
    def one_card(self):
        return f"{self.value} of {self.suit}"
    

class Deck:
    
    # init function
    def __init__(self):
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        self.cards = [Card(suit, value) for suit in suits for value in values]
       
    # random shuffle function 
    def shuffle(self):
        random.shuffle(self.cards)
        
    # draw card function
    def draw(self):
        
        if self.cards:
            card_drawn = self.cards.pop(0)
            print(f"Card drawn is : {card_drawn.one_card()}")
        else:
            print("No more cards left in deck.")
            return None
        
    
###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.


class PlaneFigure(metaclass=ABCMeta):
    
    @abstractmethod
    # define perimeter function
    def compute_perimeter(self):
        return NotImplementedError
    
    # define surface area function
    def compute_surface(self):
        return NotImplementedError
        
    
# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.


class Triangle(PlaneFigure):
    
    # init function
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h
    
    # traingle perimeter function
    def compute_perimeter(self):
        per = self.base + self.c1 + self.c2
        return per
    
    # triangle surface area function
    def compute_surface(self):
        area = (self.base * self.h) / 2
        return area 


# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.


class Rectangle(PlaneFigure):
    
    # init function
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    # rectangle perimeter function
    def compute_perimeter(self):
        per = (2 * self.a) + (2 * self.b)
        return per
    
    # rectangle surface area function
    def compute_surface(self):
        area = self.a * self.b
        return area
    

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.


class Circle(PlaneFigure):
    
    # init function
    def __init__(self, radius):
        self.radius = radius 
       
    # circle perimeter function
    def compute_perimeter(self):
        per = 2 * math.pi * self.radius
        return per
       
    # circle surface area function 
    def compute_surface(self):
        area = math.pi * (self.radius ** 2)
        return area 