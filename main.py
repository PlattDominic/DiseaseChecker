#!/usr/bin/python3

# main function that runs the main code for the application
def main():
    # A dictionary containing all the symptoms the user will type in
    symptoms = ["cough", "sneezing", "congestion", "fever", "sore throat", 
    "shortness of breath", "chest pain", "wheezing", "fatigue", "chest discomfort",
     "headache", "messed urination cycle", "stomach pain", "unexplained bleeding",
      "hallucinations", "anxiety", "hydrophobia", "hoarseness", "loss appetite", 
      "numbness", "trouble walking", "confusion", "lost of scent"]
    
    # The dictionary that will contain all the possible diseases with their symtoms
    diseases = {
    'common cold': ('cough', 'congestion', 'sneezing'), 
    'flu': ('cough', 'fever', 'sore throat'),
    'asthma': ('shortness of breath', 'chest pain', 'wheezing'),
    'bronchitis': ('fatigue', 'cough', 'chest discomfort'),
    'covid 19': ('cough', 'headache', 'fever', 'lost of scent'),
    'diabetes': ('fatigue', 'high hunger', 'messed urnination cycle'),
    'ebola': ('fever', 'stomach pain', 'unexplained bleeding'),
    'rabies': ('hallucinations', 'anxiety', 'hydrophobia'),
    'lung cancer': ('hoarseness', 'loss appetite', 'cough', "shortness of breath"),
    'stroke': ('numbness', 'trouble walking', 'confusion')}
    
    # Get's the symptoms(s) the user is experiecing, or list's all the symptoms
    user_symptoms = input('What symptom(s) are you experiencing, seperate symptoms with "," type sym to list possible symptoms: ')
    
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
            main()
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
        print("this is a test")
        main()

    #Converts a set into a list, so the daya can be indexed
    #And also prints out what disease the user might have
    set_convert = list(duplicate_diseases)
    print("A possible disease you might have: {}".format(set_convert[0]))


# If the user wants to go again this will make it restart the program
# But if not it will give them a nice sending message
def Go_Again():
    again = input("Would you like to name more symptoms?")
    if again == "yes":
        main()
    elif again == "no":
        print("Feel better soon!")

    
    
main()
Go_Again()