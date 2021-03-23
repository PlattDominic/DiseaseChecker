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
    



main()