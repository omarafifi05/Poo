class Animal():
    def dormir(self):  
        print("L'animal dort")
        
    def parler(self):  
        raise NotImplementedError("Cette méthode doit être implémentée par les sous-classes")


class Chien(Animal):
    def parler(self):  
        print("Wouf")


class Chat(Animal):     
    def parler(self): 
        print("Miaou")


ani = Animal()
chien1 = Chien()
chat1 = Chat()

chien1.dormir()  
chien1.parler() 
chat1.dormir()   
chat1.parler()   
