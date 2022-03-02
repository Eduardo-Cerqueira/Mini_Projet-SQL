# Créé par ASUS-SI, le 22/11/2020 en Python 3.7

import sqlite3
import os


def afficher(cur):
    print("-"*30)
    for i in cur.fetchall():
        enr = ""
        for j in i:
            enr+=str(j)+"\t"
        print(enr)
    print("-"*30)

def sqlClients():
    sql = "CREATE TABLE Clients "
    sql+= "( NumClient  INTEGER PRIMARY KEY AUTOINCREMENT,"
    sql+= "  Nom        TEXT    NOT NULL,"
    sql+= "  Prenom     TEXT    NOT NULL,"
    sql+= "  Adresse    TEXT    NOT NULL,"
    sql+= "  Telephone  TEXT            )"
    return sql

def sqlProduits():
    sql = "CREATE TABLE Produits "
    sql+= "( NumProduit  INTEGER PRIMARY KEY AUTOINCREMENT,"
    sql+= "  Designation TEXT    NOT NULL,"
    sql+= "  Prix        FLOAT           )"
    return sql

def sqlFactures():
    sql = "CREATE TABLE Factures "
    sql+= "( NumFacture  INTEGER PRIMARY KEY AUTOINCREMENT,"
    sql+= "  Date        DATE      NOT NULL,"
    sql+= "  NumClient   INTEGER,"
    sql+= "  FOREIGN KEY (NumClient) "
    sql+= "  REFERENCES Clients(NumClient)"
    sql+= "  ON DELETE CASCADE "
    sql+= "  ON UPDATE CASCADE)"
    return sql

def sqlAchats():
    sql = "CREATE TABLE Achats "
    sql+= "( NumFacture  INTEGER NOT NULL,"
    sql+= "  NumProduit  INTEGER NOT NULL,"
    sql+= "  Quantite    INTEGER NOT NULL,"
    sql+= "  PRIMARY KEY (NumFacture,NumProduit),"
    sql+= "  FOREIGN KEY (NumFacture) "
    sql+= "  REFERENCES Factures(NumFacture)"
    sql+= "  FOREIGN KEY (NumProduit) "
    sql+= "  REFERENCES Produits(NumProduit))"
    return sql

def sqlReglements():
    sql = "CREATE TABLE Reglements "
    sql+= "( NumReglement  INTEGER PRIMARY KEY AUTOINCREMENT,"
    sql+= "  Date          DATE    NOT NULL,"
    sql+= "  Type          TEXTE           ,"
    sql+= "  Montant       FLOAT   NOT NULL,"
    sql+= "  NumFacture    INTEGER NOT NULL,"
    sql+= "  FOREIGN KEY (NumFacture) "
    sql+= "  REFERENCES Factures(NumFacture))"
    return sql

def OuvrirBD(base):
    isExist = os.path.exists(base)
    if isExist :
        print("La base existe.")
    else:
        print("La base n'existe pas.")
        conn = sqlite3.connect(base)
        curseur = conn.cursor()
        curseur.execute("PRAGMA foreign_keys = ON")
        curseur.execute(sqlClients())
        curseur.execute(sqlProduits())
        curseur.execute(sqlFactures())
        curseur.execute(sqlAchats())
        curseur.execute(sqlReglements())
        conn.commit()
        conn.close()
        print("Elle est maintenant crée.")

def commandeSQL(base,sql):

    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    curseur.execute("PRAGMA foreign_keys = ON")
    curseur.execute(sql)
    conn.commit()
    conn.close()

#######################################################################

def AjouterClient(base):
    nom = input("Nom : ")
    prenom = input("Prenom : ")
    adresse = input("Adresse : ")
    telephone = input("Telephone : ")
    client = (nom,prenom,adresse,telephone)
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    curseur.execute("PRAGMA foreign_keys = ON")
    sql = "INSERT INTO Clients (Nom,Prenom,Adresse,Telephone)"
    sql+= "VALUES " + str(client)
    curseur.execute(sql)
    conn.commit()
    conn.close()

def ModifierClient(base):
    CLIENTCLEF = input("Rentrez le Numero de client : ")
    NOM = str(input("Rentrez le nouveau nom : "))
    PRENOM = str(input("Rentrez le nouveau prenom : "))
    ADRESSE = str(input("Rentrez le nouveau adresse : "))
    TELEPHONE = str(input("Rentrez le nouveau telephone : "))
    sql = "UPDATE Clients SET Nom = "
    sql+= "'"
    sql+= NOM
    sql+= "'"
    sql+= ", Prenom = "
    sql+= "'"
    sql+= PRENOM
    sql+= "'"
    sql+= ", Adresse = "
    sql+= "'"
    sql+= ADRESSE
    sql+= "'"
    sql+= ", Telephone = "
    sql+= "'"
    sql+= TELEPHONE
    sql+= "'"
    sql+= " WHERE NumClient = "
    sql+= CLIENTCLEF
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    curseur.execute(sql)
    conn.commit()
    conn.close()

def SupprimerClient(base):
    NUMERO = input("Numero de client : ")
    sql = "DELETE FROM Clients WHERE NumClient = "
    sql+= NUMERO
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    curseur.execute(sql)
    curseur.execute("SELECT * FROM Clients")
    conn.commit()
    conn.close()

def AfficherClients(base):
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    sql = "SELECT * FROM Clients"
    curseur.execute(sql)
    for i in curseur.fetchall():
        print (i)
    conn.commit()
    conn.close()

#######################################################################

def AfficherFactures(base):
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    sql = "SELECT * FROM Factures"
    curseur.execute(sql)
    for i in curseur.fetchall():
        print (i)
    conn.commit()
    conn.close()

def AjouterFacture(base):
    Date= input("Date : ")
    NumClient= input("Numero du client: ")
    facture = (Date,NumClient)
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    curseur.execute("PRAGMA foreign_keys = ON")
    sql = "INSERT INTO Factures (Date,NumClient)"
    sql+= "VALUES " + str(facture)
    curseur.execute(sql)
    conn.commit()
    conn.close()

def SupprimerFacture(base):
    NUMERO = input("Numero de facture : ")
    sql = "DELETE FROM Factures WHERE NumFacture = "
    sql+= NUMERO
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    curseur.execute(sql)
    curseur.execute("SELECT * FROM Factures")
    conn.commit()
    conn.close()

def ModifierFacture(base):
    nouvelle_date= input("Nouvelle date: ")
    NUMERO = input("Numero de client: ")
    sql = "UPDATE Factures SET Date = "
    sql+= "'"
    sql+= nouvelle_date
    sql+= "'"
    sql+= " WHERE NumClient ="
    sql+= NUMERO
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    curseur.execute(sql)
    curseur.execute("SELECT * FROM Factures")
    conn.commit()
    conn.close()

#######################################################################

def AjouterProduit(base):
    designation = input ("Nom du produit : ")
    prix = input ("Prix : ")
    produits = (designation,prix)
    sql = "INSERT INTO Produits (Designation,Prix)"
    sql+= "VALUES" + str(produits)
    commandeSQL(base,sql)

def AfficherProduits(base):
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    sql = "SELECT * FROM Produits"
    curseur.execute(sql)
    for i in curseur.fetchall():
        print (i)
    conn.commit()
    conn.close()

def SupprimerProduit(base):
    numero_produit = input("Numero du produit : ")
    sql = "DELETE FROM Produits WHERE NumProduit = "
    sql+=  numero_produit
    commandeSQL(base,sql)


def ModifierNomProduit(base):
        numero_produit = input("Donnez le numero du produit")
        nouveau_nom = input ("Donnez le nouveau nom")
        sql = "UPDATE Produits SET Designation = "
        sql+= "'"
        sql+= nouveau_nom
        sql+= "'"
        sql+=" WHERE NumProduit = "
        sql+= numero_produit
        commandeSQL(base,sql)


def ModifierPrixProduit(base):
        numero_produit = input("Donner le numero du produit")
        nouveau_prix = input ("Donner le nouveau prix")
        sql = "UPDATE Produits SET Prix = "
        sql+= "'"
        sql+= nouveau_prix
        sql+= "'"
        sql+=" WHERE NumProduit = "
        sql+= numero_produit
        commandeSQL(base,sql)

#######################################################################

def AjouterAchat(base):
    num_facture = input("Numero de facture: ")
    num_produit = input ("Numero du produit : ")
    quantite = input ("Quantité du produit : ")
    achat = (num_facture,num_produit,quantite)
    sql = "INSERT INTO Achats (NumFacture,NumProduit,Quantite)"
    sql+= "VALUES" + str(achat)
    commandeSQL(base,sql)

def ModifierAchat(base):
    facture = input("Numero de facture: ")
    produit = input("Numero du produit : ")
    quantite = input("Modifier la quantité du produit : ")
    sql = "UPDATE Achats SET Quantite = "
    sql+= "'"
    sql+= quantite
    sql+= "'"
    sql+= " WHERE NumFacture = "
    sql+= facture
    sql+= " AND NumProduit = "
    sql+= produit
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    curseur.execute(sql)
    curseur.execute("SELECT * FROM Factures")
    conn.commit()
    conn.close()

def SupprimerAchat(base):
    numero_facture = input("Numero de facture : ")
    numero_produit = input("Numero de produit : ")
    sql = "DELETE FROM Achats WHERE NumFacture = "
    sql+=  numero_facture
    sql+= " AND NumProduit = "
    sql+= numero_produit
    commandeSQL(base,sql)

def AfficherAchats(base):
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    sql = "SELECT * FROM Achats"
    curseur.execute(sql)
    for i in curseur.fetchall():
        print (i)
    conn.commit()
    conn.close()

#######################################################################

def AjouterReglement(base):
    num_facture = input("Numero de facture : ")
    date = input("Date de reglement : ")
    type = input("Type de reglement : ")
    montant = input("Montant à régler : ")
    client = (date,type,montant,num_facture)
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    curseur.execute("PRAGMA foreign_keys = ON")
    sql = "INSERT INTO Reglements (Date,Type,Montant,NumFacture)"
    sql+= "VALUES " + str(client)
    curseur.execute(sql)
    conn.commit()
    conn.close()

def ModifierReglement(base):
    num_facture = input("Numero de facture : ")
    date = input("Date de reglement : ")
    type = input("Type de reglement : ")
    montant = input("Modifier le montant à régler : ")
    sql = "UPDATE Reglements SET Date = "
    sql+= "'"
    sql+= date
    sql+= "'"
    sql+= ", Type = "
    sql+= "'"
    sql+= type
    sql+= "'"
    sql+= ", Montant = "
    sql+= "'"
    sql+= montant
    sql+= "'"
    sql+= " WHERE NumFacture = "
    sql+= num_facture
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    curseur.execute(sql)
    curseur.execute("SELECT * FROM Factures")
    conn.commit()
    conn.close()

def SupprimerReglement(base):
    num_facture = input("Numero de facture : ")
    sql = "DELETE FROM Reglements WHERE NumFacture = "
    sql+= num_facture
    commandeSQL(base,sql)

def AfficherReglements(base):
    conn = sqlite3.connect(base)
    curseur = conn.cursor()
    sql = "SELECT * FROM Reglements"
    curseur.execute(sql)
    for i in curseur.fetchall():
        print (i)
    conn.commit()
    conn.close()