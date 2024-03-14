from datetime import datetime
# Création de la casse Customer (client)
class Customer:
    def __init__(self, name, birthday, phone_number):
        self.name = name
        self.birthday = birthday
        self.phone_number = phone_number
        self.bill = 0
    def getName(self):
        return self.name
    def getBirthday(self):
        return self.birthday
    def getPhoneNumber(self):
        return self.phone_number
    def getBill(self):
        return self.bill
    
# Créaton de la classe GererClients qui gère les clients
class GererClients(Customer):
    def __init__(self):
        self.customers = []
    def setName(self, newName):
        self.name = newName
    def setBirthDay(self, newdate):
        self.birthday = newdate
    def setPhoneNumber(self, newTel):
        self.phone_number = newTel
    def setbill(self, newFact):
        self.bill = newFact

    def add_customer(self, customer):
        self.customers.append(customer)

# Importation du fichier cdr et conversion
class ImportCDR:
    def __init__(self, file_path):
        self.cdr_data = []
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().split('|')
                cdr_dict = {
                    'Identifiant': int(data[0]),
                    'Type call': int(data[1]),
                    'Date et heure': datetime.strptime(data[2], '%Y%m%d%H%M%S'),
                    'Appelant': data[3],
                    'Appelé': data[4],
                    'Durée': int(data[5]),
                    'Taxe': int(data[6]),
                    'TotalVolume': int(data[7])
                }
                self.cdr_data.append(cdr_dict)

class BillGeneration:
    def __init__(self, customer, cdr_data):
        self.customer = customer
        self.cdr_data = cdr_data

    def bill_generation(self):
        for cdr in self.cdr_data:
            if cdr['Type call'] == 0:  # Appel
                if cdr['Appelant'][:3] == cdr['Appelé'][:3]:  # Même réseau
                    mybill = cdr['Durée'] * 0.025
                    if cdr['Taxe']== 0: #0 : Aucune taxe
                        self.customer.bill += mybill                       
                    elif cdr['Taxe'] == 1: # Appliquer l'ACCISE 10%
                        self.customer.bill += (mybill + (mybill * 0.1))
                    elif cdr['Taxe'] == 2: # Appliquer la TVA 16%
                        self.customer.bill += (mybill + (mybill * 0.16))                        
                else:
                    mybill += cdr['Durée'] * 0.05
                    if cdr['Taxe']== 0: #0 : Aucune taxe
                        self.customer.bill += mybill                        
                    elif cdr['Taxe'] == 1: # Appliquer l'ACCISE 10%
                        self.customer.bill += (mybill + (mybill * 0.1))
                    elif cdr['Taxe'] == 2: # Appliquer la TVA 16%
                        self.customer.bill += (mybill + (mybill * 0.16))
            elif cdr['Type call'] == 1:  # SMS
                if cdr['Appelant'][:3] == cdr['Appelé'][:3]:  # Même réseau
                    mybill = 0.001
                    if cdr['Taxe']== 0: #0 : Aucune taxe
                        self.customer.bill += mybill                       
                    elif cdr['Taxe'] == 1: # Appliquer l'ACCISE 10%
                        self.customer.bill += (mybill + (mybill * 0.1))
                    elif cdr['Taxe'] == 2: # Appliquer la TVA 16%
                        self.customer.bill += (mybill + (mybill * 0.16))
                else:
                    mybill = 0.002
                    if cdr['Taxe']== 0: #0 : Aucune taxe
                        self.customer.bill += mybill                        
                    elif cdr['Taxe'] == 1: # Appliquer l'ACCISE 10%
                        self.customer.bill += (mybill + (mybill * 0.1))
                    elif cdr['Taxe'] == 2: # Appliquer la TVA 16%
                        self.customer.bill += (mybill + (mybill * 0.16))                    
            elif cdr['Type call'] == 2:  # Internet
                mybill = cdr['TotalVolume'] * 0.03
                if cdr['Taxe']== 0: #0 : Aucune taxe
                    self.customer.bill += mybill                        
                elif cdr['Taxe'] == 1: # Appliquer l'ACCISE 10%
                    self.customer.bill += (mybill + (mybill * 0.1))
                elif cdr['Taxe'] == 2: # Appliquer la TVA 16%
                    self.customer.bill += (mybill + (mybill * 0.16))

class Stats:
    def __init__(self, cdr_data):
        self.cdr_data = cdr_data

    def calcul_stats(self):
        appels = sum(1 for cdr in self.cdr_data if cdr['Type call'] == 0)
        duree_appels = sum(cdr['Durée'] for cdr in self.cdr_data if cdr['Type call'] == 0)
        nb_sms = sum(1 for cdr in self.cdr_data if cdr['Type call'] == 1)
        volume_internet = sum(cdr['TotalVolume'] for cdr in self.cdr_data if cdr['Type call'] == 2)
        return appels, duree_appels, nb_sms, volume_internet

# Test unitaire
print()
client_test = Customer("POLYTECHNIQUE", "2023-01-11", "243818140560, 243818140120")
cdr_import = ImportCDR("D:/3GEI/Semestre 1/Algorithmique et programmation/tp_algo-1.txt")
generer_facture = BillGeneration(client_test, cdr_import.cdr_data)
generer_facture.bill_generation()
statistiques = Stats(cdr_import.cdr_data)
appels, duree_appels, nb_sms, volume_internet = statistiques.calcul_stats()

client_test2 = Customer("POLYTECHNIQUE", "2023-01-11", "243818140560, 243818140120,")
cdr_import = ImportCDR("D:/3GEI/Semestre 1/Algorithmique et programmation/tp_algo-1.txt")
generer_facture = BillGeneration(client_test2, cdr_import.cdr_data)
generer_facture.bill_generation()
statistiques = Stats(cdr_import.cdr_data)
appels1, duree_appels1, nb_sms1, volume_internet1 = statistiques.calcul_stats()

print(f"Facture de {client_test2.name}: $",client_test2.bill + client_test.bill)
print(f"Nombre d'appels:", appels + appels1, "Durée totale des appels:", duree_appels + duree_appels1 ," secondes")
print(f"Nombre de SMS: ", nb_sms + nb_sms1)
print(f"Volume internet utilisé: ", volume_internet + volume_internet1 ,"MegaByte")
print()