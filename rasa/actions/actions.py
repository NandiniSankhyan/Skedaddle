# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class SetLocation(Action):
    def name(self) -> Text:
        return "action_user_location_home"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("choice")
        option = tracker.get_slot("choice1")
        txt = ""
        if (option == "3"):
            txt = f"I understand you are in {location} and you need help with Accommodation.\nFor Bayreuth we suggest the following places:\n\n1. International Condominium\n2. Residential complex Am Kreuzstein\n3. Residential complex Studentendorf Birken\n4. Dormitory Adolph Kolping\n5. Dormitory Von-Römer-Straße\n6. Housing complex Am Tappert"
            A_url = ""
            A_url = f"https://www.studentenwerk-oberfranken.de/wohnen/wohnheime/bayreuth.html"
            dispatcher.utter_message(text=f"{txt}\nRead more about International Student Accommodation: {A_url} \n") 

        elif (option == "2"):
            txt = f"I understand you are in {location} and you need help with Opening a Blocked Account.\n\nProof of financial means to cover the costs for the time of your studies by one of the following documents:\n- confirmation of a German/EU scholarship/stipend or\n- “Verpflichtungserklärung” (formal obligation letter) by sponsor living in Germany or\n- blocked account for the first year of your stay, amounting to 10,332€\n \nSuggested blocked account providers for students: \n1. Expatrio\n2. Fintiba\n3. Coracle\n"
            BA_url = ""
            BA_url = f"hhttps://help.expatrio.com/hc/en-us/articles/360009749780"
            dispatcher.utter_message(text=f"{txt}\nRead more about Blocked Account: {BA_url} \n") 
        elif (option == "1"): 
            txt = f"I understand you are in {location} and you need help with VISA.\nFor German National Student VISA, you will need the following documents ready on the date of appointment:\n\n1. Valid Passport\n2. VISA Application form \n3. Declaration for Additional contact and legal representation information\n4. Statement of purpose\n5. Proof of admittance to the study course/college\n6. Certificates of other academic qualifications\n7. Curriculum vitae\n8. 3 passport pictures\n9. VISA Fee (75 €)\n10. Travel Insurance\n"
            VISA_url = ""
            VISA_url = f"hhttps://help.expatrio.com/hc/en-us/articles/360009749780"
            dispatcher.utter_message(text=f"{txt}\nRead more about VISA requirements: {VISA_url} \n") 
        else:
            txt = f"I understand you are in {location} but you entered an invalid option. Please Type 1,2 or 3."
            dispatcher.utter_message(text=txt)
        
        return []

class SetLocation(Action):
    def name(self) -> Text:
        return "action_user_location_germany"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        location = tracker.get_slot("choice")
        option = tracker.get_slot("choice1")
        txt = ""
        if (option == "3"):
            txt = f"I understand you are in {location} and you need help with Health Insurance.\nFor Students, we suggest the below two Public Insurance providers:\n \nTK (Techniker Krankenkasse)\nDAK (Deutsche Angestellten-Krankenkasse)\n "
            TK_url = ""
            TK_url = f"https://help.expatrio.com/hc/en-us/articles/115001272071"
            dispatcher.utter_message(text=f"{txt}\nRead more about TK Health: {TK_url} \n")        
        elif (option == "2"):
            txt = f"I understand you are in {location} and you need help with Opening a Bank Account in Germany.\nWe suggest the below banks:\n\n1. Commerzbank - Leading German commercial bank\n2. ING Bank - One of the largest banks in Germany\n3. Monese - Mobile only banking service based in UK\n4. Sparkasse - Germany’s largest credit institution\n5. Tomorrow - A sustainable solution for mobile banking.\n" 
            BANK_url = ""
            BANK_url = f"https://help.expatrio.com/hc/en-us/articles/115001475512"
            dispatcher.utter_message(text=f"{txt}\nClick here to know how to open a Current Bank Account in Germany: {BANK_url} \n")  
        elif (option == "1"): 
            txt = f"I understand you are in {location} and you need help with City Registration.\n \nBayreuth-Anmeldung :"
            CR_url = ""
            CR_url = f"https://termine.crossing.de/446485739/Appointment/SelectDateAndTime"
            dispatcher.utter_message(text=f"{txt}\nClick to book your City Registration appointment: {CR_url} \n")