class Drug():
    def __init__(self, name, dclass, dose, dtype, halflife):
        self.name = name
        self.dclass = dclass
        self.dose = int(dose)
        self.dtype = dtype
        self.halflife = int(halflife)
        

        if self.dtype == 0:
            self.dtype = "Legal"
        elif self.dtype == 1:
            self.dtype = "Prescribed"
        elif self.dtype == 2:
            self.dtype = "Illegal"
        else:
            print("Insert one of the following: 0 for Legal; 1 for Prescription; 2 for Illegal")

    def describe(self):
        print("Name: " + self.name)
        print("Class: " + self.dclass)
        print("Recommended dose: " + str(self.dose) + " mg.")
        print("Type: " + self.dtype)
        print("Half-life: " + str(self.halflife) + " hours. This means that " + str(self.name) + " will stay " + str(self.halflife * 2) + " in your body but will have effect only for " + str(self.halflife))
        return 0

    def __str__(self):
        return f"{self.name} is a {self.dclass} and it is {self.dtype}"
    
    def dosage(self):
        return f"{self.name} should be consumed in doses of {self.dose} mg"

        
def Receptors(nmda_rcpt, serotonin_rcpt, dopamine_rcpt, norepin_rcpt, gaba_rcpt, glutamate_rcpt, acetylch_rcpt, orexin_rcpt, histamine_rcpt, adeno_rcpt):

    nmda_rcpt = bool(nmda_rcpt)
    serotonin_rcpt = bool(serotonin_rcpt)
    dopamine_rcpt = bool(dopamine_rcpt)
    norepin_rcpt = bool(norepin_rcpt)
    gaba_rcpt = bool(gaba_rcpt)
    glutamate_rcpt = bool(glutamate_rcpt)
    acetylch_rcpt = bool(acetylch_rcpt)
    orexin_rcpt = bool(orexin_rcpt)
    histamine_rcpt = bool(histamine_rcpt)
    adeno_rcpt = bool(adeno_rcpt)
    
    print("Which receptors would you like to check?")
    print("0 - NMDA")
    print("1 - Serotonin")
    print("2 - Dopamine")
    print("3 - Norepinephrine")
    print("4 - GABA")
    print("5 - Glutamate")
    print("6 - Acetylcholine")
    print("7 - Orexin")
    print("8 - Histamine")
    print("9 - Adenosine")
    print("Press Enter to see all receptors")
    pressnum = input("Enter number here: ")
    
    if pressnum == "":
        return f"NMDA: {nmda_rcpt} | Serotonin: {serotonin_rcpt} | Dopamine: {dopamine_rcpt} | Norepinephrine: {norepin_rcpt} | GABA: {gaba_rcpt} | Glutamate: {glutamate_rcpt} | Acetylcholine: {acetylch_rcpt} | Orexin: {orexin_rcpt} | Histamine: {histamine_rcpt} | Adenosine: {adeno_rcpt}"
    elif pressnum == "0":
        return f"NMDA: {nmda_rcpt}"
    elif pressnum == "1": 
        return f"Serotonin: {serotonin_rcpt}"
    elif pressnum == "2": 
        return f"Dopamine: {dopamine_rcpt}"
    elif pressnum == "3": 
        return f"Norepinephrine: {norepin_rcpt}"
    elif pressnum == "4": 
        return f"GABA: {gaba_rcpt}"
    elif pressnum == "5":
        return f"Glutamate: {glutamate_rcpt}"
    elif pressnum == "6": 
        return f"Acetylcholine: {acetylch_rcpt}"
    elif pressnum == "7": 
        return f"Orexin: {orexin_rcpt}"
    elif pressnum == "8": 
        return f"Histamine: {histamine_rcpt}"
    elif pressnum == "9":
        return f"Adenosine: {adeno_rcpt}"



        
def Interact(drug1, drug2):
    if (drug1.dclass == "Stimulant") == True:
        if (drug2.dclass == "Depressant") == True:
            return f"{drug1.name} should NOT be combined with {drug2.name}"
    elif (drug2.dclass == "Depressant") == True:
        if (drug1.dclass == "Stimulant" == True):
            return f"{drug1.name} should NOT be combined with {drug2.name}"
    else: 
        return f"We don't know the interaction of {drug1.name} and {drug2.name}"
    
def ChooseDrug():
    drugname = input("What drug would you like to check? ")
    
    
    
    
        
"""
class Receptor():
    def __init__(self, drugname, nmda_rcpt, serotonin_rcpt, dopamine_rcpt, norepin_rcpt, gaba_rcpt, glutamate_rcpt, acetylch_rcpt, orexin_rcpt, histamine_rcpt, adeno_rcpt):
        self.nmda_rcpt = bool(nmda_rcpt)
        self.serotonin_rcpt = bool(serotonin_rcpt)
        self.dopamine_rcpt = bool(dopamine_rcpt)
        self.norepin_rcpt = bool(norepin_rcpt)
        self.gaba_rcpt = bool(gaba_rcpt)
        self.glutamate_rcpt = bool(glutamate_rcpt)
        self.acetylch_rcpt = bool(acetylch_rcpt)
        self.orexin_rcpt = bool(orexin_rcpt)
        self.histamine_rcpt = bool(histamine_rcpt)
        self.adeno_rcpt = bool(adeno_rcpt)
        
    def returnreceptors(self):
        return "Pharmacology of {self.name}"
        return f"NMDA: {self.nmda_rcpt}"
        return f"Serotonin: {self.serotoning_rcpt}"
        """
    
    
