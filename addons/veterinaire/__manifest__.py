# -*- coding: utf-8 -*-
{
    'name': 'veterinaire',
    'summary': 'Gestion des vétérinaires et des animaux',
    'description': """
        Module Odoo pour la gestion des vétérinaires, des patients animaux et des rendez-vous.
    """,
    'author': 'My Company',
    'website': 'https://www.yourcompany.com',
    'category': 'Health',  # Catégorie de santé pour une application vétérinaire
   
    'version': '1.0',
    'depends': ['base'],  
    'data': [
        # Ajoutez ici les fichiers XML pour les vues, les données initiales, etc.
             'security/ir.model.access.csv',
             'views/veterinaire_animal.xml',
    ],
    'demo': [],  
    'installable': True,  # Indique que le module peut être installé
    'application': True,  # Indique que le module est une application principale
}
