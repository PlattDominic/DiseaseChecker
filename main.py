#!/usr/bin/python3

# main function that runs the main code for the application
def main(user_name):
    # A dictionary containing all the symptoms the user will type in
    symptoms = ["cough", "sneezing", "congestion", "fever", "sore_throat", 
    "shortness_of_breath", "chest_pain", "wheezing", "fatigue", "chest_discomfort",
     "headache", "messed_urination_cycle", "stomach_pain", "unexplained_bleeding",
      "hallucinations", "anxiety", "hydrophobia", "hoarseness", "loss_appetite", 
      "numbness", "trouble_walking", "confusion", "lost_of_scent"]
    
    # The dictionary that will contain all the possible diseases with their symtoms
    diseases = {
    'common cold': ('cough', 'congestion', 'sneezing'), 
    'flu': ('cough', 'fever', 'sore_throat'),
    'asthma': ('shortness_of_breath', 'chest_pain', 'wheezing'),
    'bronchitis': ('fatigue', 'cough', 'chest_discomfort'),
    'covid 19': ('cough', 'headache', 'fever', 'lost_of_scent'),
    'diabetes': ('fatigue', 'high_hunger', 'messed_urnination_cycle'),
    'ebola': ('fever', 'stomach_pain', 'unexplained_bleeding'),
    'rabies': ('hallucinations', 'anxiety', 'hydrophobia'),
    'lung cancer': ('hoarseness', 'loss_appetite', 'cough', "shortness_of_breath"),
    'stroke': ('numbness', 'trouble_walking', 'confusion')}

    
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
            if user_symp.replace(" ", "") in diseases[disease]:
                possible_diseases.append(disease)

    # Makes a set named duplicate_diseases which will store
    # Any disease in the possible_disease list that is
    # Seen more than one time. We are using a set because
    # We don't want duplicate items
    duplicate_diseases = set()
    for disease in possible_diseases:
        if possible_diseases.count(disease) > 1:
            duplicate_diseases.add(disease)
    
    if len(duplicate_diseases) < 1:
        print("\nYou only put one symptom, which might lead to unaccurate result")
        print("The diseases, that you might have, are: ", possible_diseases)
        go_again(user_name)

    #Converts a set into a list, so the data can be indexed
    #And also prints out what disease the user might have
    set_convert = list(duplicate_diseases)
    print("A possible disease you might have: {}".format(set_convert[0]))
    go_again(user_name)

# If the user wants to go again this will make it restart the program
# But if not it will give them a nice sending message
def go_again(user_name):
    again = input("\nWould you like to name more symptoms: ").lower()
    if again == "yes" or again == "y":
        main(user_name)
    elif again == "no" or again == "n":
        print("Feel better soon!")
        exit()

    


user_name = input("\nHello and welcome to the Disease Checker Program! We'd love to get to know you so could you please tell us your name: ")
main(user_name)
