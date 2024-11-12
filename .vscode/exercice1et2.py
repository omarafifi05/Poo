class Voiture:
    def __init__(self, marque, modele, couleur, nombre_de_places,__plaque_dimmatriculation, puissance_du_moteur):
        self.marque = marque
        self.modele = modele
        self.couleur = couleur
        self.plaque_dimmatriculation = __plaque_dimmatriculation
        self.plaque_dimmatriculation = nombre_de_places
        self.puissance_du_moteur = puissance_du_moteur

    def demmarer(self):
        print(f"La voiture {self.marque} {self.modele} num plaque {self.plaque_dimmatriculation} est demarree")
    
    def arreter (self):
        print(f"la voiture {self.marque} {self.modele} {self.plaque_dimmatriculation}  s'arrete")

    def setPlaque_dimmatriculation (self, plaque_dimmatriculation ):
        self.plaque_dimmatriculation  = plaque_dimmatriculation 

    def  getPlaque_dimmatriculation (self):
        print(f"nouveau plaque d'immatruculation est {self.plaque_dimmatriculation }")

voiture1 = Voiture("mercedes", "class g" ,  "bleu", 123456, 5, 300)
voiture2 = Voiture("mercedes", "class a" ,  "green", 1236, 5, 250)
voiture3 = Voiture("mercedes", "class s" ,  "red", 3456, 5, 200)

voiture1.setPlaque_dimmatriculation(878787)
voiture1.getPlaque_dimmatriculation()

voiture1.demmarer()
voiture2.demmarer()
voiture3.arreter()

