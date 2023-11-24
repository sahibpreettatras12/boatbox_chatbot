from typing import Dict, Text, List
import re
from rasa_sdk import Tracker
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk import Action
from rasa_sdk.events import SlotSet




class Ask_boat_values(Action):
    def name(self) -> Text:
        return "action_boat_values"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        
        
        
        print(tracker.latest_message['text']) # to get user typed message
        
        last_maintainenance = tracker.latest_message['text']
        evt = SlotSet(key = "last_maintainenance", value = last_maintainenance)

        name =  tracker.slots['name']
        email =  tracker.slots['email']
        zip_code =  tracker.slots['zip_code']
        boat_manufacturer =  tracker.slots['boat_manufacturer']
        boat_model =  tracker.slots['boat_model']
        year_manufactured =  tracker.slots['year_manufactured']
        engine_manufacturer =  tracker.slots['engine_manufacturer']
        engine_model =  tracker.slots['engine_model']
        hours_on_engine =  tracker.slots['hours_on_engine']
        last_maintainenance =  tracker.slots['last_maintainenance']
        
        dispatcher.utter_message(text=f""" 
            I will remeber that your name is {name},{email} and password is in 
                                 DB and {zip_code},{boat_manufacturer},
            {boat_model},{year_manufactured},{engine_manufacturer},
            {engine_model},{hours_on_engine} and {last_maintainenance}
        """)

        return [evt]

class AskForSlotAction_last_maint(Action):
    def name(self) -> Text:
        return "action_ask_last_maintainenance"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        
        buttons=[]
        buttons.append({
            "title":"Never performed","payload":"Never performed"
        })
        buttons.append({
            "title":"Less than 50","payload":"Less than 50"
        })
        buttons.append({
            "title":"More than 50 but less than 100",
            "payload":"More than 50 but less than 100"
        })
        buttons.append({
            "title":"Over 100 hours",
            "payload":"Over 100 hours"
        })
        
        
        dispatcher.utter_message(text="pls pickup year of last maintainence",buttons=buttons)
        print(tracker.latest_message['text']) # to get user typed message
        
        hours_on_engine = tracker.latest_message['text']
        try:
            pattern = r'\b\d+\b'
            matches = re.findall(pattern, hours_on_engine)
            hours_on_engine = matches[0]
        except:
            hours_on_engine = 0
        evt = SlotSet(key = "hours_on_engine", value = hours_on_engine)

        return [evt]
    


class AskForSlotAction_engine_hours(Action):
    def name(self) -> Text:
        return "action_ask_hours_on_engine"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        
        print(tracker.latest_message['text']) # to get user typed message
        
        engine_model = tracker.latest_message['text']
        evt = SlotSet(key = "engine_model", value = engine_model)

        dispatcher.utter_message(text="what are your total engine hours")
        return [evt]
    

    
class AskForSlotAction_engine_model(Action):
    def name(self) -> Text:
        return "action_ask_engine_model"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        print(tracker)
        dispatcher.utter_message(text="can i ask for engine model")

        print(tracker.latest_message['text']) # to get user typed message
        
        engine_manufacturer = tracker.latest_message['text']
        evt = SlotSet(key = "engine_manufacturer", value = engine_manufacturer)
        return [evt]
    

class AskForSlotAction_engine_manufacturer(Action):
    def name(self) -> Text:
        return "action_ask_engine_manufacturer"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        print(tracker)
        dispatcher.utter_message(text="and I would want your engine manufacturer's name")

        print(tracker.latest_message['text']) # to get user typed message
        print("\n","Now slots value is ",tracker.slots['year_manufactured']," engine manufactured") 
        year_manufactured = tracker.latest_message['text']
        try:
            pattern = r'\b(?:20(?:0\d|1[0-9]|20|21|22))\b'
            matches = re.findall(pattern, year_manufactured)
            year_manufactured = matches[0]
        except:
            year_manufactured = 'Before 2000'
        evt = SlotSet(key = "year_manufactured", value = year_manufactured)
        return [evt]
    
class AskForSlotAction_year_manufactured(Action):
    def name(self) -> Text:
        return "action_ask_year_manufactured"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        print(tracker)
        

        dispatcher.utter_message(text="Which year your boat was manufactured?")

        print(tracker.latest_message['text']) # to get user typed message
        
        print("\n","Now slots value is ",tracker.slots['year_manufactured']," year manufactured") 
        boat_model = tracker.latest_message['text']
        evt = SlotSet(key = "boat_model", value = boat_model)
        return [evt]
    
class AskForSlotAction_boat_model(Action):
    def name(self) -> Text:
        return "action_ask_boat_model"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        print(tracker)
        dispatcher.utter_message(text="What is your boat model?")

        print(tracker.latest_message['text']) # to get user typed message
        
        boat_manufacturer = tracker.latest_message['text']
        evt = SlotSet(key = "boat_manufacturer", value = boat_manufacturer)
        return [evt]
    
class AskForSlotAction_boat_manufacturer(Action):
    def name(self) -> Text:
        return "action_ask_boat_manufacturer"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        print(tracker)
        dispatcher.utter_message(text="What is the name of your boat manufacturer?")

        print(tracker.latest_message['text']) # to get user typed message
        
        zip_code = tracker.latest_message['text']
        evt = SlotSet(key = "zip_code", value = zip_code)
        return [evt]
    
class AskForSlotAction_zip_code(Action):
    def name(self) -> Text:
        return "action_ask_zip_code"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        print(tracker)
        dispatcher.utter_message(text="What is your zip code?")

        print(tracker.latest_message['text']) # to get user typed message
        
        password = tracker.latest_message['text']
        evt = SlotSet(key = "password", value = password)
        return [evt]
    
class AskForSlotAction_password(Action):
    def name(self) -> Text:
        return "action_ask_password"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        print(tracker)
        dispatcher.utter_message(text="Please setup your passoword")

        print(tracker.latest_message['text']) # to get user typed message
        

        email = tracker.latest_message['text']

        match = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', email)
        try:
            email = match.group(0)
        except:
            email = 'Wrong-Email'
        evt = SlotSet(key = "email", value = email)
        return [evt]
    

class AskForSlotAction_email(Action):
    def name(self) -> Text:
        return "action_ask_email"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        print(tracker)
        dispatcher.utter_message(text="what is your email address")


        
        print(tracker.latest_message['text']) # to get user typed message
        
        name = tracker.latest_message['text']
        evt = SlotSet(key = "name", value = name)
        return [evt]
    
class AskForSlotAction_name(Action):
    def name(self) -> Text:
        return "action_ask_name"

    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        print(tracker)
        dispatcher.utter_message(text="What is your name")

        # print(tracker.latest_message['text']) # to get user typed message
        
        # name = tracker.latest_message['text']
        # evt = SlotSet(key = "name", value = name)
        return []