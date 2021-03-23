#!/usr/bin/python3

# This is the main fucntion
def main():

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
    

main()