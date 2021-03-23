#!/usr/bin/python3

# This is the main fucntion
def main():
    # A dictionary containing all the symptoms the user will type in
    symptoms = ["cough", "sneezing", "congestion", "fever", "sore_throat", 
    "shortness_of_breath", "chest_pain", "wheezing", "fatigue", "chest_discomfort",
     "headache", "messed_urination_cycle", "stomach_pain", "unexplained_bleeding",
      "hallucinations", "anxiety", "hydrophobia", "hoarseness", "loss_appetite", 
      "numbness", "trouble_walking", "confusion", "lost_of_scent"]
    
    # The dictionary that will contain all the possible diseases with their symtoms
    diseases = {
    'common_cold': ('cough', 'congestion', 'sneezing'), 
    'flu': ('cough', 'fever', 'sore_throat'),
    'asthma': ('shortness_of_breath', 'chest_pain', 'wheezing'),
    'bronchitis': ('fatigue', 'cough', 'chest_discomfort'),
    'covid_19': ('cough', 'headache', 'fever', 'lost_of_scent'),
    'diabetes': ('fatigue', 'high_hunger', 'messed_urnination_cycle'),
    'ebola': ('fever', 'stomach_pain', 'unexplained_bleeding'),
    'rabies': ('hallucinations', 'anxiety', 'hydrophobia'),
    'lung_cancer': ('hoarseness', 'loss_appetite', 'cough', "shortness_of_breath"),
    'stroke': ('numbness', 'trouble_walking', 'confusion')}
    
    # Get's the symptoms(s) the user is experiecing, or list's all the symptoms
    user_symptoms = input('What symptom(s) are you experiencing, seperate symptoms with "," type sym to list possible symptoms: ')
    
    # prints out all available symptoms in an organized format
    if user_symptoms == "sym": 
        for sym in symptoms:
            print("{}, ".format(sym))
            
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

    diseases = []
    for user_symp in symptoms_list:
        for disease in diseases:
            if user_symp.replace(" ", "") in diseases[disease]:
                diseases.append(disease)
    

    print(diseases)
main()