from tkinter import *
from tkinter import messagebox
from tkinter import messagebox
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
# class Metier:
#     def __init__(self, intitule):
#         self.intitule = intitule
#         self.independants = []

#     def ajouter_independant(self, independant_id):
#         if independant_id not in self.independants:
#             self.independants.append(independant_id)

#     def supprimer_independant(self, independant_id):
#         if independant_id in self.independants:
#             self.independants.remove(independant_id)

#     def get_intitule(self):
#         return self.intitule

#     def set_intitule(self, intitule):
#         self.intitule = intitule

#     def get_independants(self):
#         return self.independants

#     def nombre_independants(self):
#         return len(self.independants)

#     def __str__(self):
#         return f"Métier: {self.intitule}, Indépendants: {self.independants}"


# class Independant:
#     independants = []

#     def __init__(self, identifiant, nom, prenom, nom_societe, codepostal, email, metier):
#         self.identifiant = identifiant
#         self.nom = nom
#         self.prenom = prenom
#         self.nom_societe = nom_societe
#         self.codepostal = codepostal
#         self.email = email
#         self.metier = metier
#         metier.ajouter_independant(identifiant)
#         Independant.independants.append(self)

#     def get_identifiant(self):
#         return self.identifiant

#     def set_identifiant(self, identifiant):
#         self.identifiant = identifiant

#     def get_nom(self):
#         return self.nom

#     def set_nom(self, nom):
#         self.nom = nom

#     def get_prenom(self):
#         return self.prenom

#     def set_prenom(self, prenom):
#         self.prenom = prenom

#     def get_nom_societe(self):
#         return self.nom_societe

#     def set_nom_societe(self, nom_societe):
#         self.nom_societe = nom_societe

#     def get_codepostal(self):
#         return self.codepostal

#     def set_codepostal(self, codepostal):
#         self.codepostal = codepostal

#     def get_email(self):
#         return self.email

#     def set_email(self, email):
#         self.email = email

#     def get_metier(self):
#         return self.metier

#     def set_metier(self, metier):
#         self.metier = metier

#     @staticmethod
#     def emails_par_specialite_et_codepostal(specialite, codepostal):
#         return [ind.email for ind in Independant.independants if ind.metier.intitule == specialite and ind.codepostal == codepostal]

#     @staticmethod
#     def nombre_par_specialite_et_codepostal(specialite, codepostal):
#         return sum(1 for ind in Independant.independants if ind.metier.intitule == specialite and ind.codepostal == codepostal)

#     def __str__(self):
#         return f"Indépendant: {self.identifiant}, Nom: {self.nom}, Prénom: {self.prenom}, Société: {self.nom_societe}, Codepostal: {self.codepostal}, Email: {self.email}, Métier: {self.metier.intitule}"






# # D'abord, je vais créer les classes selon le diagramme d'héritage fourni.

# from datetime import date
# import tkinter

# class Client:
#     def __init__(self, nom, adresse):
#         self.nom = nom
#         self.adresse = adresse
    
#     def contacter(self):
#         return f"Contacting {self.nom} at {self.adresse}"
    
#     def __str__(self):
#         return f"Client: {self.nom}, Adresse: {self.adresse}"




# class PersonneMorale(Client):
#     def __init__(self, nom, adresse, nom_contact, limite_credit):
#         super().__init__(nom, adresse)
#         self.nom_contact = nom_contact
#         self.limite_credit = limite_credit
    
#     def editerFactureMensuelle(self, montant):
#         if montant <= self.limite_credit:
#             return f"Facture de {montant} pour {self.nom} (Contact: {self.nom_contact}) éditée avec succès."
#         else:
#             return "Crédit insuffisant pour éditer la facture."
    
#     def __str__(self):
#         return f"Personne Morale: {self.nom}, Contact: {self.nom_contact}, Limite de Crédit: {self.limite_credit}"





# class PersonnePhysique(Client):
#     def __init__(self, nom, adresse, numero_carte_credit):
#         super().__init__(nom, adresse)
#         self.numero_carte_credit = numero_carte_credit
    
#     def __str__(self):
#         return f"Personne Physique: {self.nom}, Numéro de Carte de Crédit: {self.numero_carte_credit}"




# # Création des instances de Client, PersonneMorale et PersonnePhysique
# client1 = Client("Enterprise Inc", "123 Business Rd")
# client2 = PersonneMorale("Solutions Ltd", "456 Enterprise Blvd", "John Doe", 50000.0)
# client3 = PersonnePhysique("Jane Smith", "789 Residential St", "1234-5678-9101-1121")

# # Placement des objets dans une liste
# clients = [client1, client2, client3]




# # Affichage de chaque nom en parcourant la liste
# for client in clients:
#     print(client)



# # Création de la classe Commande avec la méthode __add__
# class Commande:
#     def __init__(self, date, numero, prix):
#         self.date = date
#         self.numero = numero
#         self.prix = prix
    
#     def acquitter(self):
#         return f"Commande {self.numero} acquittée."
    
#     def __add__(self, other):
#         if isinstance(other, Commande):
#             new_numero = f"{self.numero}-{other.numero}"
#             new_prix = self.prix + other.prix
#             return Commande(date.today(), new_numero, new_prix)
#         else:
#             return NotImplemented
    
#     def __str__(self):
#         return f"Commande: {self.numero}, Date: {self.date}, Prix: {self.prix}"



# # Test de la méthode __add__
# c1 = Commande(date.today(), "001", 100.0)
# c2 = Commande(date.today(), "002", 200.0)
# c3 = c1.__add__(c2)
# print(c3)


# c4 = c1 + c2
# print(c4)

#-----------------S8.1-----------------
# fenetre = Tk()

# fenetre.title("Mon logiciel")
# fenetre.configure(background='light green')

# label_identifiant = Label(fenetre, text='Identifiant')
# label_identifiant.grid(row=0, column=0, padx=10, pady=10)
# entry_identifiant = Entry(fenetre)
# entry_identifiant.grid(row=0, column=1, padx=10, pady=10)

# label_mot_de_passe = Label(fenetre, text='Mot de passe')
# label_mot_de_passe.grid(row=1, column=0, padx=10, pady=10)
# entry_mot_de_passe = Entry(fenetre, show='*')
# entry_mot_de_passe.grid(row=1, column=1, padx=10, pady=10)

# fenetre_value = StringVar()
# fenetre_prof=Radiobutton(fenetre, text="Professeur", variable=fenetre_value, value="Professeur")
# fenetre_etudiant=Radiobutton(fenetre, text="Etudiant", variable=fenetre_value, value="Etudiant")
# fenetre_prof.grid(row=3, column= 0,pady=10)
# fenetre_etudiant.grid(row=3, column=1, pady=10)

# button_connexion = Button(fenetre, text='Connexion', bg='green', fg='white')
# button_connexion.grid(row=2, column=0, columnspan=2, pady=10)

# fenetre.mainloop()

#----------------S8.2------------------

# fenetre_couleur = Tk()

# fenetre_couleur.title("TKinter")

# fenetre_couleur.grid_columnconfigure(0, weight=1)
# fenetre_couleur.grid_columnconfigure(1, weight=1)
# fenetre_couleur.grid_rowconfigure(1, weight=1)

# label_rouge = Label(fenetre_couleur, text='Rouge', bg='red', fg='white', height=8, width=16)
# label_rouge.grid(row=0, column=0)

# button_fermer = Button(text='FERMER', command=quit)
# button_fermer.grid(row=0, column=1, sticky='ew')

# # Zone verte
# label_vert = Label(text='VERT', bg='lime green', fg='white', height=3, width=30)
# label_vert.grid(row=1, column=0, columnspan=2)

# # Zone noire
# label_noir = Label(text='NOIR', bg='black', fg='white', height=5, width=20)
# label_noir.grid(row=2, column=0)

# # Zone sapin
# label_sapin = Label(text='SAPIN', bg='springGreen4', fg='white', height=5, width=13)
# label_sapin.grid(row=2, column=1)

# # Lancement de la boucle principale
# mainloop()



#---------------S8.3-------------------

# class Compte:
#     def __init__(self, identifiant, motdepasse):
#         self._identifiant = identifiant
#         self._motdepasse = motdepasse

#     # Getter pour l'identifiant
#     @property
#     def identifiant(self):
#         return self._identifiant

#     # Setter pour l'identifiant
#     @identifiant.setter
#     def identifiant(self, value):
#         self._identifiant = value

#     # Getter pour le motdepasse
#     @property
#     def motdepasse(self):
#         return self._motdepasse

#     # Setter pour le motdepasse
#     @motdepasse.setter
#     def motdepasse(self, value):
#         self._motdepasse = value

#     # Méthode pour vérifier si le compte est valide
#     def valide(self, comptes_valides):
#         return any(c.identifiant == self._identifiant and c.motdepasse == self._motdepasse for c in comptes_valides)

# # Classe MonInterface qui hérite de Tk
# class MonInterface(Tk):
#     def __init__(self, comptes_valides):
#         super().__init__()
#         self.comptes_valides = comptes_valides
#         self.title("Mon logiciel")
#         self.configure(background='PaleGreen3')

#         # Widgets comme attributs
#         self.label_identifiant = Label(self, text='Identifiant', bg='PaleGreen3')
#         self.entry_identifiant = Entry(self)
#         self.label_mot_de_passe = Label(self, text='Mot de passe', bg='PaleGreen3')
#         self.entry_mot_de_passe = Entry(self, show='*')
#         self.button_connexion = Button(self, text='Connexion', bg='green', fg='white', command=self.verif)

#         # Placement des widgets
#         self.label_identifiant.grid(row=0, column=0, padx=10, pady=10)
#         self.entry_identifiant.grid(row=0, column=1, padx=10, pady=10)
#         self.label_mot_de_passe.grid(row=1, column=0, padx=10, pady=10)
#         self.entry_mot_de_passe.grid(row=1, column=1, padx=10, pady=10)
#         self.button_connexion.grid(row=2, column=0, columnspan=2, pady=10)

#     # Méthode pour vérifier les identifiants
#     def verif(self):
#         identifiant_saisi = self.entry_identifiant.get()
#         motdepasse_saisi = self.entry_mot_de_passe.get()
#         compte_saisi = Compte(identifiant_saisi, motdepasse_saisi)
#         if compte_saisi.valide(self.comptes_valides):
#             messagebox.showinfo("Succès", "Connecté")
#         else:
#             messagebox.showerror("Erreur", "Accès non autorisé")

# # Création de la liste des comptes valides
# comptes_valides = [
#     Compte("user1", "pass1"),
#     Compte("user2", "pass2")
# ]

# # Création et lancement de l'interface
# if __name__ == "__main__":
#     app = MonInterface(comptes_valides)
#     app.mainloop()


#---------------S8.4------------------------

# class TicTacToe(Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("Tic Tac Toe")
#         self.player_turn = StringVar(self, value="X")
#         self.buttons = [[None for _ in range(3)] for _ in range(3)]
#         self.create_widgets()



#     def create_widgets(self):
#         Label(self, text="Player 1 : X").grid(row=0, column=0, columnspan=3)
#         Label(self, text="Player 2 : O").grid(row=1, column=0, columnspan=3)

#         for i in range(3):
#             for j in range(3):
#                 btn = Button(self, text="", width=10, height=3,
#                                 command=lambda row=i, col=j: self.make_move(row, col))
#                 btn.grid(row=i+2, column=j)
#                 self.buttons[i][j] = btn



#     def make_move(self, row, col):
#         current_text = self.buttons[row][col]['text']
#         if current_text == "" and self.player_turn.get() == "X":
#             self.buttons[row][col].configure(text="X")
#             self.player_turn.set("O")
#         elif current_text == "" and self.player_turn.get() == "O":
#             self.buttons[row][col].configure(text="O")
#             self.player_turn.set("X")
#         self.check_winner()

#     def check_winner(self):
#         # Add the logic to check for a winning combination
#         pass

# if __name__ == "__main__":
#     game = TicTacToe()
#     game.mainloop()




class Compte:
    def __init__(self, identifiant, motdepasse):
        self._identifiant = identifiant
        self._motdepasse = motdepasse

    @property
    def identifiant(self):
        return self._identifiant

    @identifiant.setter
    def identifiant(self, value):
        self._identifiant = value

    @property
    def motdepasse(self):
        return self._motdepasse

    @motdepasse.setter
    def motdepasse(self, value):
        self._motdepasse = value

    def valide(self):
        # Supposons que valid_accounts est une liste de Compte, vous pourriez alors vérifier
        global valid_accounts
        return any(account.identifiant == self._identifiant and account.motdepasse == self._motdepasse for account in valid_accounts)

# Classe SEOAnalyzer pour analyser le SEO d'une page web
class SEOAnalyzer:
    def __init__(self, url, keywords):
        self.url = url
        self.keywords = keywords
        self.soup = None
        self.external_links_count = 0
        self.internal_links_count = 0
        self.alt_tags_percentage = 0
        self.keywords_found = []
        self.report = None

    def fetch_page(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Cela va lancer une exception si le status n'est pas 200
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            messagebox.showerror("Error", f"An error occurred while fetching the page: {e}")

    def count_links(self):
        if self.soup is None:
            return
        parsed_uri = urlparse(self.url)
        base_domain = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
        
        for link in self.soup.find_all('a', href=True):
            if link['href'].startswith(base_domain) or link['href'].startswith('/'):
                self.internal_links_count += 1
            else:
                self.external_links_count += 1

    def calculate_alt_tags(self):
        images = self.soup.find_all('img')
        images_with_alt = [img for img in images if img.get('alt')]
        if images:
            self.alt_tags_percentage = (len(images_with_alt) / len(images)) * 100

    def analyze_keywords(self):
        text = self.soup.get_text().lower()
        for keyword in self.keywords:
            if keyword.lower() in text:
                self.keywords_found.append(keyword)

    def analyze(self):
        self.fetch_page()
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Cela va lancer une exception si le status n'est pas 200
            self.soup = BeautifulSoup(response.text, 'html.parser')
        except requests.RequestException as e:
            messagebox.showerror("Error", f"An error occurred while fetching the page: {e}")
            self.soup = None
        
        
    def get_report(self):
        return self.report


# Interface utilisateur principale pour saisir les informations et lancer l'analyse
class MainUI(Tk):
    def __init__(self):
        super().__init__()
        self.title("SEO Analyzer")
        self.geometry("400x300")
        self.analyzer = None
        self.create_widgets()

    def create_widgets(self):
        Label(self, text="URL:").pack()
        self.url_entry = Entry(self, width=50)
        self.url_entry.pack()

        Label(self, text="Keywords (comma-separated):").pack()
        self.keywords_entry = Entry(self, width=50)
        self.keywords_entry.pack()

        analyze_button = Button(self, text="Analyze", command=self.launch_analysis)
        analyze_button.pack()

    def launch_analysis(self):
        url = self.url_entry.get()
        keywords = [kw.strip() for kw in self.keywords_entry.get().split(',')]
        self.analyzer = SEOAnalyzer(url, keywords)
        self.analyzer.analyze()
        self.show_report()

    def show_report(self):
        report_ui = ReportUI(self.analyzer)
        report_ui.mainloop()

# Separate class for the report UI
class ReportUI(Toplevel):
    def __init__(self, analyzer):
        super().__init__()
        self.title("SEO Report")
        self.analyzer = analyzer
        self.create_widgets()

    def create_widgets(self):
        report = f"External Links: {self.analyzer.external_links_count}\n"
        report += f"Internal Links: {self.analyzer.internal_links_count}\n"
        report += f"Alt Tags Percentage: {self.analyzer.alt_tags_percentage}%\n"
        report += f"Keywords Found: {', '.join(self.analyzer.keywords_found)}"
        Label(self, text=report).pack(padx=10, pady=10)

if __name__ == "__main__":
    valid_accounts = [Compte('user1', 'pass1'), Compte('user2', 'pass2')]
    app = MainUI()
    app.mainloop()
