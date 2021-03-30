#!/usr/bin/python3
import webbrowser
import requests
import json
import platform

#This prints all the latest data about Covid-19
def print_covid_data():
    raw_data = requests.get("https://coronavirus-19-api.herokuapp.com/all")
    covid_dict_data = dict(raw_data.json())

    print("The current global Covid-19 numbers are cases: {}, deaths: {}, recovered: {}"
    .format(covid_dict_data["cases"], covid_dict_data["deaths"], covid_dict_data["recovered"]))

# this is the disease model
class disease_model:
    def __init__(self, name, symptoms, severity_level, about_link):
        self.name = name
        self.symptoms = symptoms
        self.severity_level = severity_level
        self.about_link = about_link

#This is a function that makes all the diseases print out in color based on low, medium, or high severity
def print_disease(disease):
    low_severity = '\033[32m'
    med_severity = '\033[33m'
    high_severity = '\033[31m'
    default_col = '\033[0m'

    #This prints out the disease and it's color based on the severity. 1 and 2 = green, 3 and 4 = yellow, 5 and 6 = red
    if disease.severity_level <= 2:
        print("A possible disease you might have:"+low_severity, disease.name)
    elif disease.severity_level > 2 and disease.severity_level <= 4:
        print("A possible disease you might have:"+med_severity, disease.name)
    else:
        print("A possible disease you might have:"+high_severity, disease.name)

    # This asks the user if they would to open up the website if yes then the browser would open with the website
    print(default_col+"To learn about this disease visit: {}".format(disease.about_link))
    user_choice = input("Would you like to open this link in your broswer [y or n]: ").lower()
    if user_choice == "y":
        print("Opening link...")
        webbrowser.open(disease.about_link, new=0)
        del user_choice

    # Relays a message if the user supposedly has a disease over the severity level of 4 or if they have covid-19
    if disease.name == "covid 19":
        print("\nIf you believe you have covid-19 make sure to wear a mask, stay at home, and get tested at any local hospital")
    elif disease.severity_level > 4:
        print("\nYou might have a disease that can be very serious or life threatening")
        user_choice = input("Would you like to be shown hospitals near you [y or n]: ")
        if user_choice == "y":
            webbrowser.open("https://www.google.com/maps/search/hospital/", new=0)
    



# main function that runs the main code for the application
def main(user_name):
    # A dictionary containing all the symptoms the user will type in
    symptoms = ["cough", "sneezing", "congestion", "fever", "sore_throat", 
    "shortness_of_breath", "chest_pain", "wheezing", "fatigue", "chest_discomfort",
     "headache", "messed_urination_cycle", "stomach_pain", "unexplained_bleeding",
      "hallucinations", "anxiety", "hydrophobia", "hoarseness", "loss_appetite", 
      "numbness", "trouble_walking", "confusion", "lost_of_scent", "neck_pain", 
      "numbness", "chest_pressure", "vomiting", "body_aches", "chills", "mouth_ulcers",
      "night_sweats", "spasms", "difficulty_swallowing", "muscle_stiffness", "high_hunger"]
    
    # The dictionary that will contain all the possible diseases with their symptoms
    diseases = {
    disease_model('common_cold', ('cough', 'congestion', 'sneezing'), 1, "https://www.mayoclinic.org/diseases-conditions/common-cold/symptoms-causes/syc-20351605"), 
    disease_model('flu', ('cough', 'fever', 'sore_throat'), 3, "https://www.mayoclinic.org/diseases-conditions/flu/symptoms-causes/syc-20351719"),
    disease_model('asthma', ('shortness_of_breath', 'chest_pain', 'wheezing'), 3, "https://www.mayoclinic.org/diseases-conditions/asthma/symptoms-causes/syc-20369653"),
    disease_model('bronchitis', ('fatigue', 'cough', 'chest_discomfort'), 3, "https://www.mayoclinic.org/diseases-conditions/bronchitis/symptoms-causes/syc-20355566"),
    disease_model('covid 19', ('cough', 'headache', 'fever', 'lost_of_scent'), 4, "https://www.mayoclinic.org/diseases-conditions/coronavirus/symptoms-causes/syc-20479963"),
    disease_model('diabetes', ('fatigue', 'high_hunger', 'messed_urination_cycle'), 4, "https://www.mayoclinic.org/diseases-conditions/diabetes/symptoms-causes/syc-20371444"),
    disease_model('ebola', ('fever', 'stomach_pain', 'unexplained_bleeding'), 5, "https://www.mayoclinic.org/diseases-conditions/ebola-virus/symptoms-causes/syc-20356258"),
    disease_model('rabies', ('hallucinations', 'anxiety', 'hydrophobia'), 6, "https://www.mayoclinic.org/diseases-conditions/rabies/symptoms-causes/syc-20351821"),
    disease_model('lung_cancer', ('hoarseness', 'loss_appetite', 'cough', "shortness_of_breath"), 6, "https://www.mayoclinic.org/diseases-conditions/lung-cancer/symptoms-causes/syc-20374620"),
    disease_model('stroke', ('numbness', 'trouble_walking', 'confusion'), 3, "https://www.mayoclinic.org/diseases-conditions/stroke/symptoms-causes/syc-20350113"),
    disease_model('heart_disease', ('neck_pain', 'numbness', 'chest_pressure'), 6, "https://www.mayoclinic.org/diseases-conditions/heart-disease/symptoms-causes/syc-20353118"),
    disease_model('small_pox', ('vomiting', 'fever', 'body_aches'), 4, "https://www.mayoclinic.org/diseases-conditions/smallpox/symptoms-causes/syc-20353027"),
    disease_model('hiv', ('chills', 'mouth_ulcers', 'night_sweats'), 5, "https://www.mayoclinic.org/diseases-conditions/hiv-aids/symptoms-causes/syc-20373524"),
    disease_model('tetanus', ('spasms', 'difficulty_swallowing', 'muscle_stiffness'), 5, "https://www.mayoclinic.org/diseases-conditions/tetanus/symptoms-causes/syc-20351625")}

    
    # Get's the symptoms(s) the user is experiecing, or list's all the symptoms
    user_symptoms = input("\nHello {} what symptom(s) are you experiencing, seperate symptoms with ',' type sym to list possible symptoms: ".format(user_name))
    
    # prints out all available symptoms in an organized format
    if user_symptoms == "sym": 
        for sym in symptoms:
            print("{}, ".format(sym))
        del user_symptoms
        user_symptoms = input('What symptom(s) are you experiencing, seperate symptoms with ",": ')
            
    # Stores the user symptoms into a list
    symptoms_list = user_symptoms.split(',')
    
    # Restarts the program if you write an invalid symptom
    for sym in symptoms_list:
        if sym.replace(" ", "") not in symptoms:
            print("you wrote something that's not in our list of symptoms, please try again")
            del user_symptoms
            del symptoms_list
            main(user_name)
            break 
    
    # Make a list called possible_diseases, which will store
    # Possible diseases the user might have, according from their Symptoms
    possible_diseases = []
    for user_symp in symptoms_list:
        for disease in diseases:
            if user_symp.replace(" ", "") in disease.symptoms:
                possible_diseases.append(disease)

    # Makes a set named duplicate_diseases which will store
    # Any disease in the possible_disease list that is
    # Seen more than one time. We are using a set because
    # We don't want duplicate items
    duplicate_diseases = set()
    for disease in possible_diseases:
        if possible_diseases.count(disease) > 1:
            duplicate_diseases.add(disease)
    
    # If the user types in only one symptom, it may lead to innacurate results
    #It's encouraged that the user should put two or more symptoms
    if len(duplicate_diseases) < 1:
        print("\nWe had some trouble finding a disease with your symptoms, which might lead to unaccurate results")
        print("The diseases that you might have are: ")
        for disease in possible_diseases:
            print(disease.name)
        go_again(user_name)

    #Converts a set into a list, so the data can be indexed
    #And also prints out what disease the user might have
    set_convert = list(duplicate_diseases)
    print_disease(set_convert[0])
    go_again(user_name)

# If the user wants to go again this will make it restart the program
# But if not it will give them a nice sending message
def go_again(user_name):
    again = input("\nWould you like to name more symptoms [y or n]: ").lower()
    if again == "yes" or again == "y":
        main(user_name)
    elif again == "no" or again == "n":
        print("Feel better soon!\n")
        exit()
    else:
        print("You have entered an invalid choice, please try again")
        del again
        go_again(user_name)


# The program will ask the user to input their name. This is to make it user friendly and get the program to know the user 
user_name = input("\nHello and welcome to the Disease Checker Program! We'd love to get to know you so could you please tell us your name: ")

user_choice = input("\nWould you like to see the current global numbers for covid-19 [y or n]: ").lower()
if user_choice == "y":
    print_covid_data()

main(user_name)
