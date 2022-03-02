import BD

base = "Papeterie.db"

BD.OuvrirBD(base)

import tkinter
from tkinter import *

fenetre = tkinter.Tk()
label = Label(fenetre, text="Où allez vous :", bg="white")
label.pack()
fenetre.title("Base de données")
fenetre.config(bg = "#E7FAFC")
fenetre.geometry("640x480")
fenetre.maxsize(800,600)
fenetre.minsize(300,400)
fenetre.mainloop()

bouton1=Button(fenetre, text="Clients",)
bouton1.pack()

bouton2=Button(fenetre, text="Factures")
bouton2.pack()

bouton3=Button(fenetre, text="Produits")
bouton3.pack()

bouton4=Button(fenetre, text="Achats")
bouton4.pack()

bouton5=Button(fenetre, text="Reglement")
bouton5.pack()


if (bouton1):
    print("  1.Ajouter un client")
    print("  2.Modifier un client")
    print("  3.Supprimer un client")
    print("  4.Afficher les clients")

    commande1 = input("Que voulez vous faire :")

    if (commande1=="1"):
        BD.AjouterClient(base)

    if (commande1=="2"):
        BD.ModifierClient(base)

    if (commande1=="3"):
        BD.SupprimerClient(base)

    if (commande1=="4"):
        BD.AfficherClients(base)

if (commande=="2"):
    print("  1.Ajouter une facture")
    print("  2.Modifier une facture")
    print("  3.Supprimer une facture")
    print("  4.Afficher les factures")

    commande2 = input("Que voulez vous faire :")

    if(commande2=="1"):
        BD.AjouterFacture(base)

    if(commande2=="2"):
        BD.ModifierFacture(base)

    if(commande2=="3"):
        BD.SupprimerFacture(base)

    if (commande2=="4"):
        BD.AfficherFactures(base)

if (commande=="3"):
    print("  1.Ajouter un produit")
    print("  2.Modifier un produit")
    print("  3.Supprimer un produit")
    print("  4.Afficher les produits")

    commande3 = input("Que voulez vous faire :")

    if(commande3=="1"):
        BD.AjouterProduit(base)

    if(commande3=="2"):
        print("    1.Modifier le nom du produit")
        print("    2.Modifier le prix du produit")
        commande3_1 = input("Commande = ")

        if(commande3_1=="1"):
            BD.ModifierNomProduit(base)

        if(commande3_1=="2"):
            BD.ModifierPrixProduit(base)

    if(commande3=="3"):
        BD.SupprimerProduit(base)

    if (commande3=="4"):
        BD.AfficherProduits(base)

if (commande=="4"):
    print("  1.Ajouter un achat à une facture")
    print("  2.Modifier un achat d'une facture")
    print("  3.Supprimer un achat d'une facture")
    print("  4.Afficher les achats d'une facture")

    commande4 = input("Que voulez vous faire :")

    if(commande4=="1"):
        BD.AjouterAchat(base)

    if(commande4=="2"):
        BD.ModifierAchat(base)

    if(commande4=="3"):
        BD.SupprimerAchat(base)

    if(commande4=="4"):
        BD.AfficherAchats(base)

if (commande=="5"):
    print("  1.Ajouter un reglement à une facture")
    print("  2.Modifier le reglement des achats")
    print("  3.Supprimer le reglement de la facture")
    print("  4.Afficher les reglements des factures")

    commande5 = input("Que voulez vous faire :")

    if(commande5=="1"):
        BD.AjouterReglement(base)

    if(commande5=="2"):
        BD.ModifierReglement(base)

    if(commande5=="3"):
        BD.SupprimerReglement(base)

    if(commande5=="4"):
        BD.AfficherReglements(base)