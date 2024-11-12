class CompteBancaire:
    def __init__(self, __titulaire, __solde=0):
        self.titulaire = __titulaire
        self.solde = __solde

    def deposer(self, montant):
        if montant > 0:
            self.solde += montant
            print(f"solde : {self.solde}.")
        else:
            print("Le montant doit être positif.")

    def retirer(self, montant):
        if montant > 0 and montant <= self.solde:
            self.solde -= montant
            print(f"solde : {self.solde}.")
        
        else:
            print("Le montant doit être positif.")
    
    def afficher_solde(self):
        print(f"Le solde de {self.titulaire} est de {self.solde}.")



    def setTitulaire (self, titulaire):
        self.titulaire = titulaire


    def  getTitulaire (self):
        print(f"le titulaire est {self.titulaire}")

compte = CompteBancaire("Omar AFIFI", 1000)


compte.setTitulaire("Omar CASA")
compte.getTitulaire()

compte.deposer(200)  
compte.retirer(500)  
compte.afficher_solde()  
