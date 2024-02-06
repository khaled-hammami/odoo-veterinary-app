# -*- coding: utf-8 -*-
from odoo import api, fields, models

class VeterinaireAnimal(models.Model):

    _name = "veterinaire.animal"  # Utilisez '_name' pour définir le nom du modèle
    _description = "Animal"  # Utilisez '_description' pour définir la description du modèle

    name = fields.Char()  # Utilisez 'fields.Char' pour définir un champ de texte
