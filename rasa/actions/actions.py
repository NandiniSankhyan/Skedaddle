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
            txt = f"I understand you are in {location} and you need help with Accommodation.<br/>For Bayreuth we suggest the following places:<br/><br/>1. International Condominium<br/>2. Residential complex Am Kreuzstein<br/>3. Residential complex Studentendorf Birken<br/>4. Dormitory Adolph Kolping<br/>5. Dormitory Von-Römer-Straße<br/>6. Housing complex Am Tappert"
            A_url = ""
            A_url = f"https://www.studentenwerk-oberfranken.de/wohnen/wohnheime/bayreuth.html"
            dispatcher.utter_message(text=f"{txt}<br/>Read more about International Student Accommodation: {A_url} <br/>") 

        elif (option == "2"):
            txt = f"I understand you are in {location} and you need help with Opening a Blocked Account.<br/><br/>Proof of financial means to cover the costs for the time of your studies by one of the following documents:<br/>- confirmation of a German/EU scholarship/stipend or<br/>- “Verpflichtungserklärung” (formal obligation letter) by sponsor living in Germany or<br/>- blocked account for the first year of your stay, amounting to 10,332€<br/> <br/>Suggested blocked account providers for students: <br/>1. Expatrio<br/>2. Fintiba<br/>3. Coracle<br/>"
            BA_url = ""
            BA_url = f"hhttps://help.expatrio.com/hc/en-us/articles/360009749780"
            dispatcher.utter_message(text=f"{txt}<br/>Read more about Blocked Account: {BA_url} <br/>") 
        elif (option == "1"): 
            txt = f"I understand you are in {location} and you need help with VISA.<br/>For German National Student VISA, you will need the following documents ready on the date of appointment:<br/><br/>1. Valid Passport<br/>2. VISA Application form <br/>3. Declaration for Additional contact and legal representation information<br/>4. Statement of purpose<br/>5. Proof of admittance to the study course/college<br/>6. Certificates of other academic qualifications<br/>7. Curriculum vitae<br/>8. 3 passport pictures<br/>9. VISA Fee (75 €)<br/>10. Travel Insurance<br/>"
            VISA_url = ""
            VISA_url = f"hhttps://help.expatrio.com/hc/en-us/articles/360009749780"
            dispatcher.utter_message(text=f"{txt}<br/>Read more about VISA requirements: {VISA_url} <br/>") 
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
            txt = f"I understand you are in {location} and you need help with Health Insurance.<br/>For Students, we suggest the below two Public Insurance providers:<br/> <br/>TK (Techniker Krankenkasse)<br/>DAK (Deutsche Angestellten-Krankenkasse)<br/> "
            TK_url = ""
            TK_url = f"https://help.expatrio.com/hc/en-us/articles/115001272071"
            dispatcher.utter_message(text=f"{txt}<br/>Read more about TK Health: {TK_url} <br/>")        
        elif (option == "2"):
            txt = f"I understand you are in {location} and you need help with Opening a Bank Account in Germany.<br/>We suggest the below banks:<br/><br/>1. Commerzbank - Leading German commercial bank<br/>2. ING Bank - One of the largest banks in Germany<br/>3. Monese - Mobile only banking service based in UK<br/>4. Sparkasse - Germany’s largest credit institution<br/>5. Tomorrow - A sustainable solution for mobile banking.<br/>" 
            BANK_url = ""
            BANK_url = f"https://help.expatrio.com/hc/en-us/articles/115001475512"
            dispatcher.utter_message(text=f"{txt}<br/>Click here to know how to open a Current Bank Account in Germany: {BANK_url} <br/>")  
        elif (option == "1"): 
            txt = f"I understand you are in {location} and you need help with City Registration.<br/> <br/>Bayreuth-Anmeldung :"
            CR_url = ""
            CR_url = f"https://termine.crossing.de/446485739/Appointment/SelectDateAndTime"
            dispatcher.utter_message(text=f"{txt}<br/>Click to book your City Registration appointment: {CR_url} <br/>")