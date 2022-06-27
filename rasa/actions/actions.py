from typing import Dict, Text, List
import random
import urllib

from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
from rasa_sdk.events import SlotSet, AllSlotsReset

class ProposeFood(Action):
    def name(self) -> Text:
        return "action_propose_food"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        cuisine = tracker.get_slot("cuisine")

        # Some mocked data here, normally you would call a database, or make an API call to retrieve data
        asian_food = ['Gyozas', 'Pho', 'Ramen', 'Sushi', 'Takoyaki']
        french_food = ['Souffle', 'Creme Brulee', 'Ratatouille', 'Rillettes']
        german_food = ['Kässpatzen', 'Schweinsbraten', 'Knödel', 'Maultaschen']
        indian_food = ['Butter Chicken', 'Naan', 'Palak Paneer']
        italian_food = ['Spaghetti Carbonara', 'Minestrone', 'Pizza', 'Osso Buco']

        food = "Pasta"

        if (cuisine == "Asian"):
            food = random.choice(asian_food)
        elif (cuisine == "French"):
            food = random.choice(french_food)
        elif (cuisine == "German"):
            food = random.choice(german_food)
        elif (cuisine == "Indian"):
            food = random.choice(indian_food)
        elif (cuisine == "Italian"):
            food = random.choice(italian_food)

        return[SlotSet("food", food)]

class SendRecipe(Action):
    def name(self) -> Text:
        return "action_send_recipe"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        food = tracker.get_slot("food")
        food_url = ""
        encoded_food = urllib.parse.quote(food)
        food_url = f"https://www.chefkoch.de/rs/s0/{encoded_food}/Rezepte.html"
        dispatcher.utter_message(text=f"Here are some {food} recipes: {food_url}")
        return []

class ProposeFoodPlace(Action):
    def name(self) -> Text:
        return "action_propose_food_place"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        address = tracker.get_slot("address")
        # We use the address input directly. In a real application we would check the validity first
        encoded_address = urllib.parse.quote(address)
        food_place_url = f"https://www.google.com/maps/search/food+place+near+{encoded_address}"
        dispatcher.utter_message(text=f"Here is a food place near you: {food_place_url}")
        return []

class ResetSlots(Action):
    def name(self) -> Text:
        return "action_reset_all_slots"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return[AllSlotsReset()]