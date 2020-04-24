# -*- coding: utf-8 -*-

##############################
#                            #
#        MarketBot v0.1      #
#          By ModzDev_       #
#                            #
##############################

# Enter your email Facebook account
email = "email.test@exemple.com"
# Enter your password Facebook account
password = "AwesomePass"
# Enter your phone number
phone_number = "01 02 03 04 05"


default_message = """
••CODE RÉDUCTION : ROUGE75

Rendez-vous chez DBC ELECTRONICS 
Situé au 154 BOULEVARD BERTHIER 75017
Métro 3 : Porte de Champerret, RER C pereire

7 jours / 7 sans interruption 
Du lundi au dimanche 
de 11h00 à 19h

100% d’origine à prix imbattable 🔥

Vendu avec accessoires facture et garantie grâce à mon code ROUGE75 à donner en caisse.
uniquement avec mon code : ROUGE75

( comme neuf un peu plus cher )
A partir de :

Voilà les stocks actuellement vous les mettez ça dans vos liste vous remplacer juste la partie des stocks ou il y a les prix des téléphones vous mettez ça à la place j’ai rajouté les nouvelles arrivages et enlever l’es rupture copier coller ça 

iPhone 5/5c 16go: 59€
iPhone 6S 64go : 99€
iPhone 6s Plus 32/64go : 149€
iPhone 7 32/128go : 149€
iPhone 8 64go : 229€
IPhone 7 Plus 32go : 229
iPhone X 64go : 359€
iPhone XS Max 64go : 579€


Samsung galaxy s5 16go : 79€
Samsung galaxy s7 32go :  139€
Samsung galaxy s7 edge 32go : 159€
Samsung galaxy s8 64go : 179€
Samsung galaxy s9 64go : 229€
Samsung galaxy s10e 128go : 379€
Samsung galaxy s10 128go : 419€
Samsung galaxy s10plus 128go : 499€
Samsung Note 10 256go : 499€
Samsung Note 10 plus 256go : 549€


iPad 2 16go : 79€
iPad 3 16go : 109€
iPad 4 16go : 169€
En 32go +30€
En 64go +45€

👇🏽👇🏽
*stock sous réserve de disponibilités 📱
**les prix varient selon l’état esthétique du produit
***l'adresse du magasin ainsi que les horaires sont tout en haut de la liste 

••CODE À NE SURTOUT PAS OUBLIEZ ROUGE75
"""

deliver_message = """
LE MAGASIN LIVRE UNIQUEMENT DES TELEPHONES NEUFS !
Les prix des téléphones seront légèrement plus chèrs car ils sont comme neuf. Le paiement se fera en espèce ou CB uniquement.

Pour prévoir une livraison, veuillez me contacter par SMS au {PHONE_NUMBER} et préciser votre numéro de téléphone valide, adresse complète et une carte d'identité.
""".format(PHONE_NUMBER=phone_number)

status_phone_message = """
Tous nos téléphones sont commes neufs. Les prix affichés sont ceux des téléphones les plus abîmés. En revanche, nous avons des téléphone d'occasions, comme neufs, sans traces d'usures. Les prix pour ces derniers sont bien entendu plus élevé.
"""

shop_adress_message = """
Le magasin se situe au 154 boulevard Berthier 75017, Métro 3: Porte de Champerret, RER C Pereire
"""