#!/usr/bin/python3
def main():
    Symp = input("Name your symptoms ==>")

    if Symp == "cough":
        print("You might have the symptoms for a Chronic Cough")
        print("Try getting medications like Antihistamines or Decongestants")
        print("get better soon")
        main()

    elif Symp == "sneezing":
        print("You might have the symptoms for a common cold")
        print("Try taking Acetaminophen like Tylenol and Ibuprofen like Advil to help make you feel better")
        print("get better soon")
        main()





main()