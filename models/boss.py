# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

from odoo import models,fields
#Esto es como se declara una clase en Phyton. Esta clase hereda todos los atributos de Model.
class Boss (models.Model):
    #Vamos a hacer una herencia de la clase user que existe en Odoo, añadiremos atributos extra que necesitamos para nuestro módulo
    _name = "emex51.boss"
    _inherit = 'res.users'
    
    # Declaración de los atributos de tipo básico de en Odoo.
    wage = fields.Float(string = "Salario")
    
    #Declaración de los atributos relacionales con otras clases.
    
    #Un jefe gestiona varios empleados.
    empleados = fields.One2many ('emex51.employee','jefe', string = "Empleados")