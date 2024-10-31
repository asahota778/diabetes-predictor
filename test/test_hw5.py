
import sys
import os

# Add the project root directory 'diabetes-predictor' to sys.path for importing modules correctly
current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir,'..'))
sys. path.append(parent_dir)

import pytest
from hw5 import Patient, Card, Deck, Triangle, Rectangle, Circle

### Test for Patient Class ###

@pytest.fixture
def patient_instance():
    return Patient(name="John Doe", symptoms=["fever", "cough"])

def test_patient_initialization(patient_instance):
    assert patient_instance.name == "John Doe"
    assert patient_instance.symptoms == ["fever", "cough"]

def test_add_test(patient_instance):
    patient_instance.add_test("COVID-19", True)
    assert patient_instance.tests["COVID-19"] is True

def test_has_covid_with_test(patient_instance):
    patient_instance.add_test("covid", True)
    assert patient_instance.has_covid() == 0.99

def test_has_covid_no_test(patient_instance):
    assert patient_instance.has_covid() == 0.25  # Base 0.05 + 0.1 each for fever and cough

### Test for Card and Deck Classes ###

def test_card_initialization():
    card = Card(suit="Hearts", value="A")
    assert card.suit == "Hearts"
    assert card.value == "A"

def test_card_one_card():
    card = Card(suit="Spades", value="K")
    assert card.one_card() == "K of Spades"

@pytest.fixture
def deck_instance():
    deck = Deck()
    deck.shuffle()
    return deck

def test_deck_initialization(deck_instance):
    assert len(deck_instance.cards) == 52

def test_deck_shuffle(deck_instance):
    initial_order = deck_instance.cards[:]
    deck_instance.shuffle()
    assert deck_instance.cards != initial_order

def test_deck_draw(deck_instance):
    initial_count = len(deck_instance.cards)
    deck_instance.draw()
    assert len(deck_instance.cards) == initial_count - 1

### Test for PlaneFigure and Its Subclasses ###

def test_triangle():
    triangle = Triangle(base=3, c1=4, c2=5, h=6)
    assert triangle.compute_perimeter() == 12
    assert triangle.compute_surface() == 9

def test_rectangle():
    rectangle = Rectangle(a=4, b=6)
    assert rectangle.compute_perimeter() == 20
    assert rectangle.compute_surface() == 24

def test_circle():
    circle = Circle(radius=3)
    assert round(circle.compute_perimeter(), 2) == 18.85  # Approximation for 2 * pi * 3
    assert round(circle.compute_surface(), 2) == 28.27  # Approximation for pi * 3^2
