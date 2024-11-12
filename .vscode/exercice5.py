class User:
    def __init__(self , first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def se_connecter(self):
        print(f"hi,{self.first_name} {self.last_name} you are an user")

class Admin(User):
    
    def gerer_utilisateur(self):
        print(f"hi,{self.first_name} {self.last_name} you are an admin")

user = User("Omar","Afifi")
admin = Admin("ramo","fifia")

user.se_connecter()
admin.se_connecter()
admin.gerer_utilisateur()


