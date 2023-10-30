from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk import Tracker
import requests
import random

# Action to provide the cultivation steps
class ActionProvideCultivationSteps(Action):
    def name(self) -> Text:
        return "action_provide_cultivation_steps"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        cultivation_steps = """
        Here are the basic steps for banana cultivation:
        1. Choose the right banana variety.
        2. Prepare the soil and plant the banana sucker.
        3. Provide adequate water and nutrients.
        4. Control pests and diseases.
        5. Harvest ripe bananas.
        """
        dispatcher.utter_message(cultivation_steps)
        return []

# Action to provide the disease prevention methods
class ActionProvideDiseasePrevention(Action):
    def name(self) -> Text:
        return "action_provide_disease_prevention"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        disease_prevention_tips = """
        To prevent banana diseases, you can:
        1. Keep the area clean and free of debris.
        2. Use disease-resistant banana varieties.
        3. Apply appropriate fungicides when necessary.
        """
        dispatcher.utter_message(disease_prevention_tips)
        return []

# Action to provide the banana diseases
class ActionProvideBananaDiseases(Action):
    def name(self) -> Text:
        return "utter_provide_banana_diseases"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        banana_diseases = """
        Here are some common banana diseases:
        1. Panama Disease (Tropical Race 4)
        2. Black Sigatoka
        3. Anthracnose
        4. Banana Bunchy Top Virus
        5. Fusarium Wilt
        """
        dispatcher.utter_message(text=banana_diseases)
        return []	

# Action to provide the thank you
class ActionThankYou(Action):
    def name(self) -> Text:
        return "action_thank_you"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message("You're welcome! If you have more questions or need further assistance, feel free to ask.")
        return []

# Action to predict Cordana
class ActionDiseasePredictionC(Action):
    def name(self) -> Text:
        return "action_disease_prediction"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        symptoms = tracker.latest_message.get("text").lower()

        if "circular spots" in symptoms and "dark brown margins" in symptoms and "light gray centers" in symptoms:
            dispatcher.utter_message("Based on the symptoms, it appears to be Cordana disease.")
        else:
            dispatcher.utter_message("I'm sorry, I couldn't determine the disease from the symptoms you mentioned.")

        return []

# Action to predict Sigatoka    
class ActionDiseasePredictionS(Action):
    def name(self) -> Text:
        return "action_disease_prediction"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Predict the disease based on symptoms
        predicted_disease = "Black Sigatoka (Black Leaf Streak)"
        dispatcher.utter_message("Based on the symptoms, it appears to be {predicted_disease}.")
        return []

# Action to predict Anthracnose
class ActionDiseasePredictionA(Action):
    def name(self) -> Text:
        return "action_disease_prediction"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Predict the disease based on symptoms
        predicted_disease = "Anthracnose"
        dispatcher.utter_message("Based on the symptoms, it appears to be {predicted_disease}.")
        return []
    
# Action to predict Crown Rot
class ActionDiseasePredictionCr(Action):
    def name(self) -> Text:
        return "action_disease_prediction"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        # Predict the disease based on symptoms
        predicted_disease = "Crown Rot"
        dispatcher.utter_message("Based on the symptoms, it appears to be {predicted_disease}.")
        return []
    
# Action to provide the cordana diseases symptoms
class ActionProvideCDiseases(Action):
    def name(self) -> Text:
        return "utter_cordana_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        banana_diseases = """
        Cordana (Cordana Leaf Spot) symptoms:
        1. Leaf Spots: Circular to elliptical spots with dark brown margins and light gray centers may appear on the leaves. These spots are typically between 1 to 3 centimeters in diameter.
        2. Streaks: In some cases, long, dark streaks may develop along the leaves, often following the veins.
        3. Concentric Rings: Concentric rings can be seen within the spots on the leaves.
        4. Leaf Death: As the disease progresses, the leaves can die and wither, leading to reduced photosynthesis and ultimately affecting the overall health of the plant.
        """
        dispatcher.utter_message(text=banana_diseases)
        return []	
    
# Action to provide the Black Sigatoka diseases symptoms
class ActionProvideCDiseases(Action):
    def name(self) -> Text:
        return "utter_blacksigatoka_symptoms"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        banana_diseases = """
        Cordana (Cordana Leaf Spot) symptoms:
        1. Leaf Spots: Circular to elliptical spots with dark brown margins and light gray centers may appear on the leaves. These spots are typically between 1 to 3 centimeters in diameter.
        2. Streaks: In some cases, long, dark streaks may develop along the leaves, often following the veins.
        3. Concentric Rings: Concentric rings can be seen within the spots on the leaves.
        4. Leaf Death: As the disease progresses, the leaves can die and wither, leading to reduced photosynthesis and ultimately affecting the overall health of the plant.
        """
        dispatcher.utter_message(text=banana_diseases)
        return []